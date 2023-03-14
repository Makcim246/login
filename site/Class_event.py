
class Event:

    def __init__(self, request):
        self.requests = request

    def schow_page(self):
        HDRS_CSS = 'HTTP/1.1 200 OK\r\nContent-Type: text/css; charseet=utf-8\r\n\r\n'
        HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charseet=utf-8\r\n\r\n'
        HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charseet=utf-8\r\n\r\n'
        path = self.requests.split(' ')[1]
        try:
            with open('site/template/base.html', 'rb') as file:
                response = file.read()
            with open('site/template' + path, 'rb') as file:
                response_1 = file.read()
                res = response.replace('{body}'.encode('utf-8'), response_1)
                if path == "/index.html" or path == "/abaut.html":
                    return HDRS.encode('utf-8') + res
                else:
                    return HDRS_CSS.encode('utf-8') + res
        except FileNotFoundError:
            return HDRS_404.encode('utf-8') + "Страница не найдена".encode('utf-8')

    def save_users_db(self):
        users = []
        path = self.requests.split(' ')[0]
        if path == 'POST':
            temp_data = self.requests.split('\n')[-1]
            temp_users = temp_data.split('&')
            for item in temp_users:
                users.append(item.split('=')[1])
        for item in users:
            if item == 'maks%40gmail.com':
                users[1] = '@'.join(item.split('%40'))
