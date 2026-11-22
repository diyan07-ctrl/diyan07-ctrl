"""Build the profile's dark header artwork using Python's standard library."""
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / 'assets'

def header(mobile=False):
    width, height = (600, 220) if mobile else (1200, 232)
    x = 30 if mobile else 48
    name_y = 84 if mobile else 100
    size = 50 if mobile else 60
    background = f'''
<defs>
 <linearGradient id="background" x2="1" y2=".4"><stop stop-color="#121720"/><stop offset="1" stop-color="#0d1117"/></linearGradient>
 <linearGradient id="edge"><stop stop-color="#7e99b6" stop-opacity=".6"/><stop offset="1" stop-color="#7e99b6" stop-opacity="0"/></linearGradient>
</defs>
<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="14" fill="url(#background)" stroke="#29313c"/>
<path d="M{x} 1H{width-80}" stroke="url(#edge)"/>
'''
    if not mobile:
        background += '''<g stroke="#72849a" stroke-opacity=".17" fill="none" stroke-width="1.5">
<path d="M970 60h92v42h90M1018 60v92h102M970 174h42v-22"/>
<circle cx="970" cy="60" r="4"/><circle cx="1156" cy="102" r="4"/><circle cx="1124" cy="152" r="4"/><circle cx="966" cy="174" r="4"/>
</g>'''
    text = f'''<g font-family="Segoe UI,Arial,sans-serif">
<text x="{x}" y="{name_y}" font-size="{size}" font-weight="600" letter-spacing="-2" fill="#e6edf3">Diyan Patel</text>
<text x="{x}" y="{name_y+47}" font-size="{22 if mobile else 23}" fill="#a9b6c7">Electrical &amp; Electronics Engineering</text>
<text x="{x}" y="{name_y+81}" font-size="{19 if mobile else 17}" fill="#7d8b9e">Ahmedabad University</text>
</g>'''
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">Diyan Patel, Electrical and Electronics Engineering student at Ahmedabad University.</title>{background}{text}</svg>\n'

if __name__ == '__main__':
    ASSETS.mkdir(exist_ok=True)
    for mobile in (False, True):
        name = 'profile-header-mobile.svg' if mobile else 'profile-header.svg'
        (ASSETS / name).write_text(header(mobile), encoding='utf-8')
    print('Built desktop and mobile profile headers.')
