def load_html(requsts):
    HDRS_CSS = 'HTTP/1.1 200 OK\r\nContent-Type: text/css; charseet=utf-8\r\n\r\n'
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charseet=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charseet=utf-8\r\n\r\n'
    print(requsts)
    path = requsts.split(' ')[1]
    try:
        with open('template/base.html', 'rb') as file:
            response = file.read()
        with open('template' + path, 'rb') as file:
            response_1 = file.read()
            res = response.replace('{body}'.encode('utf-8'), response_1)
            if path == "/index.html" or path == "/abaut.html":
                return HDRS.encode('utf-8') + res
            else:
                return HDRS_CSS.encode('utf-8') + res
    except FileNotFoundError:
        return HDRS_404.encode('utf-8') + "Страница не найдена".encode('utf-8')
