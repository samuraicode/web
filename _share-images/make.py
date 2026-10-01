#!/usr/bin/env python3
"""Render the 1200x630 share images in images/og-*.png, and apple-touch-icon.png,
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

# slug, name, icon emoji, headline (the page's h1), screenshot
APPS = [
    ('isitout', 'IsItOut', '🎬', 'Never Miss Another Movie Release', 'images/screenshot-watchlist.png'),
    ('scoreitquick', 'ScoreItQuickly', '🏆', 'The Fastest Way to Keep Score', 'images/scoreitquick/screenshot-1.png'),
    ('fakenews', 'FakeNews', '📰', 'Star in Your Own Breaking News', 'images/fakenews/screenshot-1.png'),
    ('toomanyzombies', 'Too Many Zombies', '🧟', 'Every Roll Could Be Your Last', 'images/toomanyzombies/screenshot-1.png'),
]


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
    render(fill('touch-icon.html'), os.path.join(ROOT, 'apple-touch-icon.png'), tmp, size='180,180')

    icons = '\n'.join(f'            <span class="icon">{emoji}</span>' for _, _, emoji, _, _ in APPS)
    render(fill('home.html', root=ROOT, icons=icons), os.path.join(ROOT, 'images/og-home.png'), tmp)

    for slug, name, emoji, headline, shot in APPS:
        html = fill('app.html', root=ROOT, slug=slug, name=name, emoji=emoji, headline=headline, shot=shot)
        render(html, os.path.join(ROOT, f'images/og-{slug}.png'), tmp)
