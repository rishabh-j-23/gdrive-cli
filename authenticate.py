from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import os
import pickle

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
GLOBAL_DIRECTORY = os.path.expanduser('~/.gdrive-cli')
CREDENTIALS_PATH = os.path.join(GLOBAL_DIRECTORY, 'credentials.json')
TOKEN_PATH = os.path.join(GLOBAL_DIRECTORY, 'token.pickle')

def create_global_directory():
    if not os.path.exists(GLOBAL_DIRECTORY):
        os.makedirs(GLOBAL_DIRECTORY)
        print(f"Created global directory: {GLOBAL_DIRECTORY}")

def authenticate():
    create_global_directory()

    creds = None
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_PATH, 'wb') as token:
            pickle.dump(creds, token)
    return creds
