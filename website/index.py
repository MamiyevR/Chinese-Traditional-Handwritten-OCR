import tornado.web
import tornado.ioloop

class uploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    
    def post(self):
        files = self.request.files["imgFile"]
        for f in files:
            fh = open(f"website/img/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
        
        self.write(f"<a href = 'http://localhost:8080/website/img/{f.filename}'>")

if(__name__ == "__main__"):
    app = tornado.web.Application([
        ("/", uploadHandler),
        ("/website/img/(.*)", tornado.web.StaticFileHandler, {"path": "website/img"})
    ])

    app.listen(8080)
    print("Listening on port 8080")

    tornado.ioloop.IOLoop.instance().start()
