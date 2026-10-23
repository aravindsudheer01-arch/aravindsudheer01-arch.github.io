# Aravind Sudheer — engineering / software portfolio

A static, content-driven portfolio connecting robotics and industrial automation with Python, applied AI, computer vision and SQL.

**First version:** 17 HTML pages, 10 case studies, four public CV PDFs, no backend, no Node build, no tracking or remote fonts. All diagrams are original explanatory SVGs, labelled as such. No project photographs or app screenshots are fabricated.

## Start here: preview the already-built site

The download includes `dist/`. Open **`dist/index.html`** in a browser, or run this in the website folder:

```bash
python3 serve.py
```

Then open `http://127.0.0.1:8000`. This preview uses the Python standard library only. Stop it with `Ctrl+C`.

The prebuilt version does not need pip, Node, a database, an API key or a network call. Copy-to-clipboard is shown only when the browser supports it in a secure context. Email links work independently.

## Edit and rebuild

Use your existing Python 3.10+ environment (the project was built with Python 3.13; GitHub Actions uses 3.12). On your Mac:

```bash
cd /path/to/aravind-portfolio
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python build.py
python -m unittest discover -s tests -v
python scripts/check_site.py
python serve.py
```

After editing a content file, run `python build.py` again and refresh the browser. There is intentionally no continuously running build/watch service. The generator writes only to `dist/`, validates required fields and assets, and refuses unsafe image paths. Draft case studies are not included in the built site.

Build dependencies are Jinja2, MarkupSafe, Mistune and PyYAML. No ML or webcam dependencies are installed by this website.

## Add a project

```bash
python scripts/new_project.py "A useful new project" --category software
```

1. Edit the new file in `content/projects/`.
2. Replace the template text with the problem, your contribution, approach, actual evidence and limitations.
3. Add images to `assets/images/`. Update `image`, `image_alt` and `image_caption` in the file.
4. Add a real `repository`, `demo_url` or `gallery` entry when available. Omit unavailable links; never use a fake live-demo URL.
5. Set `draft: false`. Run the build and link checker.

Categories: `software`, `data`, `engineering`, `vision`. `order` controls project order. `featured: true` includes a case study on the homepage; keep four featured projects for the current design. All case study pages and index cards are generated automatically. No component changes are needed.

**Important:** `draft: true` hides the item from the built website, not from a public GitHub source repository. Never put confidential information or credentials in draft content.

## Add photographs or demo links

Use images you own or have permission to publish. For ordinary photographs, aim for roughly 1,600 pixels on the long edge and an appropriately compressed JPEG/WebP. Do not resize an engineering diagram so small that its labels are unreadable. SVG diagrams may remain vector files.

Example front matter:

```yaml
gallery:
  - src: assets/images/solar-prototype.webp
    alt: My assembled solar-monitoring prototype during a permitted test
    caption: Prototype assembly; photograph shared with permission.
demo_url: https://your-actual-demo-or-video-url
```

There is no autoplay or external video embedding. A demo link opens the actual resource. A supplied screenshot should be labelled as a screenshot; an explanatory diagram should remain labelled as a diagram.

## Change contact details, skills or experience

Edit `content/profile.json`. It controls the public email, GitHub and LinkedIn links, education, skills, experience and CV labels. The public location is deliberately only **India**. No personal phone number appears in the site or its public CV downloads.

## Update a CV

Replace the relevant PDF in `assets/cv/`, preserving its name, or update `file` in `content/profile.json`. Editable Word versions are delivered separately in the CV bundle and are not copied into the site source. Add your phone number only to private application copies when appropriate.

Current PDFs:

- `Aravind_SW_AI_CV.pdf`
- `Aravind_DATA_CV.pdf`
- `Aravind_ML_CV.pdf`
- `Aravind_Engineering_CV.pdf`

All contain a clickable GitHub link. The software, data and ML/CV versions have targeted project updates matching the reviewed public repositories. The engineering version retains its engineering focus. Inspect the wording against your own contribution before publishing.

## Publish

Follow **[DEPLOY.md](DEPLOY.md)**. The repository includes a GitHub Pages workflow; you only need to create the repository, push the files and select GitHub Actions as the Pages publishing source.

Only `dist/` is deployed. It is also suitable for other static hosts. No paid hosting, custom domain or server process is required for the recommended GitHub Pages route.

## Structure

```text
content/
  profile.json           # Contact, experience, education, CV labels
  project-template.md    # Copyable case-study template
  projects/*.md          # Content and metadata, one file per case study
templates/               # Jinja HTML templates
assets/
  style.css              # Design system and responsive layouts
  site.js                # Filters, search, mobile menu, copy email
  images/                # Original SVG diagrams; add real project assets here
  cv/                    # Public CV PDFs
build.py                 # Static generator, no network access
serve.py                 # Standard-library local preview server
scripts/
  new_project.py         # Create a draft Markdown project
  check_site.py          # Link, asset and structure validation
tests/                   # Standard-library unittest content/build tests
.github/workflows/       # GitHub Pages build and deploy
review/                  # Audit and QA notes (not copied to dist/)
dist/                    # Ready-to-serve site; rebuildable and gitignored
```

## Evidence and ownership

Read **CONTENT_REVIEW.md** before publication. Engineering descriptions use the supplied CVs and prior project clarifications. Software pages link to their public repositories. Project descriptions do not claim commercial impact, trained models, real-driving validation or production deployment without evidence.

The code/templates and illustrative SVGs were created for this portfolio. No third-party font files, paid templates, stock photos, private datasets, course handouts or employer programs are bundled. Choose a licence deliberately if you decide to open-source the website implementation; no licence is imposed on your project content or CVs by this bundle.

## What this version intentionally does not include

No blog, CMS account, backend, authentication, job tracker, analytics dashboard, LLM chat widget, automated applications, invented testimonials or performance counters. These are not needed to start sending the portfolio with applications.

## Verification

See `review/TEST_REPORT.md` for the checks actually run and their limits. `python scripts/check_site.py` is an offline local-link checker, not a claim that all third-party URLs or external project applications are running.
