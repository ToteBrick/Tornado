# _*_coding: utf-8 _*_
import os

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options

define("port", default=8001, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        name = self.get_argument("name", "python", True)
        self.render('index.html', name=name)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    base_dir = os.path.dirname(__file__)
    handlers = [(r"/", IndexHandler), ]
    settings = {
        "template_path": os.path.join(base_dir, "templates"),
        "static_path": os.path.join(base_dir, "statics"),
        "debug": True
    }
    app = tornado.web.Application(handlers, **settings)  
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
