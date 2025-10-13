# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

IsItOut is a static marketing website for a movie release countdown tracker iOS app. The site consists of two standalone HTML files with embedded CSS and minimal JavaScript.

## Project Structure

- `index.html` - Main landing page featuring app description, features, and App Store download link
- `privacy-policy.html` - Privacy policy page detailing data handling practices
- `images/` - App screenshots used in the landing page
- No build process, dependencies, or server-side code

## Development Workflow

**Local Development:**
Simply open the HTML files in a browser:
```bash
open index.html
```

Or use a simple HTTP server:
```bash
python3 -m http.server 8000
# Then visit http://localhost:8000
```

**Deployment:**
This appears to be hosted on GitHub Pages at `https://jeremy.github.io/isitout/`. To deploy changes:
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
- Typography: -apple-system with tight letter-spacing (-0.01em to -0.03em)
- Color palette: Black text (#1a1a1a), gray secondary (#666), light gray accents (#fafafa)
- Pill-shaped buttons with rounded corners (border-radius: 100px)
- Subtle shadows and spacing for visual hierarchy
- Feature grid using CSS Grid with `repeat(auto-fit, minmax(280px, 1fr))`

**Screenshots:**
- Real app screenshots located in `images/` directory
- Three main screens: watchlist, search, and upcoming movies
- Styled with rounded corners (24px) and shadow effects
- Responsive sizing: 270px desktop, 220px mobile

**External references:**
- Contact email: jeremy@samuraicode.com
- Company website: samuraicode.com
- Movie data source: The Movie Database (TMDB) API (mentioned in privacy policy)
- App Store URL: https://apps.apple.com/us/app/isitout/id6752792124?uo=4
