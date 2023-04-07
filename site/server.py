import socket
from Class_event import *


class Server_1:

    def __init__(self, ip_addr, host):
        self.ip_addr = ip_addr
        self.host_port = host

    def go_server(self):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((self.ip_addr, self.host_port))
            server.listen(4)
            start_server = f'http://127.0.0.1:{self.host_port}/index.html'
            print(f'Server started {start_server}')
            while True:
                conn, addr = server.accept()
                data = conn.recv(1024).decode('utf-8')
                event = Event()
                conn.send(event.schow_page(data))
                event.save_users_db(data)
                conn.shutdown(socket.SHUT_WR)
        except KeyboardInterrupt:
            conn.close()
