from cli.colors import Colors
from cli.mimetypes import mime_types

def setup(subparsers):
    parser = subparsers.add_parser('mimetypes', help='List mimetypes supported by Google Drive')
    parser.add_argument('-q', '--query', help="Search specific mimetype", default=None)
    parser.set_defaults(func=mimetype)

def mimetype(args):
    print_table(mime_types, args.query)
    
def print_table(types, query):
    max_mimeType_length = len("application/vnd.openxmlformats-officedocument.presentationml.presentation")
    print(f"{Colors.GREEN}{'Mimetype'.ljust(max_mimeType_length)}  {'Extension'}{Colors.RESET}")
    
    if query:
        for k, v in mime_types.items():
            if (query in k or query in v):
                print(f"{v.ljust(max_mimeType_length)}  {k}")
    else:
        for k, v in mime_types.items():
            print(f"{v.ljust(max_mimeType_length)}  {k}")