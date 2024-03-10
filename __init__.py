import argparse
import os
import pickle
import time
import random
import logging
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

from cli.commands.files import listfiles, uploadfiles, deletefiles, downloadfile, exportfiles
from cli.commands import mimetypes
from cli.commands.auth import login, logout
from cli.commands.account import me, storage

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def add_subparsers(subparsers):
    # Authentication
    login.setup(subparsers)
    logout.setup(subparsers)

    # Ailes
    listfiles.setup(subparsers)
    uploadfiles.setup(subparsers)
    deletefiles.setup(subparsers)
    downloadfile.setup(subparsers)
    exportfiles.setup(subparsers)

    # Mimetypes list
    mimetypes.setup(subparsers)

    # Account
    me.setup(subparsers)
    storage.setup(subparsers)

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print('Follow https://github.com/rishabh-j-23/gdrive-cli/blob/main/README.md on how to create credentials.json file!')
                return
                
            flow = InstalledAppFlow.from_client_secrets_file(
                './credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    parser = argparse.ArgumentParser(description="Google Drive CLI")
    subparsers = parser.add_subparsers(title='Commands', dest='subcommand')

    # Commands setup
    add_subparsers(subparsers)


    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
