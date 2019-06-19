# -*- coding:utf-8 -*-
import json

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):
    def get(self):
        print(self.request)

        json_str = {"username": "admin", "password": "123123"}
        # self.write(json.dumps(json_str))
        self.write(json_str)


if __name__ == "__main__":
    app = Application([(r"/", IndexHandler)])

    app.listen(8001)

    IOLoop.current().start()
