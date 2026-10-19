"""Render cards from unauthenticated public endpoints. No tokens or private API calls."""
import datetime as dt
import html
import json
from pathlib import Path
import re
import urllib.request

USER = 'diyan07-ctrl'
ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)
STAMP = dt.datetime.now(dt.timezone.utc).strftime('%d %b %Y')

def get(url):
    request = urllib.request.Request(url, headers={'User-Agent': USER + '-public-profile', 'Accept': 'application/vnd.github+json' if 'api.github.com' in url else 'text/html'})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read().decode()

def txt(x, y, text, size=16, color='#a8b8d1', weight=400):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}">{html.escape(str(text))}</text>'

def card(width, height, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect x="1" y="1" width="{width-2}" height="{height-2}" rx="16" fill="#0b1224" stroke="#243451"/><g font-family="Segoe UI,Arial,sans-serif">{body}</g></svg>'

def write(name, value):
    (ASSETS / name).write_text(value, encoding='utf-8')

def main():
    repos = []
    page = 1
    while True:
        batch = json.loads(get(f'https://api.github.com/users/{USER}/repos?per_page=100&page={page}'))
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    original = [r for r in repos if not r['fork'] and not r['private']]
    stars = sum(r['stargazers_count'] for r in original)
    body = txt(24, 33, 'PUBLIC / REPOSITORIES', 13, '#65e6ef', 600)
    for x, value, label in [(24,len(original),'Original repos'),(220,stars,'Stars received')]:
        body += txt(x, 96, value, 44, '#edf4ff', 600) + txt(x, 124, label, 14)
    body += txt(24, 166, 'Public originals only · ' + STAMP, 12, '#8294b3')
    stats = card(450, 190, body)
    languages = {}
    for repo in original:
        for lang, count in json.loads(get(repo['languages_url'])).items():
            languages[lang] = languages.get(lang, 0) + count
    total = sum(languages.values()) or 1
    items = sorted(languages.items(), key=lambda item: item[1], reverse=True)
    shown = items[:3]
    if len(items) > 3:
        shown.append(('Other',sum(n for _, n in items[3:])))
    colors = ['#65e6ef','#9c87ff','#4d8dff','#8494b2']
    body = txt(24,33,'LANGUAGES / BY CODE BYTES',13,'#b2a3ff',600)
    x = 24
    for (lang, count), color in zip(shown, colors):
        width = 402 * count / total
        body += f'<rect x="{x:.2f}" y="58" width="{width:.2f}" height="12" fill="{color}"/>'
        x += width
    for i, ((lang,count),color) in enumerate(zip(shown,colors)):
        x, y = 24+(i%2)*205, 105+(i//2)*26
        body += txt(x,y,f'{lang}  {count/total:.1%}',14,color)
    body += txt(24,166,'Public originals · includes library code',12,'#8294b3')
    langs = card(450,190,body)
    calendar = get(f'https://github.com/users/{USER}/contributions')
    counts = {}
    tips = {ident: re.sub('<[^>]+>', '', content) for ident,content in re.findall(r'<tool-tip\b[^>]*for="([^"]+)"[^>]*>(.*?)</tool-tip>',calendar,re.S)}
    for tag in re.findall(r'<td\b[^>]*data-date="[^"]+"[^>]*>',calendar):
        attrs = dict(re.findall(r'([\w-]+)="([^"]*)"',tag))
        tip = tips.get(attrs['id'], '')
        match = re.search(r'(\d+) contributions?',tip)
        if not match and not tip.startswith('No contributions'):
            raise ValueError('Unrecognized public calendar tooltip; retain existing cards')
        counts[dt.date.fromisoformat(attrs['data-date'])] = int(match.group(1)) if match else 0
    if len(counts) < 350:
        raise ValueError('Incomplete public contribution calendar')
    today = dt.datetime.now(dt.timezone.utc).date()
    counts = {d:n for d,n in counts.items() if d <= today}
    longest = run = 0
    for day in sorted(counts):
        run = run+1 if counts[day] else 0
        longest = max(longest,run)
    cursor = today if counts.get(today,0) else today-dt.timedelta(days=1)
    current = 0
    while counts.get(cursor,0):
        current += 1
        cursor -= dt.timedelta(days=1)
    body = txt(26,34,'ACTIVITY / PUBLIC CONTRIBUTION CALENDAR',13,'#65e6ef',600)
    body += txt(26,67,f'{sum(counts.values())} contributions',23,'#edf4ff',600)
    body += txt(510,66,f'Current streak  {current}d    /    Longest in window  {longest}d',14,'#b2a3ff')
    start = min(counts)
    start -= dt.timedelta(days=(start.weekday()+1)%7)
    palette = ['#18243b','#214957','#26778a','#36b6c9','#65e6ef']
    for day, count in sorted(counts.items()):
        week = (day-start).days//7
        row = (day.weekday()+1)%7
        level = 0 if count==0 else 1 if count<=2 else 2 if count<=5 else 3 if count<=9 else 4
        body += f'<rect x="{31+week*16}" y="{90+row*16}" width="12" height="12" rx="3" fill="{palette[level]}"><title>{day}: {count} contributions</title></rect>'
    body += txt(26,232,f'{min(counts)} — {max(counts)} · Updated {STAMP} · UTC',12,'#8294b3')
    activity = card(920,255,body)
    body = txt(24,33,'GITHUB / CONTRIBUTION STREAK',13,'#b2a3ff',600)
    for x, value, label in [(24,current,'Current streak'),(170,longest,'Longest streak'),(316,sum(counts.values()),'Contributions')]:
        body += txt(x,96,value,38,'#edf4ff',600)+txt(x,124,label,12)
    body += txt(24,166,'Last year · public calendar · UTC',12,'#8294b3')
    streak = card(450,190,body)
    ist = dt.datetime.now(dt.timezone(dt.timedelta(hours=5,minutes=30)))
    updated = card(360,32,txt(14,21,'Last updated: '+ist.strftime('%d %b %Y, %H:%M')+' IST',12,'#a8b8d1'))
    # Do not replace cards until all data sources and parsing succeed.
    for name,value in [('stats.svg',stats),('languages.svg',langs),('activity.svg',activity),('streak.svg',streak),('last-updated.svg',updated)]:
        write(name,value)
    print(f'Generated public cards: {len(original)} original repos, {sum(counts.values())} contributions; {STAMP}')

if __name__ == '__main__':
    main()
