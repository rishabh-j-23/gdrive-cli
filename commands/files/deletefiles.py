from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import pickle
import argparse
import os

from cli.colors import Colors
from cli.authenticate import authenticate


def setup(subparsers):
    parser = subparsers.add_parser(
        'delete', help='Delete file from Google Drive')
    parser.add_argument('-id', '--id', help='ID of the file to delete')
    parser.set_defaults(func=delete_file)


def delete_file(args):
    service = build("drive", "v3", credentials=authenticate())
    id = args.id

    file = service.files().delete(fileId=id).execute()
    print(Colors.RED + "Deleted Successfully!!" + Colors.RESET)
