import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from functools import partial

HERE = os.path.dirname(os.path.abspath(__file__))

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", ""):
            self.path = "/index.html"          # root returns the JSON
        elif self.path.endswith(".py"):
            self.send_error(404)              # don't expose the script
            return
        super().do_GET()

HTTPServer(("127.0.0.1", 8000), partial(Handler, directory=HERE)).serve_forever()