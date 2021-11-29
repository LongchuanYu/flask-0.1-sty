from http_test.server import SimpleHTTPRequestHandler

from server import socketserver


if __name__ == '__main__':
    PORT = 5000
    httpd = socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler)
    print("serving at port", PORT)
    httpd.serve_forever()
