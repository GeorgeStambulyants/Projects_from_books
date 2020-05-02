# !!! Program does not work on Windows !!!

import os
import sys
import time
from socket import *


my_host = ''
my_port = 50007


socketobj = socket(AF_INET, SOCK_STREAM)
socketobj.bind((my_host, my_port))
socketobj.listen(5)


def now():
    return time.ctime(time.time())


active_children = []


def reap_children():
    while active_children:
        pid, stat = os.waitpid(0, os.WNOHANG)
        if not pid:
            break
        active_children.remove(pid)


def handle_client(connection):
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data:
            break
        reply = f'Echo => {data} at {now()}'
        connection.send(reply.encode())
    connection.close()
    os._exit(0)


def dispatcher():
    while True:
        connection, address = socketobj.accept()
        print(f'Server connected by {address} at {now()}')
        reap_children()
        child_pid = os.fork()
        if child_pid == 0:
            handle_client(connection)
        else:
            active_children.append(child_pid)


if __name__ == '__main__':
    dispatcher()
