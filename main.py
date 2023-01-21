import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8000))
server.listen(1)

while True:
    conn, addr = server.accept()
    print(f'Connection server: {addr}')
    request = conn.recv(1024).decode('utf-8')
    print(request)
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charseet=utf-8\r\n\r\n'
    response = 'test'.encode('utf-8')
    conn.send(HDRS.encode('utf-8') + response)
    conn.close()
    print('Connection closed\n')
