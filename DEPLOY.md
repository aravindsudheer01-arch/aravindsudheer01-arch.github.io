# Deploy and update the live portfolio

Live site: https://aravindsudheer01-arch.github.io/

Source: https://github.com/aravindsudheer01-arch/aravindsudheer01-arch.github.io

The GitHub Pages workflow (`.github/workflows/deploy.yml`) builds the project on a push to `main` and publishes the generated `dist/` folder.

## Making a change

1. Edit source files in `content/`, `templates/` or `assets/`.
2. Run `python -m unittest discover -s tests -v`, `python build.py`, and `python scripts/check_site.py`.
3. Commit and push to `main`.
4. Check GitHub Actions → **Build and deploy portfolio** for a successful run.
5. Open the live site and check Projects, Experience, About, contact links and the mobile menu.

The navigation intentionally has **no CV page**, and the repository no longer publishes its old CV PDFs. Contact information remains visible in the footer.

Project images are configured via `image` and `gallery` in each `content/projects/*.md` file. Set `demo_url` to link to an authorized externally hosted project video. Do not upload private footage, confidential employer information or access credentials.

The `review/` directory contains historical reports from the original release and should not be treated as verification of the latest site.

Troubleshooting: inspect the failed workflow step; missing images and invalid YAML are build errors, while missing local links are flagged by `scripts/check_site.py`. If the live site seems unchanged despite a successful run, try a hard refresh.

Official documentation: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
