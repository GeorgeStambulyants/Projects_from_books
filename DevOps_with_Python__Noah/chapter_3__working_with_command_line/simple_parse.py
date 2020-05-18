#!/home/george_stamb/PyVenvs/Projects_from_books/DevOps_with_Python__Noah/venv/bin/python
#
# Simple command-line tool that echos user's input
# using argparse
#
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Echo your input')
    parser.add_argument('message', help='Message to echo')
    parser.add_argument(
        '--twice', '-t', help='Do it twice', action='store_true'
    )
    args = parser.parse_args()

    print(args.message)
    if args.twice:
        print(args.message)
