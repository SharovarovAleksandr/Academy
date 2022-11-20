from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class HttpGetHandler(BaseHTTPRequestHandler):
    """Method GET realization"""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Привіт друже,</title></head>'.encode())
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<body><h1>Привіт це я!!!!</h1></body></html>'.encode())

def run(server_class=HTTPServer, handler_class=HttpGetHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

run()