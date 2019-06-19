# -*- coding:utf-8 -*-
import os

from tornado.web import Application, RequestHandler, StaticFileHandler
from tornado.ioloop import IOLoop
import pymysql

db = pymysql.Connection(host='127.0.0.1', database='django_db', user='root', password='mysql', charset='utf8')


class IndexHandler(RequestHandler):

    def initialize(self):
        self.db = db
        self.cursor = db.cursor()

    def get(self):
        self.write('index')
        print(os.path.dirname(__file__))

    def post(self):
        title = self.get_argument("btitle")
        pub_date = self.get_argument("bpub_date")
        read = self.get_argument("bread")
        comment = self.get_argument("bcomment")
        delete = self.get_argument("is_delete")

        try:
            ret = self.cursor.execute(
                "insert into tb_books(btitle, bpub_date, bread,bcomment,is_delete) values(%s, %s, %s,%s,%s)", (title,
                pub_date, read, comment, delete))
        except Exception as e:
            self.db.rollback()
            self.write("DB error:%s" % e)
        else:
            self.db.commit()
            self.cursor.close()
            self.write("OK %d" % ret)


if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    app = Application(
        [
            (r"/", IndexHandler),
            (r'^/()$', StaticFileHandler,
             {"path": os.path.join(current_path, "statics/html"), "default_filename": "index.html"}),
            (r'^/view/(.*)$', StaticFileHandler, {"path": os.path.join(current_path, "statics/html")}),
        ],
        static_path=os.path.join(current_path, "statics"),  # 静态文件
        template_path=os.path.join(os.path.dirname(__file__), "templates")  # 模板渲染
    )

    app.listen(8001)
    IOLoop.current().start()
