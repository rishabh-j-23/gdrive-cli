import os

def setup(subparsers):
    parser = subparsers.add_parser(
        'logout', help='Log out of gdrive cli')
    parser.set_defaults(func=logout)


def logout(args): 
    if os.path.exists('token.pickle'):
        os.remove('token.pickle')
