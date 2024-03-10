import os

GLOBAL_DIRECTORY = os.path.expanduser('~/.gdrive-cli')
TOKEN_PATH = os.path.join(GLOBAL_DIRECTORY, 'token.pickle')

def create_global_directory():
    if not os.path.exists(GLOBAL_DIRECTORY):
        os.makedirs(GLOBAL_DIRECTORY)
        print(f"Created global directory: {GLOBAL_DIRECTORY}")

def setup(subparsers):
    parser = subparsers.add_parser(
        'logout', help='Log out of gdrive cli')
    parser.set_defaults(func=logout)

def logout(args): 
    create_global_directory()

    if os.path.exists(TOKEN_PATH):
        os.remove(TOKEN_PATH)
