import sys
import time
from select import select
from socket import socket, AF_INET, SOCK_STREAM


my_host = ''
my_port = 50007

if len(sys.argv) == 3:
    my_host, my_port = sys.argv[1:]
num_port_socks = 2


def now():
    return time.ctime(time.time())


mainsocks, readsocks, writesocks = [], [], []
for i in range(num_port_socks):
    portsock = socket(AF_INET, SOCK_STREAM)
    portsock.bind((my_host, my_port))
    portsock.listen(5)
    mainsocks.append(portsock)

    readsocks.append(portsock)
    my_port += 1


print('select-server loop starting')
while True:
    print(readsocks)
    readables, writeables, exceptions = select(readsocks, writesocks, [])
    for sockobj in readables:
        if sockobj in mainsocks:
            newsock, address = sockobj.accept()

            print(f'Connect: {address} {id(newsock)}')
            readsocks.append(newsock)
        else:
            data = sockobj.recv(1024)
            print(f'\tgot {data} on {id(sockobj)}')
            if not data:
                sockobj.close()
                readsocks.remove(sockobj)
            else:
                reply = f'Echo => {data} at {now()}'
                sockobj.send(reply.encode())
