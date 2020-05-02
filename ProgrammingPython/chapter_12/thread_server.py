import time
import _thread as thread
from socket import *


my_host = ''
my_port = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((my_host, my_port))
sockobj.listen(5)


def now():
    return time.ctime(time.time())


def handle_client(connection):
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data:
            break
        reply = f'Echo => {data} at {now()}'
        connection.send(reply.encode())
    connection.close()


def dispatcher():
    while True:
        connection, address = sockobj.accept()
        print(f'Server connected by {address} at {now()}')
        thread.start_new_thread(handle_client, (connection,))


if __name__ == '__main__':
            dispatcher()
