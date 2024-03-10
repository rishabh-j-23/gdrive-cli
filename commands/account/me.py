from googleapiclient.discovery import build

import os
import pickle

from cli.colors import Colors
from cli.authenticate import authenticate

SCOPES = ['https://www.googleapis.com/auth/drive']


def setup(subparsers):
    parser = subparsers.add_parser('me', help='User Details')
    parser.set_defaults(func=me)


def me(args):
    creds = authenticate()
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    service = build("drive", "v3", credentials=creds)

    results = service.about().get(fields="*").execute()['user']
    print("+-------------------------------------------------------------------------------------------------------")
    for key, value in results.items():
        print(
            f"{Colors.GREEN}{key.ljust(13).capitalize()}-> {Colors.BRIGHT_CYAN}{value}{Colors.RESET}")
    print("+-------------------------------------------------------------------------------------------------------")
