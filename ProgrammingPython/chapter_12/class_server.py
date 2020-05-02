import socketserver
import time


my_host = ''
my_port = 50007


def now():
    return time.ctime(time.time())


class MyClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address, now())
        time.sleep(5)
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            reply = f'Echo => {data} at {now()}'
            self.request.send(reply.encode())
        self.request.close()


if __name__ == '__main__':
    my_addr = (my_host, my_port)
    server = socketserver.ThreadingTCPServer(my_addr, MyClientHandler)
    server.serve_forever()
