import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from datetime import datetime
import pickle

from cli.colors import Colors
from cli.authenticate import authenticate
from cli.mimetypes import mime_types

import json

SCOPES = ['https://www.googleapis.com/auth/drive']

def setup(subparsers):
    parser = subparsers.add_parser('storage', help='List storage available in Google Drive')
    parser.set_defaults(func=storage)

def storage(args):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = authenticate()
    else:
        print("User not logged in")
        return

    service = build('drive', 'v3', credentials=creds)

    results = service.about().get(fields="*").execute()
    storage = results['storageQuota']
    max_upload_size = results['maxUploadSize']
    
    print("+-------------------------------------------------------------------------------------------------------")
    for key, value in storage.items():
        mb = convert_to_mb(value)
        gb = convert_to_gb(value)
        print(f"{Colors.GREEN}{key.ljust(18).capitalize()}-> {Colors.BRIGHT_CYAN}{str(value).ljust(12)}B | {str(mb).ljust(6)}MB | {gb}GB{Colors.RESET}")

    # print(f"{Colors.GREEN}{'MaxUploadSize'.ljust(18)}-> {Colors.BRIGHT_CYAN}{str(max_upload_size).ljust(12)}B | {str(convert_to_mb(max_upload_size)).ljust(6)}MB | {convert_to_gb(max_upload_size)}GB{Colors.RESET}")
    print("+-------------------------------------------------------------------------------------------------------")

def convert_to_mb(val):
    return (int(val)//(1024*1024))

def convert_to_gb(val):
    return convert_to_mb(int(val))//1024
