from threading import Thread
from time import sleep


class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = 'Hello Parallel Python CookBook!\n'

    def print_message(self):
        print(self.message)

    def run(self):
        print('Thread starting\n')
        x = 0
        while x < 10:
            self.print_message()
            sleep(2)
            x += 1
        print('Thread Ended\n')


if __name__ == '__main__':
    print('Process Started')
    hello_python = CookBook()
    hello_python.start()
    print('Process Ended')
