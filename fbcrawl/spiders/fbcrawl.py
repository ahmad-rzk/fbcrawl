import scrapy
import logging

from scrapy.loader import ItemLoader
from scrapy.http import FormRequest
from scrapy.exceptions import CloseSpider
from fbcrawl.items import FbcrawlItem, parse_date, parse_date2
from datetime import datetime
from fbcrawl.spiders.assets.fbcrawl_consts import *



class FacebookSpider(scrapy.Spider):
    '''
    Parse FB pages (needs credentials)
    '''
    name = 'fb'
    # custom_settings = {
    #     'FEED_EXPORT_FIELDS': ['source','shared_from','date','text', \
    #                            'reactions','likes','ahah','love','wow', \
    #                            'sigh','grrr','comments','post_id','url']
    # }
    custom_settings = {
        'FEED_EXPORT_FIELDS': ['source','shared_from','date','text', \
                               'reactions', \
                               'comments','post_id','url']
    }


    def __init__(self, *args, **kwargs):
        #turn off annoying logging, set LOG_LEVEL=DEBUG in settings.py to see more logs
        logger = logging.getLogger('scrapy.middleware')
        logger.setLevel(logging.WARNING)

        super().__init__(*args,**kwargs)

        #email & pass need to be passed as attributes!
        if 'email' not in kwargs or 'password' not in kwargs:
            raise AttributeError('You need to provide valid email and password:\n'
                                 'scrapy fb -a email="EMAIL" -a password="PASSWORD"')
        else:
            self.logger.info('Email and password provided, will be used to log in')

        #page name parsing (added support for full urls)
        if 'page' in kwargs:
            if self.page.find('/groups/') != -1:
                self.group = 1
            else:
                self.group = 0
            if self.page.find('https://www.facebook.com/') != -1:
                self.page = self.page[25:]
            elif self.page.find('https://mbasic.facebook.com/') != -1:
                self.page = self.page[28:]
            elif self.page.find('https://m.facebook.com/') != -1:
                self.page = self.page[23:]


        #parse date
        if 'date' not in kwargs:
            self.logger.info('Date attribute not provided, scraping date set to 2004-02-04 (fb launch date)')
            self.date = datetime(2004,2,4)
        else:
            self.date = datetime.strptime(kwargs['date'],'%Y-%m-%d')
            self.logger.info('Date attribute provided, fbcrawl will stop crawling at {}'.format(kwargs['date']))
        self.year = self.date.year

        #parse lang, if not provided (but is supported) it will be guessed in parse_home
        if 'lang' not in kwargs:
            self.logger.info('Language attribute not provided, fbcrawl will try to guess it from the fb interface')
            self.logger.info('To specify, add the lang parameter: scrapy fb -a lang="LANGUAGE"')
            self.logger.info('Currently choices for "LANGUAGE" are: "en", "es", "fr", "it", "pt"')
            self.lang = '_'
        elif self.lang == 'en'  or self.lang == 'es' or self.lang == 'fr' or self.lang == 'it' or self.lang == 'pt':
            self.logger.info('Language attribute recognized, using "{}" for the facebook interface'.format(self.lang))
        else:
            self.logger.info('Lang "{}" not currently supported'.format(self.lang))
            self.logger.info('Currently supported languages are: "en", "es", "fr", "it", "pt"')
            self.logger.info('Change your interface lang from facebook settings and try again')
            raise AttributeError('Language provided not currently supported')

        #max num of posts to crawl
        if 'max' not in kwargs:
            self.max = int(10e5)
        else:
            self.max = int(kwargs['max'])

        #current year, this variable is needed for proper parse_page recursion
        self.k = datetime.now().year
        #count number of posts, used to enforce DFS and insert posts orderly in the csv
        self.count = 0

        self.start_urls = ['https://mbasic.facebook.com']

        #the socket to output to 
        if 'outputAddress' not in kwargs:
            self.outputAddress = "tcp://127.0.0.1:8"
        else:
            self.outputAddress = str(kwargs['outputAddress'])


    def parse(self, response):
        '''
        Handle login with provided credentials
        '''
        return FormRequest.from_response(
                response,
                formxpath=xLOGIN_FORM,
                formdata={'email': self.email,'pass': self.password},
                callback=self.parse_home
                )

    def parse_home(self, response):
        '''
        This method has multiple purposes:
        1) Handle failed logins due to facebook 'save-device' redirection
        2) Set language interface, if not already provided
        3) Navigate to given page
        '''
        #handle 'save-device' redirection
        if response.xpath(xSAVE_DEVICE_HYPERLINK):
            self.logger.info('Going through the "save-device" checkpoint')
            return FormRequest.from_response(
                response,
                formdata={'name_action_selected': 'dont_save'},
                callback=self.parse_home
                )

        #set language interface
        if self.lang == '_':
            found = False
            for key,val in xUI_LANGUAGES_.items():
                 if response.xpath(val):
                    self.logger.info('Language recognized: lang="%s"' % key)
                    self.lang = key
                    found=True
                    break

            if not found:
                    raise AttributeError('Language not recognized\n'
                                     'Change your interface lang from facebook '
                                     'and try again')

        #navigate to provided page
        href = response.urljoin(self.page)
        self.logger.info('Scraping facebook page {}'.format(href))
        return scrapy.Request(url=href,callback=self.parse_page,meta={'index':1})

    def parse_page(self, response):
        '''
        Parse the given page selecting the posts.
        Then ask recursively for another page.
        '''
#        #open page in browser for debug
#        from scrapy.utils.response import open_in_browser
#        open_in_browser(response)

        #select all posts
        for post in response.xpath(xPOST_['root']):

            many_features = post.xpath(xPOST_['attributes']['many_features']).get()
            date = []
            date.append(many_features)
            date = parse_date(date,{'lang':self.lang})
            current_date = datetime.strptime(date,'%Y-%m-%d %H:%M:%S') if date is not None else date

            if current_date is None:
                date_string = post.xpath('.//abbr/text()').get()
                date = parse_date2([date_string],{'lang':self.lang})
                current_date = datetime(date.year,date.month,date.day) if date is not None else date
                date = str(date)

            #if 'date' argument is reached stop crawling
            if self.date > current_date:
                raise CloseSpider('Reached date: {}'.format(self.date))

            new = ItemLoader(item=FbcrawlItem(),selector=post)
            if abs(self.count) + 1 > self.max:
                raise CloseSpider('Reached max num of post: {}. Crawling finished'.format(abs(self.count)))
            self.logger.info('Parsing post n = {}'.format(abs(self.count)))
            new.add_xpath('comments', xPOST_['attributes']['comments'])
            new.add_value('date',date)
            new.add_xpath('post_id',xPOST_['attributes']['post_id'])
            new.add_xpath('url', xPOST_['attributes']['url'])

            #page_url #new.add_value('url',response.url)

            #returns full post-link in a list
            post = post.xpath(xPOST_['attributes']['post-link']).extract()
            temp_post = response.urljoin(post[0])
            self.count -= 1
            yield scrapy.Request(temp_post, self.parse_post, priority = self.count, meta={'item':new})

        #load following page, try to click on "more"
        if self.group == 1:
            new_page = response.xpath("//div[contains(@id,'stories_container')]/div[2]/a/@href").extract()
        else:
            new_page = response.xpath(xMORE_POSTS_HYPERLINK).extract()

        if not new_page:
            self.logger.info('[!] "more" link not found, will look for a year')
            #self.k is the year that we look for in the link.
            if response.meta['flag'] == self.k and self.k >= self.year:
                self.logger.info('There are no more, flag set at = {}'.format(self.k))
                xpath = xYEAR_HYPERLINK % (str(self.k))
                new_page = response.xpath(xpath).extract()
                if new_page:
                    new_page = response.urljoin(new_page[0])
                    self.k -= 1
                    self.logger.info('Found a link for year "{}", new_page = {}'.format(self.k,new_page))
                    yield scrapy.Request(new_page, callback=self.parse_page, meta={'flag':self.k})
                else:
                    while not new_page: #sometimes the years are skipped this handles small year gaps
                        self.logger.info('Link not found for year {}, trying with previous year {}'.format(self.k,self.k-1))
                        self.k -= 1
                        if self.k < self.year:
                            raise CloseSpider('Reached date: {}. Crawling finished'.format(self.date))
                        xpath = xYEAR_HYPERLINK % (str(self.k))
                        new_page = response.xpath(xpath).extract()
                    self.logger.info('Found a link for year "{}", new_page = {}'.format(self.k,new_page))
                    new_page = response.urljoin(new_page[0])
                    self.k -= 1
                    yield scrapy.Request(new_page, callback=self.parse_page, meta={'flag':self.k})
            else:
                self.logger.info('Crawling has finished with no errors!')
        else:
            new_page = response.urljoin(new_page[0])
            if 'flag' in response.meta:
                self.logger.info('Page scraped, clicking on "more"! new_page = {}'.format(new_page))
                yield scrapy.Request(new_page, callback=self.parse_page, meta={'flag':response.meta['flag']})
            else:
                self.logger.info('First page scraped, clicking on "more"! new_page = {}'.format(new_page))
                yield scrapy.Request(new_page, callback=self.parse_page, meta={'flag':self.k})

    def parse_post(self,response):
        new = ItemLoader(item=FbcrawlItem(),response=response,parent=response.meta['item'])
        new.context['lang'] = self.lang
        new.add_xpath('source',xPOST_['attributes']['source'])
        new.add_xpath('shared_from',xPOST_['attributes']['shared_from'])
     #   new.add_xpath('date','//div/div/abbr/text()')
        new.add_xpath('text',xPOST_['attributes']['text'])

        check_reactions = response.xpath(xPOST_['attributes']['reactions']).get()
        if not check_reactions:
            yield new.load_item()
        else:
            new.add_xpath('reactions',xPOST_['attributes']['reactions'])
#            reactions = response.xpath(xREACTIONS_['root'])
#            reactions = response.urljoin(reactions[0].extract())
            yield new.load_item()
#            yield scrapy.Request(reactions, callback=self.parse_reactions, meta={'item':new})

    # def parse_reactions(self,response):
    #     new = ItemLoader(item=FbcrawlItem(),response=response, parent=response.meta['item'])
    #     new.context['lang'] = self.lang
    #     new.add_xpath('likes',xREACTIONS_['attributes']['likes'])
    #     new.add_xpath('ahah',xREACTIONS_['attributes']['ahah'])
    #     new.add_xpath('love',xREACTIONS_['attributes']['love'])
    #     new.add_xpath('wow',xREACTIONS_['attributes']['wow'])
    #     new.add_xpath('sigh',xREACTIONS_['attributes']['sigh'])
    #     new.add_xpath('grrr',xREACTIONS_['attributes']['grrr'])
    #     yield new.load_item()
