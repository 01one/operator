import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template/index.html",page_title='example_title',page_meta="Example meta description tag")

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/about-us.html",page_title='About Page',page_meta="This About Page")

class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/contact.html")

def make_app(debug=False):
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/about-us", AboutHandler),
        (r"/contact", ContactHandler),
    ], template_path="templates", debug=debug)

if __name__ == "__main__":
    app = make_app(debug=True)
    app.listen(8888)
    print("Server is running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
