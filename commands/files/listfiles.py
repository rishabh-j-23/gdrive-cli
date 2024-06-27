import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from datetime import datetime
import pickle

from cli.colors import Colors
from cli.authenticate import authenticate
from mimetypes_dict import mime_types

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
CREDENTIALS_PATH = 'credentials.json'


def setup(subparsers):
    parser = subparsers.add_parser('list', help='List files from Google Drive')
    parser.add_argument('-ps', '--pagesize', type=int,
                        help='Number of files per page', default=10)
    parser.add_argument(
        '-S', '--show-type', help='show which mimetype to show (use "gdrive mimetype" to see all mimetype)')
    parser.set_defaults(func=list_files)


def list_files(args, pageSize=10):
    creds = None
    pageSize = args.pagesize
    show_type = args.show_type
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    service = build("drive", "v3", credentials=authenticate())

    results = service.files().list(
        pageSize=pageSize, fields="nextPageToken, files(id, name, modifiedTime, mimeType, size)").execute()
    items = results.get('files', [])

    if not items:
        print(Colors.RED + 'No files found.' + Colors.RESET)
    else:
        print_table(items, show_type)


def print_table(data, show_type):
    # Find the maximum length of id and name
    max_id_length = max(len(row['id']) for row in data)
    max_name_length = max(len(row['name']) for row in data)
    max_date_length = max(len(row['modifiedTime']) for row in data)
    max_mimeType_length = max(len(row['mimeType']) for row in data)
    # max_size_length = max(len(str(row['size'])) for row in data)

    print(f"{Colors.GREEN}{'Name'.ljust(max_name_length)}  {'Type'.ljust(max_mimeType_length)}  {'Modified Time'.ljust(max_date_length)}  {'id'.ljust(max_id_length)}  {'Size'.ljust(14)}{Colors.RESET}")
    # Print the data with padding
    for row in data:
        # Convert ISO 8601 timestamp to datetime object
        datetime_obj = datetime.fromisoformat(row['modifiedTime'][:-1])
        # Format the datetime object as a readable string
        time = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

        if show_type:
            if row['mimeType'] == mime_types.get(show_type):
                if "size" not in row:
                    row['size'] = "None"
                print(f"{row['name'].ljust(max_name_length)}  {row['mimeType'].ljust(max_mimeType_length)}  {time.ljust(max_date_length)}  {row['id'].ljust(max_id_length)}  {row['size'].ljust(14)}  ")

        else:
            if "size" not in row:
                row['size'] = "None"
            print(f"{row['name'].ljust(max_name_length)}  {row['mimeType'].ljust(max_mimeType_length)}  {time.ljust(max_date_length)}  {row['id'].ljust(max_id_length)}  {row['size'].ljust(14)}  ")
