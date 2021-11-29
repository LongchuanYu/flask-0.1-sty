from server.my_socketserver import MyTCPServer
from server.my_server import MyRequestHandler

if __name__ == '__main__':
    server = MyTCPServer(('localhost', 5000), MyRequestHandler)
    server.serve_forever()
