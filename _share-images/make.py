#!/usr/bin/env python3
"""Render the 1200x630 share images in images/og-*.png, the 1000x1500 Pinterest
pins in images/pin-*.png, apple-touch-icon.png and the web app manifest icons,
with headless Chrome.

Run from anywhere: python3 _share-images/make.py
Set CHROME to use a Chrome binary other than the macOS default.
"""
import os
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CHROME = os.environ.get('CHROME', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')

# slug, name, headline (the page's h1), screenshot. Icons come from images/<slug>/icon.png.
APPS = [
    ('isitout', 'IsItOut', 'Never Miss Another Movie Release', 'images/screenshot-watchlist.png'),
    ('scoreitquick', 'ScoreItQuickly', 'The Fastest Way to Keep Score', 'images/scoreitquick/screenshot-1.png'),
    ('fakenews', 'FakeNews', 'Star in Your Own Breaking News', 'images/fakenews/screenshot-1.png'),
    ('toomanyzombies', 'Too Many Zombies', 'Every Roll Could Be Your Last', 'images/toomanyzombies/screenshot-1.png'),
    ('randomly', 'Randomly', "Reminders You'll Actually Notice", 'images/randomly/screenshot-1.png'),
]


def icon(slug):
    return (f'<img src="file://{ROOT}/images/{slug}/icon.png" alt="" '
            'style="width:100%;height:100%;border-radius:inherit;display:block">')


def fill(template, **values):
    html = open(os.path.join(HERE, template)).read()
    for key, value in values.items():
        html = html.replace('{{%s}}' % key, value)
    return html


def render(html, out, tmp, size='1200,630'):
    page = os.path.join(tmp, os.path.basename(out) + '.html')
    open(page, 'w').write(html)
    subprocess.run([CHROME, '--headless', '--disable-gpu', '--hide-scrollbars',
                    '--force-device-scale-factor=1', f'--window-size={size}',
                    f'--screenshot={out}', f'file://{page}'],
                   check=True, capture_output=True)
    print(os.path.relpath(out, ROOT))


with tempfile.TemporaryDirectory() as tmp:
    for name, size in [('apple-touch-icon.png', 180), ('icon-192.png', 192), ('icon-512.png', 512)]:
        render(fill('touch-icon.html', size=str(size)), os.path.join(ROOT, name), tmp, size=f'{size},{size}')

    icons = '\n'.join(f'            <span class="icon">{icon(slug)}</span>' for slug, _, _, _ in APPS)
    render(fill('home.html', root=ROOT, icons=icons), os.path.join(ROOT, 'images/og-home.png'), tmp)

    for slug, name, headline, shot in APPS:
        html = fill('app.html', root=ROOT, slug=slug, name=name, icon=icon(slug), headline=headline, shot=shot)
        render(html, os.path.join(ROOT, f'images/og-{slug}.png'), tmp)

        html = fill('pin.html', root=ROOT, slug=slug, name=name, icon=icon(slug), headline=headline, shot=shot)
        render(html, os.path.join(ROOT, f'images/pin-{slug}.png'), tmp, size='1000,1500')
