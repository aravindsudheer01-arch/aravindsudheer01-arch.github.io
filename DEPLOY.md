# Deploy to GitHub Pages

**Status:** the website is built locally, not published. No remote repository or Pages setting was changed by this delivery. The connected GitHub tools used for the audit did not expose repository creation or code-push actions.

## Recommended destination

Create a public repository named exactly:

```text
aravindsudheer01-arch.github.io
```

Once Pages deployment succeeds, GitHub should publish this user-site address:

```text
https://aravindsudheer01-arch.github.io/
```

That is the intended address, not a claim that it is already live. A custom domain can be connected later; do not buy one to unblock applications.

## One-time setup

1. Review `CONTENT_REVIEW.md`, the project wording, the contact details and the four public CV PDFs. No phone number is included publicly. Keep employer and client information private.
2. On GitHub, create the public repository named above. For the fresh-folder Git commands below, leave GitHub's README, .gitignore and licence initialization unchecked so the repository starts empty. If a repository with that name already exists, do not overwrite it; use its normal branch/review workflow instead.
3. Open the downloaded `aravind-portfolio` folder in VS Code. In Terminal, run:

```bash
cd /path/to/aravind-portfolio
git init
git branch -M main
git add .
git diff --cached --stat
git commit -m "Add engineering and software portfolio"
git remote add origin https://github.com/aravindsudheer01-arch/aravindsudheer01-arch.github.io.git
git push -u origin main
```

Use your normal GitHub authentication. Never paste credentials into code, the website or a chat. If Git asks for identity configuration, use the name and verified/noreply email appropriate to your GitHub account.

4. In that repository, open **Settings → Pages → Build and deployment → Source → GitHub Actions**.
5. Open the **Actions** tab, choose **Build and deploy portfolio**, and use **Run workflow** if the initial run happened before Pages was enabled. A new push to `main` also triggers it.
6. The workflow installs the small Python dependencies, runs content tests, builds static pages, checks local references, then deploys only `dist/`.
7. Use the deployment URL shown by GitHub. Check the homepage, one case study, mobile menu, contact links and all four PDF downloads. Only then add the live website URL to your CV and LinkedIn.

The included workflow uses the Pages metadata to set the production canonical URL and sitemap. Do not add a speculative site URL to CVs before this step succeeds.

## Updating after launch

```bash
# Edit content/projects/*.md, content/profile.json or assets first.
python build.py
python -m unittest discover -s tests -v
python scripts/check_site.py
git add content assets templates build.py serve.py scripts tests .github README.md DEPLOY.md CONTENT_REVIEW.md
git diff --cached --stat
git commit -m "Update portfolio content"
git push
```

The next workflow run rebuilds and deploys the site. You do not manually edit the generated HTML. `dist/` is intentionally gitignored.

## Common first-deployment problems

- **Workflow cannot configure Pages:** select GitHub Actions in Settings → Pages, then rerun. Confirm the repository is eligible for Pages and your account can manage it.
- **Actions are disabled:** enable Actions for this repository using your account settings. Review the supplied workflow before granting permissions.
- **Wrong repository name:** a user site requires `<username>.github.io`. A differently named repository is a project site with a path prefix. Relative site links support a path prefix, but verify the resulting Pages URL.
- **Missing .github directory:** macOS Finder hides dot-folders. The `git add .` command includes the workflow. Do not upload only the visible files using Finder.
- **Content build fails:** the error identifies missing metadata or an image. Correct the relevant Markdown file and rebuild.
- **PDF appears outdated:** replace the source PDF in `assets/cv/`, commit, deploy, then check the actual downloaded file.

## Alternative: already-built output

The `dist/` folder is the entire static website. It can be served on another static host without running Python on that host. Python is a build-time tool only. Do not upload the original project ZIP, old code archives, `.env`, private application records or credentials.

For manual hosting, set `site_url` in `content/profile.json` to the real HTTPS site URL and rebuild so canonical tags and the sitemap use the correct address.

## Official references

- Creating a Pages site: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- Custom Pages workflows: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

These were checked on 23 October 2026. GitHub's own deployment screen is the authority for the actual published address and build status.
