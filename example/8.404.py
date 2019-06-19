# -*- coding:utf-8 -*-

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):

    def get(self):
        self.write("hello, simon.com")

        self.send_error(404, msg="页面丢失", info="家里服务器崩溃了")

    def write_error(self, status_code, **kwargs):
        self.write("<h1>出错啦，工程师正在加紧修复中.....</h1>")
        self.write("<p>错误信息:%s</p>" % kwargs["msg"])
        self.write("<p>错误描述:%s</p>" % kwargs["info"])


if __name__ == "__main__":
    app = Application([(r"/", IndexHandler)])

    app.listen(8000)

    IOLoop.current().start()
