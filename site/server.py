import socket
from Class_event import *


class Server_1:

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
            start_server = f'http://127.0.0.1:{self.host_port}/index.html'
            print(f'Server started {start_server}')
            while True:
                self.conn, addr = server.accept()
                self.data = self.conn.recv(1024).decode('utf-8')
                event = Event(self.data)
                self.conn.send(event.schow_page())
                event.save_users_db()
                self.conn.shutdown(socket.SHUT_WR)
        except KeyboardInterrupt:
            server.close()
