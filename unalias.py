import os


ALIAS_DIR = os.path.dirname(__file__)


def main(args):
    if args.a:
        for cmd in os.listdir(ALIAS_DIR):
            if cmd.endswith('.cmd') and cmd not in ('alias.cmd', 'unalias.cmd'):
                os.remove(cmd)

    for cmd in args.name:
        # Don't delete the actual commands
        if cmd in ('alias', 'unalias'):
            continue

        cmd_path = "{}\\{}.cmd".format(ALIAS_DIR, cmd)
        if os.path.isfile(cmd_path):
            os.remove(cmd_path)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        usage='unalias [-a] name [name ...]',
        add_help=False,
    )

    parser.add_argument('-a', action='store_true')
    parser.add_argument('name', action='append')

    main(parser.parse_args())
