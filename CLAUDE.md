# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SamuraiCode multi-app portfolio website. Static HTML pages with embedded CSS, no build process or dependencies.

## Project Structure

- `index.html` - Homepage listing all apps with links to individual app pages
- `isitout/index.html` - IsItOut app landing page (movie release countdown tracker)
- `isitout/privacy-policy.html` - IsItOut privacy policy
- `images/` - App screenshots (referenced from app pages via `../images/`)
- No build process, dependencies, or server-side code

## Development Workflow

**Local Development:**
Use a simple HTTP server (needed for correct relative paths):
```bash
python3 -m http.server 8000
# Then visit http://localhost:8000
```

**Deployment:**
Hosted on GitHub Pages. Push to main to deploy:
```bash
git add .
git commit -m "Description of changes"
git push origin main
```

## Architecture Notes

**Self-contained HTML files:**
- All CSS is embedded in `<style>` tags within each HTML file
- No external stylesheets, JavaScript frameworks, or dependencies
- Fully responsive design with mobile breakpoints at 768px

**Design system:**
- Modern minimalist aesthetic with clean white background
- Typography: -apple-system, `text-wrap: balance` on headings, `text-wrap: pretty` on body
- Color palette: Black text (#1a1a1a), gray secondary (#666), light gray accents (#fafafa)
- Pill-shaped buttons with rounded corners (border-radius: 100px)
- Transitions: compositor props only (transform, opacity), 200ms max, ease-out

**Adding a new app:**
1. Create a new directory (e.g., `myapp/`)
2. Add `myapp/index.html` with the app's landing page
3. Add a new `.app-card` link in the root `index.html`

**External references:**
- Contact email: jeremy@samuraicode.com
- Company website: samuraicode.com
