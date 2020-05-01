from socket import *


my_host = ''
my_port = 50007

socketobj = socket(AF_INET, SOCK_STREAM)
socketobj.bind(my_host, my_post)
socketobj.listen(5)


while True:
    conntection, address = socketobj.accept()

    print(f'Server connected by {address}')

    while True:
        data = conntection.recv(1024)
        if not data:
            break
        conntection.send(b'Echo => ' + data)
    conntection.close()
