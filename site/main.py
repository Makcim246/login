from server import *
from random import randint


try:
    sess = Server_1('127.0.0.1', 8100)
    data = sess.go_server()
except OSError as OSE:
    print(OSE)
