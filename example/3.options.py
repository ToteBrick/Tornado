# -*- coding:utf-8 -*-

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import tornado.options

# 全局配置-改变端口
tornado.options.define('port', default=8000, type=int, help="this is the port >for application")


class IndexHandler(RequestHandler):
    def get(self):
        self.write('全局配置')


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    tornado.options.parse_command_line()  # 命令行参数转换

    http_server = HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)
    # 启动IOLoop轮循监听
    IOLoop.current().start()
