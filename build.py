#!/usr/bin/env python3
"""Build the portfolio locally. No network access, Node or backend required.

Content is trusted owner-authored Markdown; YAML uses safe_load, HTML is escaped.
"""
from __future__ import annotations
import argparse
import html
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import unicodedata
from urllib.parse import urlparse
from xml.sax.saxutils import escape
import jinja2
from markupsafe import Markup
import mistune
import yaml

ROOT = Path(__file__).resolve().parent
CATEGORIES = {'all':'All work','software':'Python & AI','data':'Data & SQL','engineering':'Robotics & hardware','vision':'Computer vision'}
REQUIRED = ('slug','title','summary','category','kind','period','role','tools','order','image','image_alt','image_caption')

def slugify(value: str) -> str:
    value = unicodedata.normalize('NFKD', value).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',value).strip('-') or 'section'

class Renderer(mistune.HTMLRenderer):
    def __init__(self):
        super().__init__(escape=True)
        self.headings=[]; self.ids=set()
    def heading(self,text,level,**attrs):
        plain=html.unescape(re.sub('<[^>]+>','',text)); original=slugify(plain); anchor=original; i=1
        while anchor in self.ids:
            i+=1; anchor=f'{original}-{i}'
        self.ids.add(anchor)
        if level==2:self.headings.append({'id':anchor,'text':plain})
        return f'<h{level} id="{anchor}">{text}</h{level}>\n'


def safe_asset(value: str) -> Path:
    if not isinstance(value,str) or not value.startswith('assets/'):
        raise ValueError(f'Asset must be under assets/: {value!r}')
    path=(ROOT/value).resolve()
    if not path.is_relative_to((ROOT/'assets').resolve()) or not path.is_file():
        raise ValueError(f'Missing or unsafe asset: {value}')
    return path


def load_project(path: Path) -> dict:
    text=path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):raise ValueError(f'{path.name}: missing YAML front matter')
    parts=text.split('---\n',2)
    if len(parts)!=3:raise ValueError(f'{path.name}: unclosed front matter')
    meta=yaml.safe_load(parts[1])
    if not isinstance(meta,dict):raise ValueError(f'{path.name}: front matter must be a mapping')
    if meta.get('draft',False):return {}
    for key in REQUIRED:
        if key not in meta:raise ValueError(f'{path.name}: missing {key}')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',str(meta['slug'])):raise ValueError(f'{path.name}: invalid slug')
    if meta['category'] not in CATEGORIES or meta['category']=='all':raise ValueError(f'{path.name}: invalid category')
    if not isinstance(meta['tools'],list) or not all(isinstance(t,str) for t in meta['tools']):raise ValueError(f'{path.name}: tools must be a list of strings')
    if not isinstance(meta['order'],int):raise ValueError(f'{path.name}: order must be an integer')
    safe_asset(meta['image'])
    for image in meta.get('gallery',[]):
        safe_asset(image['src'])
        if not image.get('alt'):raise ValueError('Gallery images need alt text')
    for value in [meta.get('repository'),meta.get('demo_url')]+[s.get('url') for s in meta.get('sources',[])]:
        if value and (urlparse(value).scheme!='https' or not urlparse(value).netloc):raise ValueError(f'{path.name}: external links must be HTTPS')
    renderer=Renderer();md=mistune.create_markdown(renderer=renderer,plugins=['table','strikethrough'])
    meta['body']=md(parts[2]);meta['headings']=renderer.headings
    meta['category_label']=CATEGORIES[meta['category']]
    meta.setdefault('repository','');meta.setdefault('demo_url','');meta.setdefault('gallery',[]);meta.setdefault('sources',[])
    return meta


def load_projects() -> list[dict]:
    projects=[p for path in sorted((ROOT/'content/projects').glob('*.md')) if (p:=load_project(path))]
    slugs=[p['slug'] for p in projects]
    if len(slugs)!=len(set(slugs)):raise ValueError('Duplicate project slug')
    return sorted(projects,key=lambda p:(p['order'],p['slug']))


def build(destination: Path | None=None) -> Path:
    destination=(destination or ROOT/'dist').resolve()
    # Never replace the project source, home, or an arbitrary existing directory.
    if destination != (ROOT/'dist').resolve():
        raise ValueError('Build destination is fixed to the project dist/ directory')
    projects=load_projects()
    profile=json.loads((ROOT/'content/profile.json').read_text())
    profile['site_url'] = os.environ.get('PORTFOLIO_SITE_URL', profile.get('site_url','')).rstrip('/')
    for cv in profile['cv']:
        if cv.get('file'):
            safe_asset('assets/cv/' + cv['file'])
    env=jinja2.Environment(loader=jinja2.FileSystemLoader(ROOT/'templates'),autoescape=jinja2.select_autoescape(['html']),undefined=jinja2.StrictUndefined)
    work=Path(tempfile.mkdtemp(prefix='.site-build-',dir=ROOT))
    routes=[]
    def render(template,route,title,description,active='',**extra):
        parent=Path(route).parent
        def url(path):return os.path.relpath(path,str(parent)).replace(os.sep,'/')
        canonical=profile['site_url'].rstrip('/')+'/'+route.replace('index.html','') if profile['site_url'] else ''
        text=env.get_template(template).render(profile=profile,projects=projects,categories=CATEGORIES,title=title,description=description,active=active,url=url,canonical=canonical,is_404=(route=='404.html'),**extra)
        file=work/route;file.parent.mkdir(parents=True,exist_ok=True);file.write_text(text,encoding='utf-8');routes.append(route)
    try:
        shutil.copytree(ROOT/'assets',work/'assets')
        render('home.html','index.html',profile['name'],profile['intro'],featured=[p for p in projects if p.get('featured')])
        render('projects.html','projects/index.html','Selected work','Python applications, SQL analytics, computer vision, robotics and academic engineering case studies.','work')
        for i,p in enumerate(projects):render('project.html',f"projects/{p['slug']}/index.html",p['title'],p['summary'],'work',project=p,next_project=projects[(i+1)%len(projects)])
        for template,route,title,description,active in [
            ('experience.html','experience/index.html','Experience','Professional ABB robotics and industrial automation experience.','experience'),
            ('about.html','about/index.html','About','Engineering background, education and technical skills.','about'),
            ('resume.html','resume/index.html','CV & professional links','Download role-specific CVs with GitHub links.','resume'),
            ('privacy.html','privacy/index.html','Privacy & credits','Privacy practices, project evidence and visual credits.',''),
            ('404.html','404.html','Page not found','This page could not be found.','')]:render(template,route,title,description,active)
        (work/'.nojekyll').write_text('')
        robots='User-agent: *\nAllow: /\n'
        if profile['site_url']:
            site_url=profile['site_url'].rstrip('/')
            if urlparse(site_url).scheme!='https':raise ValueError('site_url must be HTTPS')
            urls=''.join(f'<url><loc>{escape(site_url+"/"+route.replace("index.html",""))}</loc></url>' for route in routes if route!='404.html')
            (work/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+'</urlset>')
            robots+='Sitemap: '+site_url+'/sitemap.xml\n'
        (work/'robots.txt').write_text(robots)
        (work/'build-manifest.json').write_text(json.dumps({'pages':routes,'projects':len(projects),'content_reviewed':profile['updated']},indent=2))
        if destination.exists():shutil.rmtree(destination)
        work.rename(destination)
    except Exception:
        shutil.rmtree(work,ignore_errors=True);raise
    print(f'Built {len(routes)} pages / {len(projects)} case studies → {destination}')
    return destination

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.parse_args()
    try:build()
    except (ValueError,KeyError,jinja2.TemplateError,yaml.YAMLError) as error:raise SystemExit(f'Build error: {error}') from None
