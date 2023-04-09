import socket
from requsts import Requsts
from application import *


class Server_1:

    def __init__(self, ip_addr, host):
        self.ip_addr = ip_addr
        self.host_port = host

    def go_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.ip_addr, self.host_port))
        server.listen(1)
        while True:
            conn, adrr = server.accept()
            data = conn.recv(1024).decode('utf-8')
            try:
                try:
                    req = Requsts()
                    requst, user = req.parse(data)
                    res = Application()
                    respons = res.process(requst, user)
                    conn.send(respons)
                except Exception as e:
                    print(e)
            finally:
                conn.close()
