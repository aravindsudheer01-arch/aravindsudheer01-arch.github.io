#!/usr/bin/env python3
"""Create a draft case study without touching templates or components."""
import argparse
from pathlib import Path
import sys
import yaml
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from build import ROOT, slugify, CATEGORIES

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('title');p.add_argument('--category',choices=[c for c in CATEGORIES if c!='all'],default='software')
    args=p.parse_args();slug=slugify(args.title);target=ROOT/'content/projects'/f'{slug}.md'
    if target.exists():raise SystemExit(f'Refusing to overwrite {target.name}')
    _,front,body=(ROOT/'content/project-template.md').read_text().split('---\n',2)
    data=yaml.safe_load(front);data.update(slug=slug,title=args.title,category=args.category)
    target.write_text('---\n'+yaml.safe_dump(data,sort_keys=False,allow_unicode=True)+'---\n'+body,encoding='utf-8')
    print(f'Created {target.relative_to(ROOT)} (draft: true). Edit it and set draft: false when ready.')
if __name__=='__main__':main()
