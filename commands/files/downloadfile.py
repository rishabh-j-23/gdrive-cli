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
    parser = subparsers.add_parser(
        'download', help='Download file from Google Drive')
    parser.add_argument('-id', '--id', help='ID of the file to download')
    parser.add_argument('destination', help='Destination of downloaded file', default="/")
    parser.add_argument('-n', '--name', help='Save file with name (give proper extension eg. example.zip, exmaple.txt, etc)', default='',)
    parser.set_defaults(func=download_file)

def download_file(args):
    service = build("drive", "v3", credentials=authenticate())

    file_id = args.id
    destination = args.destination
    name = args.name

    try:
        request = service.files().get_media(fileId=file_id)

        file = service.files().get(fileId=file_id).execute()
        original_file_name = file['name']

        if not name:
            name = original_file_name

        # generate proper path
        relative_path = os.path.join(destination, name)
        absolute_path = os.path.join(os.getcwd(), relative_path)

        # Ensure that the directory exists
        os.makedirs(os.path.dirname(absolute_path), exist_ok=True)

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))

        # Save the downloaded file to disk
        with open(absolute_path, 'wb') as f:
            f.write(fh.getvalue())

        print(Colors.GREEN, "Downloaded Successfully!!", Colors.RESET, "Saved to: ", absolute_path)
    except Exception as e:
        print(e)
