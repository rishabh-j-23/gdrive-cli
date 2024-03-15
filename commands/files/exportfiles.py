from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload

import io
import pickle
import argparse
import os

from cli.colors import Colors
from cli.authenticate import authenticate


def setup(subparsers):
    parser = subparsers.add_parser('export', help='Export file from Google Drive')
    parser.add_argument('-id', '--id', help='ID of the file to export')
    parser.add_argument('destination', help='Destination of exported file', default="/")
    parser.add_argument('-n', '--name', help='Save file with name (give proper extension eg. example.zip, exmaple.txt, etc)', default='')
    parser.add_argument('-t', '--type', help='export file as (zip, exmaple.txt, etc)', default='')
    parser.set_defaults(func=export_file)


def export_file(args):
    service = build("drive", "v3", credentials=authenticate())

    file_id = args.id
    destination = args.destination
    name = args.name
    _type = args.type

    try:
        file_metadata = service.files().get(fileId=file_id).execute()
        original_file_name = file_metadata['name']

        if not name:
            name = original_file_name

        # Generate proper path
        absolute_path = os.path.join(destination, name)

        # Ensure that the directory exists
        os.makedirs(os.path.dirname(absolute_path), exist_ok=True)

        request = service.files().export_media(fileId=file_id, mimeType='application/pdf')

        with open(absolute_path + str(_type), 'wb') as f:
            downloader = MediaIoBaseDownload(f, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print("Download %d%%." % int(status.progress() * 100))

        print("Downloaded Successfully!! Saved to: ", destination)
    except Exception as e:
        print(e)
