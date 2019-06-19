import os
import json
import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.httpclient import HTTPClient, AsyncHTTPClient
from tornado.options import define, options

define("port", default=8001, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('async.html')

    # 同步版
    # def post(self):
    #     if self.get_argument("search",False):
    #         search_text = self.get_argument("search")
    #     else:
    #         search_text = json.loads(self.request.body)["search"]
    #     client = HTTPClient()
    #     res = client.fetch("https://suggest.taobao.com/sug?code=utf-8&q=%s"%search_text)
    #     context = res.body.decode("utf8")
    #     self.write(context)

    # 异步版
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        if self.get_argument("search", False):
            search_text = self.get_argument("search")
        else:
            search_text = json.loads(self.request.body)["search"]
        client = AsyncHTTPClient()
        res = yield tornado.gen.Task(client.fetch, "https://suggest.taobao.com/sug?code=utf-8&q=%s" % search_text)
        content = res.body.decode("utf8")
        self.write(content)
        self.finish()


if __name__ == "__main__":
    tornado.options.parse_command_line()
    base_dir = os.path.dirname(__file__)
    handlers = [(r"/", IndexHandler), ]
    settings = {
        "template_path": os.path.join(base_dir, "templates"),
        "static_path": os.path.join(base_dir, "static"),
        "debug": True
    }
    app = tornado.web.Application(handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
