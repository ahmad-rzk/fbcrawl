from scrapy.exporters import BaseItemExporter
from scrapy.utils.serialize import ScrapyJSONEncoder
from scrapy.utils.python import to_bytes
from fbcrawl.tcp_contract import prepare_msg

import logging
import zmq
import datetime
import threading


class TCPExports(BaseItemExporter):

    def __init__(self, outputAddress, **kwargs):
        self._configure(kwargs, dont_fail=True)
        # self.file = file
        # needs to be updated when migrating to proto-buff
        self.encoder = ScrapyJSONEncoder(**kwargs)
        self.first_item = True
        # creating ZMQ context and socket
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        # self.socket.setsockopt(zmq.LINGER, 100)
        self.outputAddress = outputAddress

    def start_exporting(self):
        # Connecting the socket
        self.socket.bind(str(self.outputAddress))

    def export_item(self, item):
        # sending the item
        msg: dict = {'value': b'MSG'}

        # thread = threading.Thread(target=prepare_msg, args=(item, msg))
        # thread.start()
        # thread.join()

        msg['value'] = prepare_msg(item, msg)

        if not msg is None:
            self.socket.send(msg['value'])
        # while True:
        #     if not msg is None:
        #         self.socket.send(msg['value'])
        #         break

    def finish_exporting(self):
        # Closing the socket
        self.socket.close()
