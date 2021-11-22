# coding=utf-8
import socketserver
import sys
import SimpleHTTPServer
from http.server import HTTPServer, BaseHTTPRequestHandler


class WSGIRequestHandler(BaseHTTPRequestHandler, object):

    """A request handler that implements WSGI dispatching."""

    @property
    def server_version(self):

        return "Werkzeug/" + '1.0.0'

    def handle_one_request(self):
        """Handle a single HTTP request."""
        self.raw_requestline = self.rfile.readline()  # GET / HTTP/1.1
        print(self.raw_requestline)

    def send_response(self, code, message=None):
        """Send the response header and log the response code."""
        print('here...')
        if message is None:
            message = code in self.responses and self.responses[code][0] or ""
        if self.request_version != "HTTP/0.9":
            hdr = "%s %d %s\r\n" % (self.protocol_version, code, message)
            self.wfile.write(hdr.encode("ascii"))


class BaseServer(HTTPServer, object):
    def __init__(self):
        HTTPServer.__init__(self, ('localhost', 5000), WSGIRequestHandler)

    def serve_forever(self):
        HTTPServer.serve_forever(self)


b = BaseServer()
b.serve_forever()
