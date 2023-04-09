from response import *
from read_html import *
from db_user import *
import hashlib


class Application:

    def registration(self, data, password_user):
        res = Response(read_page(data), data[0])
        return res.return_respons(password_user)

    def home_page(self, data):
        res = Response(read_page(data), data[0])
        return res.return_respons()

    def sign_in(self, data, password_user):
        res = Response(read_page(data), data[0])
        return res.return_respons(password_user)

    def process(self, req, user):
        password_user = ''
        HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charseet=utf-8\r\n\r\n'
        velues = req[0]
        try:
            match velues:
                case '/index.html':
                    res = self.home_page(req)
                    return res
                case '/registration.html':
                    if len(user) == 3:
                        password_user = user[2]
                    res = self.registration(req, password_user)
                    if req[1] == 'POST':
                        conect_db(user)
                    return res
                case '/sign_in.html':
                    res = self.sign_in(req, password_user)
                    return res
        except FileNotFoundError:
            return HDRS_404.encode('utf-8') + "Страница не найдена".encode('utf-8')

