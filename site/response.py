class Response:

    def __init__(self, body, host):
        self.host = host
        self.body = body

    def return_respons(self, token):
        cookie = f"token={token}; Expires=Fri, 07-Jul-23 13:22:07 GMT; Domain=127.0.0.1:8100 Path=/"
        HDRS_CSS = 'HTTP/1.1 200 OK\r\nContent-Type: text/css; charseet=utf-8\r\n\r\n'
        HDRS_ICON = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charseet=utf-8\r\n\r\n'
        HDRS = f'HTTP/1.1 200 OK\r\n{cookie}\r\nContent-Type: text/html; charseet=utf-8\r\n\r\n'
        HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charseet=utf-8\r\n\r\n'
        return HDRS.encode('utf-8') + self.body

