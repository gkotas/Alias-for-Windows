from __future__ import print_function
import os


ALIAS_DIR = os.path.dirname(__file__)


def printAlias(name):
    """
    Opens the name.cmd file and prints the value it's aliasing in the
    correct format.
    """
    with open('{}\\{}.cmd'.format(ALIAS_DIR, name)) as f:
        for i, line in enumerate(f):
            # Alias value is always the 4th line
            if i == 3:
                # Strip off " %*\n" from line
                print("alias {}={}".format(name, line[:-4]))
                break


def main(args):
    if args.p or not args.name:
        for cmd in os.listdir(ALIAS_DIR):
            if cmd.endswith('.cmd') and cmd not in ('alias.cmd', 'unalias.cmd'):
                printAlias(cmd[:-4])
        return

    args_name = ' '.join(args.name)
    print(args_name)

    if args_name.find('=') != -1:
        # '=' in arg, create .cmd for alias
        name, cmd = args_name.split('=', 1)

        # Remove quotes around value, if present
        # if cmd[0] == cmd[-1] and cmd[0] in "'\"":
            # cmd = cmd[1:-1]

        # Opening with 'w' will overwite
        with open('{}\\{}.cmd'.format(ALIAS_DIR, name), 'w') as f:
            f.write('@echo off\n')
            # Temp store current path
            f.write('set oldpath=%PATH%\n')
            # Removes the alias directory from the path because of infinite loops
            f.write('set PATH=%PATH:{};=%\n'.format(ALIAS_DIR))
            # The aliasing line
            f.write('{} %*\n'.format(cmd))
            # Restore path
            f.write('set PATH=%oldpath%\n')
            # Unset temp
            f.write('set oldpath=\n')

    else:
        # Just name of alias, print it
        printAlias(args_name)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        usage='alias [-p] [name[=value] ...]',
        add_help=False,
    )

    parser.add_argument('-p', action='store_true')
    parser.add_argument('name', nargs='*')

    main(parser.parse_args())
