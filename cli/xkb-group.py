import argparse
import sys
from xkbgroup import XKeyboard

def main(args):
    xkb = XKeyboard()
    if args.l:
        print("\n".join(xkb.groups_names))
    elif args.p:
        print(xkb.group_name)
    elif args.s:
        xkb.group_name = args.s

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument("-l", help="list layout groups", action='store_true')
    command_group.add_argument("-p", help="show current layout groups", action='store_true')
    command_group.add_argument("-s", help="set current layout groups", type=str)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args(sys.argv[1:])
    main(args)
