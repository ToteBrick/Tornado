# _*_coding: utf-8 _*_
import os
import random

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options

define("port", default=8001, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):

    def initialize(self, upload, download):
        '''文件上传与下载'''
        self.upload = upload
        self.download = download

    def get(self):
        name = self.get_argument("name", "python", True)
        get_img = self.get_argument("get_img", "false", True)
        if get_img != "true":
            self.render('photo.html', name=name)
        else:
            # set_header方法设置header头
            self.set_header('Content-Type', 'application/octet-stream')
            # self.set_header('Content-Disposition', 'attachment; filename="随机图片.png"')
            img_list = os.listdir(self.download)
            img_path = random.choice(img_list)
            with open(os.path.join(self.download, img_path), 'rb') as f:
                while True:
                    data = f.read(4096)
                    if not data:
                        break
                    self.write(data)

    def post(self):
        files = self.request.files
        # {"head_img":[{"filename":"..","content_type":"...","body":"..."}]}
        head_img_obj = files.get('head_img')[0]
        if head_img_obj:
            head_img_path = os.path.join(self.upload, head_img_obj['filename'])
            with open(head_img_path, 'wb') as f:
                f.write(head_img_obj["body"])
        self.write("success !")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    base_dir = os.path.dirname(__file__)
    settings = {
        "template_path": os.path.join(base_dir, "templates"),
        "static_path": os.path.join(base_dir, "statics"),
        "debug": True
    }
    handlers = [
        (r"/", IndexHandler, dict(
            upload=os.path.join(settings["static_path"], "upload"),
            download=os.path.join(settings["static_path"], "download")
        )),
    ]

    app = tornado.web.Application(handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
