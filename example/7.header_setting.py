# -*- coding:utf-8 -*-

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):
    def set_default_headers(self):
        # 第二种响应头设置方式
        print("---------> 响应头set_default_headers()执行")
        self.set_header("Content-type", "application/json; charset=utf-8")
        self.set_header("name", "simon")

    def get(self):
        # 第一种操作响应头的方式：
        # self.set_header("Content-type", "application/json")
        print("---------->get方法执行")
        self.write("{'name':'simon'}")
        self.set_header("name", "simon")


if __name__ == "__main__":
    app = Application([(r"/", IndexHandler)])

    app.listen(8000)

    IOLoop.current().start()
