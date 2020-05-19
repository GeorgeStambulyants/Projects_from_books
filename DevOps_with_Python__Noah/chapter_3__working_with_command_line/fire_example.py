#!/home/george_stamb/PyVenvs/Projects_from_books/DevOps_with_Python__Noah/venv/bin/python
#
# Simple command-line tool using fire
#
import fire


class Ships():

    def sail(self):
        ship_name = 'Your ship'
        print(f'{ship_name} is setting sail')

    def list(self):
        ships = ['John B', 'Yankee Clipper', 'Pequod']
        print(f'Ships: {",".join(ships)}')


def sailors(greeting, name):
    message = f'{greeting} {name}'
    print(message)


class Cli():
    def __init__(self):
        self.sailors = sailors
        self.ships = Ships()


if __name__ == '__main__':
    fire.Fire(Cli)
