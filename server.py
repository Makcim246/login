import socket
from pesponse import *


class Server_1:

    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charseet=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charseet=utf-8\r\n\r\n'

    def __init__(self, ip_addr, host, conn=None, data=None):
        self.ip_addr = ip_addr
        self.host_port = host
        self.conn = conn
        self.data = data

    def go_server(self):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((self.ip_addr, self.host_port))
            server.listen(4)
            while True:
                self.conn, addr = server.accept()
                self.data = self.conn.recv(1024).decode('utf-8')
                self.conn.send(load_html(self.data))
                self.conn.shutdown(socket.SHUT_WR)
        except KeyboardInterrupt:
            server.close()
        return self.data
