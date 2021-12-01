# coding=utf-8
import socket


class MyRequestHandler:
    def __init__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server

        self.conn = None
        self.rfile = None
        self.wfile = None
        self._headers_buffer = []

        self.setup()
        try:
            self.handle()
        finally:
            self.finish()

    def setup(self):
        self.conn = self.request
        self.conn.settimeout(5)
        self.conn.setsockopt(socket.IPPROTO_TCP,
                             socket.TCP_NODELAY, True)
        self.rfile = self.conn.makefile('rb', -1)
        # self.wfile = _SocketWriter(self.connection)
        self.wfile = self.conn.makefile('wb', 0)

    def handle(self):
        # handle one request
        raw_requestline = self.rfile.readline(-1)
        body = 'ly test'
        self.send_response(200, 'OK')
        self.send_body(body)

        # must flush at the end
        self.wfile.flush()

    def finish(self):
        if not self.wfile.closed:
            try:
                self.wfile.flush()
                # ??? 请求完毕之后必须关闭连接，否则客户端会一直等待
                self.conn.close()
            except socket.error as e:
                # A final socket error may have occurred here, such as
                # the local error ECONNABORTED.
                print(e)
        self.wfile.close()
        self.rfile.close()

    # core
    def send_response(self, code, message=None):
        self._headers_buffer.append(("%s %d %s\r\n" %
                                     ('HTTP/1.0', code, message)).encode(
            'latin-1', 'strict'))

        self.send_header("Content-type", 'text/plain')
        self.send_header("Content-Length", str(10))
        self.end_headers()

    def send_header(self, keyword, value):
        """Send a MIME header to the headers buffer."""
        self._headers_buffer.append(
            ("%s: %s\r\n" % (keyword, value)).encode('latin-1', 'strict'))

    def end_headers(self):
        """Send the blank line ending the MIME headers."""
        self._headers_buffer.append(b"\r\n")
        # flush headers
        self.wfile.write(b"".join(self._headers_buffer))
        self._headers_buffer = []

    def send_body(self, body):
        self.wfile.write(body.encode('UTF-8', 'replace'))
