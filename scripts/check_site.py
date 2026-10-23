#!/usr/bin/env python3
"""Check generated local links, fragments, images, page metadata and structure."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set(); self.duplicate_ids=[]; self.h1=0; self.title=False; self.description=False; self.errors=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1':self.h1+=1
        if tag=='title':self.title=True
        if tag=='meta' and a.get('name')=='description':self.description=bool(a.get('content'))
        if 'id' in a:
            if a['id'] in self.ids:self.duplicate_ids.append(a['id'])
            self.ids.add(a['id'])
        if tag=='img' and 'alt' not in a:self.errors.append('Image missing alt attribute')
        for key in ['href','src']:
            if key in a:self.links.append(a[key])

def check(root=None):
    root=(root or ROOT/'dist').resolve(); parsed={}; errors=[]; count=0
    for path in root.rglob('*.html'):
        data=Page();data.feed(path.read_text());parsed[path.resolve()]=data
        for e in data.errors:errors.append(f'{path.relative_to(root)}: {e}')
        if data.h1!=1:errors.append(f'{path.name}: expected one H1; got {data.h1}')
        if not data.title or not data.description:errors.append(f'{path.name}: missing title/description')
        if data.duplicate_ids:errors.append(f'{path.name}: duplicate ids {data.duplicate_ids}')
    for path,data in parsed.items():
        for ref in data.links:
            count+=1; parts=urlsplit(ref)
            if parts.scheme in ('https','mailto','tel'):continue
            if parts.scheme:errors.append(f'{path.name}: unsupported URL scheme {ref}');continue
            if not ref:errors.append(f'{path.name}: empty link');continue
            target=(root/unquote(parts.path.lstrip('/'))) if parts.path.startswith('/') else ((path.parent/unquote(parts.path)).resolve() if parts.path else path)
            if target.is_dir():target=target/'index.html'
            if not target.exists():errors.append(f'{path.relative_to(root)} → missing {ref}')
            if parts.fragment and target in parsed and unquote(parts.fragment) not in parsed[target].ids:errors.append(f'{path.name}: missing fragment {ref}')
    if not parsed:errors.append('No HTML pages found')
    return {'pages':len(parsed),'references_checked':count,'errors':errors}
if __name__=='__main__':
    result=check();print(json.dumps(result,indent=2));sys.exit(bool(result['errors']))
