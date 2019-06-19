# -*- coding:utf-8 -*-

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):

    def get(self):
        self.write("hello simon.com")
        self.set_cookie("user", "admin")
        print(self.get_cookie("user"))
        print(self.cookies)


if __name__ == "__main__":
    app = Application([(r"/", IndexHandler)])

    app.listen(8000)

    IOLoop.current().start()
