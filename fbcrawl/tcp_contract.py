from fbcrawl.items import FbcrawlItem
from fbcrawl.items import CommentsItem
from fbcrawl.pbitems import FbcrawlNativeItem
from fbcrawl.pbitems import CommentNativeItem
from google.protobuf import message
from chardet import detect
# test json
import json
import fbcrawl

# A method to be injected


def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__,
                      sort_keys=True, indent=4)


def prepare_msg(item, msg):

    # Default Empty Res
    res = bytes(("0").encode(
        encoding='UTF-8', errors='strict'))

    if type(item) is fbcrawl.items.FbcrawlItem:
        res = bytes((__convert_to_native_fbcrawler(item)).encode(
            encoding='UTF-8', errors='strict'))

    elif type(item) is fbcrawl.items.CommentsItem:
        res = bytes((__convert_to_native_comment(item)).encode(
            encoding='UTF-8', errors='strict'))

    return res


def __convert_to_native_fbcrawler(item):
    # WERE USED WITH Proto-buff
    # target = FbcrawlNativeItem.FbCrawlItem()
    # target.source = str(item['source'])
    # # target.date = item['date']
    # target.text = str(item['text'])
    # target.comments = str(item['comments'])
    # target.reactions = __get_number(item['reactions'])
    # # target.share = str(item['share'])
    # target.url = str(item['url'])
    # target.post_id = str(item['post_id'])
    # # target.shared_from = str(item['shared_from'])
    # # return json.dumps(item)

    # # remove
    # target.date = 123456789
    # target.shared_from = str("rzk")
    # target.share = str("70000 Share")

    # yield (target)
    # msg = (item.toJSON())
    setattr(type(item), 'toJSON', toJSON)
    return item.toJSON()
    # return str(target.SerializeToString())


def __convert_to_native_comment(item):
    # target = CommentsItem()
    # target.source = item.source
    # target.reply_to = item.reply_to
    # target.date = item.date
    # target.text = item.text
    # target.reactions = item.reactions
    # target.source_url = item.source_url
    # target.url = item.url
    # return bytearray(target.SerializeToString(), 'UTF-8')
    setattr(type(item), 'toJSON', toJSON)
    return item.toJSON()


def __get_number(string_val):
    to_be_processed_val: str = str(string_val).strip().upper()
    # Null Check
    if not to_be_processed_val:
        return 0
    if to_be_processed_val.endswith('K'):
        return int(float(to_be_processed_val[0:-1]) * 1000)
    elif to_be_processed_val.endswith('M'):
        return int(float(to_be_processed_val[0:-1]) * 1000000)
    else:
        return int(to_be_processed_val)
