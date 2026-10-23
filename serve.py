#!/usr/bin/env python3
"""Serve the prebuilt website locally using Python's standard library."""
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import argparse

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port',type=int,default=8000)
    args=parser.parse_args()
    root=Path(__file__).resolve().parent/'dist'
    if not (root/'index.html').is_file():raise SystemExit('Missing dist/index.html. Run python build.py first.')
    server=ThreadingHTTPServer(('127.0.0.1',args.port),partial(SimpleHTTPRequestHandler,directory=str(root)))
    print(f'Preview: http://127.0.0.1:{args.port} (Ctrl+C to stop)',flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()
if __name__=='__main__':main()
