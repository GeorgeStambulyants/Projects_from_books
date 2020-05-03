import sys
import time
import os
import _thread as thread
from socket import *


blksz = 1024
default_host = 'localhost'
default_port = 50001

helptext = '''
    USAGE...
    server => getfile.py -mode server             [-port nnn] [-host hhh|localhost]
    client => getfile.py [-mode client] -file fff [-port nnn] [-host hhh|localhost]
'''


def now():
    return time.asctime()


def parsecommandline():
    options = {}
    args = sys.argv[1:]
    while len(args) >= 2:
        options[args[0]] = args[1]
        args = args[2:]
    return options


def client(host, port, filename):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send((filename + '\n').encode())
    dropdir = os.path.split(filename)[1]
    file = open(dropdir, 'wb')
    while True:
        data = sock.recv(blksz)
        if not data:
            break
        file.write(data)
    sock.close()
    file.close()
    print(f'Client got {filename} at {now()}')


def serverthread(clientsock):
    sockfile = clientsock.makefile('r')
    filename = sockfile.readline()[:-1]

    try:
        file = open(filename, 'rb')
        while True:
            bytes = file.read(blksz)
            if not bytes:
                break
            sent = clientsock.send(bytes)
            assert sent == len(bytes)
    except Exception as e:
        print(e)
        print(f'Error downloading file on server: {filename}')
    clientsock.close()


def server(host, port):
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind((host, port))
    serversock.listen(5)
    while True:
        clientsock, clientaddr = serversock.accept()
        print(f'Server connected by {clientaddr} at {now()}')
        thread.start_new_thread(serverthread, (clientsock,))


def main(args):
    host = args.get('-host', default_host)
    port = args.get('-post', default_port)
    if args.get('-mode') == 'server':
        if host == 'localhost':
            host = ''
        server(host, port)
    elif args.get('-file'):
        client(host, port, args['-file'])
    else:
        print(helptext)


if __name__ == '__main__':
    args = parsecommandline()
    main(args)
