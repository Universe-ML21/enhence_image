from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from enhance import toImage
items = []


class TodoItems(RequestHandler):
    def get(self):
        self.write({'items': items})


class TodoItem(RequestHandler):
    def post(self):
        data = self.request.body
        img = toImage(data)
        print(" 200")
        self.write({
            "msg": 200,
            "img_enhanced": img.decode()
        })


def make_app():
    urls = [
        ("/", TodoItems),
        # (r"/api/item/([^/]+)?", TodoItem)
        (r"/api/get_enhanced_img_base64", TodoItem)
    ]
    return Application(urls, debug=True)


if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()
