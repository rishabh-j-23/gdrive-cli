import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle

from cli.colors import Colors

SCOPES = ['https://www.googleapis.com/auth/drive']
CREDENTIALS_PATH = 'credentials.json'


def setup(subparsers):
    parser = subparsers.add_parser(
        'login', help='gdrive-cli login through google account')
    parser.set_defaults(func=login)


def login(args): 
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print(Colors.RED + 'Follow https://github.com/rishabh-j-23/gdrive-cli/readme.md on how to create credentials.json file!')
                return
            flow = InstalledAppFlow.from_client_secrets_file(
                './credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
        
        return 
        
    else:
        print(Colors.GREEN + 'User already logged in' + Colors.RESET)