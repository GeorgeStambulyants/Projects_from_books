import sys
from socket import *


server_host = 'localhost'
server_port = 50007

message = [b'Hello network world']

if len(sys.argv) > 1:
    server_host = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])


socketobj = socket(AF_INET, SOCK_STREAM)
socketobj.connect((server_host, server_port))

for line in message:
    socketobj.send(line)
    data = socketobj.recv(1024)
    print(f'Client received: {data}')

socketobj.close()
