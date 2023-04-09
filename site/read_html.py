def read_page(velues):
    with open('site/template/base.html', 'rb') as file:
        response = file.read()
    with open('site/template' + velues[0], 'rb') as file:
        response_1 = file.read()
        if velues[1] == 'GET':
            res = response.replace('{body}'.encode('utf-8'), response_1)
            return res
        elif velues[1] == 'POST' and velues[0] == '/registration.html':
            res = response.replace('{body}'.encode('utf-8'), 'everything is ok!'.encode('utf-8'))
            return res
        else:
            res = response.replace('{body}'.encode('utf-8'), 'Welcome!'.encode('utf-8'))
            return res

