import time
import socket
import signal

class MyTCPServer(object):
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 5

    def __init__(self, server_address, RequestHandlerClass):
        self.RequestHandlerClass = RequestHandlerClass
        self.server_address = server_address
        self.request = None
        self.client_addr = None
        self._headers_buffer = []
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        self.server_bind_and_activate()
        self.exited = False

    def server_bind_and_activate(self):
        self.socket.bind(self.server_address)
        self.socket.listen(self.request_queue_size)

    def shutdown_request(self, request):
        """Called to shutdown and close an individual request."""
        try:
            #explicitly shutdown.  socket.close() merely releases
            #the socket and waits for GC to perform the actual close.
            request.shutdown(socket.SHUT_WR)
        except OSError:
            pass #some platforms may raise ENOTCONN here
        request.close()
        print('server closed')

    def serve_forever(self):
        while not self.exited:
            self.request_handler()
            time.sleep(5)

    def request_handler(self):
        # setup() -> handle() -> finish()
        self.request, self.client_addr = self.socket.accept()
        self.RequestHandlerClass(self.request, self.client_addr, self)
