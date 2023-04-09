from server import *


try:
    sess = Server_1('127.0.0.1', 8100)
    data = sess.go_server()
except OSError as OSE:
    print(OSE)
