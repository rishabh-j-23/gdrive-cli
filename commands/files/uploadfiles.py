from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

import pickle
import argparse
import os

from cli.colors import Colors
from cli.authenticate import authenticate


def setup(subparsers):
    parser = subparsers.add_parser(
        'upload', help='Upload file to Google Drive')
    parser.add_argument('-p', '--path', help='Path of the file to upload')
    parser.add_argument('-n', '--name', help='Name of the file to upload')
    parser.add_argument(
        '--parentid', help='ID of the parent folder in Google Drive', default=None)
    parser.set_defaults(func=upload_file)


def upload_file(args):
    service = build("drive", "v3", credentials=authenticate())
    file_path = args.path
    file_name = args.name
    parent_id = args.parentid
    file_metadata = {'name': file_name}
    if parent_id:
        file_metadata['parents'] = [parent_id]

    media = MediaFileUpload(file_path, resumable=True)

    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()
    print(Colors.GREEN + 'File ID: ', file.get('id'), " File Name: ",
          file.get('name', "NA"), " Uploaded Successfully!!" + Colors.RESET)
