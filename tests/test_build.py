import unittest
import tempfile
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from build import load_projects, load_project, safe_asset, slugify, Renderer
import mistune

class ContentTests(unittest.TestCase):
    def test_projects_have_unique_slugs(self):
        projects=load_projects();self.assertGreaterEqual(len(projects),10)
        self.assertEqual(len(projects),len({p['slug'] for p in projects}))
    def test_every_case_has_substantial_content(self):
        for p in load_projects():
            self.assertGreater(len(p['headings']),3)
            self.assertTrue(p['image_alt'])
            self.assertIn('Limitations',p['body']) if p['slug'] not in ('robotic-concrete-printing','warehouse-automation') else None
    def test_unsafe_asset_rejected(self):
        with self.assertRaises(ValueError):safe_asset('assets/../../etc/passwd')
    def test_missing_asset_rejected(self):
        with self.assertRaises(ValueError):safe_asset('assets/does-not-exist.png')
    def test_slug(self):self.assertEqual(slugify('Results & Evidence'),'results-evidence')
    def test_duplicate_heading_ids(self):
        r=Renderer();md=mistune.create_markdown(renderer=r)
        result=md('## Results\n\nText\n\n## Results\n')
        self.assertIn('id="results-2"',result)
    def test_raw_html_is_escaped(self):
        result=mistune.create_markdown(renderer=Renderer())('<script>alert(1)</script>')
        self.assertNotIn('<script>',result)
    def test_draft_is_not_published(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'draft.md';p.write_text('---\ndraft: true\n---\nPrivate notes')
            self.assertEqual(load_project(p),{})
    def test_missing_metadata_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'bad.md';p.write_text('---\ntitle: Test\n---\nText')
            with self.assertRaises(ValueError):load_project(p)
    def test_incomplete_front_matter_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'bad.md';p.write_text('No metadata')
            with self.assertRaises(ValueError):load_project(p)
    def test_projects_navigation_and_no_public_cv(self):
        from build import build
        site=build()
        home=(site/'index.html').read_text(encoding='utf-8')
        projects=(site/'projects/index.html').read_text(encoding='utf-8')
        self.assertIn('>Projects</a>', home)
        self.assertIn('>Experience</a>', home)
        self.assertNotIn('resume/index.html', home)
        self.assertFalse((site/'resume').exists())
        self.assertFalse((site/'assets/cv').exists())
        self.assertIn('All projects', projects)
if __name__=='__main__':unittest.main()
