# -*- coding:utf-8 -*-
import os

from tornado.web import Application, RequestHandler, StaticFileHandler
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):

    def get(self):
        self.write('index')
        print(os.path.dirname(__file__))


if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    app = Application(
        [
            (r"/", IndexHandler),
            (r'^/()$', StaticFileHandler,
             {"path": os.path.join(current_path, "statics/html"), "default_filename": "index.html"}),
            (r'^/view/(.*)$', StaticFileHandler, {"path": os.path.join(current_path, "statics/html")}),
        ],
        static_path=os.path.join(current_path, "statics"), #静态文件
        template_path=os.path.join(os.path.dirname(__file__), "templates") # 模板渲染
    )

    app.listen(8001)
    IOLoop.current().start()
