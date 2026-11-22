"""Build original, self-contained dark liquid-glass SVG artwork; no dependencies."""
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
ASSETS.mkdir(exist_ok=True)

def save(name, body, width, height, title):
    (ASSETS / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{title}</title>{body}</svg>', encoding='utf-8')

save('banner.svg', '''
<defs>
 <linearGradient id="canvas" x2="1" y2="1"><stop stop-color="#10141e"/><stop offset=".55" stop-color="#080b12"/><stop offset="1" stop-color="#111125"/></linearGradient>
 <radialGradient id="aura"><stop stop-color="#6358ed" stop-opacity=".38"/><stop offset="1" stop-color="#6358ed" stop-opacity="0"/></radialGradient>
 <linearGradient id="liquid" x1=".1" y1="0" x2=".9" y2="1"><stop stop-color="#d2ffff" stop-opacity=".94"/><stop offset=".17" stop-color="#78d9ee" stop-opacity=".5"/><stop offset=".43" stop-color="#384a93" stop-opacity=".16"/><stop offset=".72" stop-color="#8d72f1" stop-opacity=".4"/><stop offset="1" stop-color="#dfd2ff" stop-opacity=".9"/></linearGradient>
 <linearGradient id="rim" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#ecffff" stop-opacity=".9"/><stop offset=".35" stop-color="#a1b9ff" stop-opacity=".1"/><stop offset=".7" stop-color="#b6a3ff" stop-opacity=".2"/><stop offset="1" stop-color="#e2dcff" stop-opacity=".9"/></linearGradient>
 <filter id="blur"><feGaussianBlur stdDeviation="18"/></filter>
 <filter id="soft"><feGaussianBlur stdDeviation="4"/></filter>
 <clipPath id="bounds"><rect x="1" y="1" width="1198" height="438" rx="26"/></clipPath>
</defs>
<style>
 .float { animation: float 10s ease-in-out infinite; transform-origin: 920px 217px; }
 .breathe { animation: breathe 8s ease-in-out infinite; }
 @keyframes float { 0%,100% { transform:translateY(0) rotate(-3deg); } 50% { transform:translateY(-10px) rotate(3deg); } }
 @keyframes breathe { 0%,100% { opacity:.55; } 50% { opacity:1; } }
 @media (prefers-reduced-motion:reduce) { .float,.breathe { animation:none; } }
</style>
<g clip-path="url(#bounds)">
 <rect width="1200" height="440" fill="url(#canvas)"/>
 <ellipse class="breathe" cx="955" cy="237" rx="340" ry="260" fill="url(#aura)"/>
 <path d="M590 440 Q950 80 1200 150M630 440 Q970 100 1200 195" stroke="#96a7dc" stroke-opacity=".07" fill="none"/>
 <ellipse cx="929" cy="362" rx="125" ry="18" fill="#000" opacity=".45" filter="url(#blur)"/>
 <g class="float">
  <path d="M874 81 C941 52 1038 95 1066 167 C1095 239 1039 309 969 339 C905 367 813 333 793 269 C771 202 802 114 874 81Z" fill="url(#liquid)" stroke="url(#rim)" stroke-width="1.5"/>
  <path d="M901 117 C950 95 1016 126 1035 177 C1055 226 1012 280 965 302 C915 324 852 297 834 250 C814 199 847 142 901 117Z" fill="#090d1d" fill-opacity=".8" stroke="url(#rim)" stroke-opacity=".6"/>
  <path d="M874 81 C805 120 781 214 807 274" fill="none" stroke="#b9ffff" stroke-opacity=".6" stroke-width="4" filter="url(#soft)"/>
  <path d="M876 88 C836 108 807 151 801 191" fill="none" stroke="#e1ffff" stroke-opacity=".88" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M996 322 Q1050 297 1065 243" fill="none" stroke="#e4d3ff" stroke-opacity=".8" stroke-width="2" stroke-linecap="round"/>
  <ellipse cx="937" cy="213" rx="188" ry="54" transform="rotate(-28 937 213)" fill="none" stroke="#a2b5de" stroke-opacity=".18"/>
  <circle cx="1099" cy="139" r="4" fill="#a8e3ed"/>
  <circle cx="790" cy="292" r="2.5" fill="#ad9cec"/>
 </g>
 <g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Arial,sans-serif">
  <rect x="54" y="49" width="173" height="29" rx="14.5" fill="#a9b9df" fill-opacity=".04" stroke="#b5c4e2" stroke-opacity=".16"/>
  <circle cx="71" cy="63" r="3" fill="#a0d8d2"/>
  <text x="84" y="67" font-size="10" letter-spacing="1.8" fill="#b5c7d9">ENGINEERING STUDENT</text>
  <text x="50" y="184" font-size="79" letter-spacing="-4" font-weight="650" fill="#f2f4fa">Diyan Patel<tspan fill="#9b9de9">.</tspan></text>
  <text x="55" y="236" font-size="24" letter-spacing="-.4" fill="#c4cad9">Building things that move.</text>
  <text x="55" y="271" font-size="24" letter-spacing="-.4" fill="#7e899f">And the systems behind them.</text>
  <path d="M55 318H625" stroke="#b8c6e0" stroke-opacity=".12"/>
  <text x="55" y="353" font-size="11" letter-spacing="2" fill="#97a5bd">EMBEDDED SYSTEMS</text>
  <circle cx="214" cy="349" r="1.5" fill="#67748b"/>
  <text x="233" y="353" font-size="11" letter-spacing="2" fill="#97a5bd">ROBOTICS</text>
  <circle cx="330" cy="349" r="1.5" fill="#67748b"/>
  <text x="349" y="353" font-size="11" letter-spacing="2" fill="#97a5bd">COMPUTER VISION</text>
  <text x="55" y="407" font-size="10" letter-spacing="1.3" fill="#626f86">AHMEDABAD UNIVERSITY</text>
  <text x="1145" y="407" text-anchor="end" font-size="10" letter-spacing="1.3" fill="#626f86">HARDWARE / SOFTWARE / CURIOSITY</text>
 </g>
</g>
<rect x="1" y="1" width="1198" height="438" rx="26" fill="none" stroke="#c9d4f3" stroke-opacity=".14"/>
''',1200,440,'Diyan Patel. Building things that move, and the systems behind them. Engineering student at Ahmedabad University.')

body='''<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#10151f"/><stop offset="1" stop-color="#090d15"/></linearGradient></defs>
<rect x="1" y="1" width="1198" height="166" rx="18" fill="url(#bg)" stroke="#252d3c"/>
<path d="M401 30V138M801 30V138" stroke="#222b3a"/>
<g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Arial,sans-serif">'''
for x,num,title,subtitle,color in [(30,'01','Close to the hardware','Firmware / interfaces / real-time systems','#b6d8e9'),(430,'02','Thinking in motion','Robotics / control / autonomy','#c3b9ec'),(830,'03','Making sense of pixels','Computer vision / Python / OpenCV','#acd6ce')]:
    body+=f'<text x="{x}" y="40" font-size="11" letter-spacing="2" fill="{color}">{num} / FOCUS</text><text x="{x}" y="88" font-size="23" letter-spacing="-.6" fill="#e1e6f0">{title}</text><text x="{x}" y="121" font-size="13" fill="#8592a8">{subtitle}</text>'
save('focus.svg',body+'</g>',1200,168,'Three areas of focus: embedded systems, robotics and computer vision.')

save('footer.svg','''<defs><linearGradient id="bg"><stop stop-color="#111622"/><stop offset="1" stop-color="#0d101b"/></linearGradient></defs>
<rect x="1" y="1" width="1198" height="94" rx="18" fill="url(#bg)" stroke="#262e40"/>
<g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Arial,sans-serif">
<text x="30" y="42" font-size="19" fill="#dce3f2" letter-spacing="-.4">A little curiosity. A lot of building.</text>
<text x="30" y="66" font-size="12" fill="#7f8da5">Explore the code behind the ideas.</text>
<rect x="982" y="27" width="187" height="42" rx="21" fill="#b5b9f1" fill-opacity=".08" stroke="#aab4ee" stroke-opacity=".25"/>
<text x="1003" y="53" font-size="13" fill="#c7cef3">Explore repositories</text><path d="M1143 49h8m-4-4 4 4-4 4" stroke="#c7cef3" fill="none"/>
</g>''',1200,96,'Explore Diyan Patel’s repositories.')
print('Built dark liquid-glass hero, focus strip and footer; no external assets or fonts.')

# Narrow-screen art keeps labels legible rather than shrinking desktop typography.
mobile = (ASSETS / 'banner.svg').read_text(encoding='utf-8')
mobile = mobile.replace('width="1200" height="440" viewBox="0 0 1200 440"', 'width="600" height="600" viewBox="0 0 600 600"')
mobile = mobile.replace('width="1198" height="438"', 'width="598" height="598"')
mobile = mobile.replace('width="1200" height="440"', 'width="600" height="600"')
mobile = mobile.replace('cx="955" cy="237"', 'cx="510" cy="140"')
mobile = mobile.replace('<g class="float">', '<g transform="translate(-140 -25) scale(.67)"><g class="float">')
mobile = mobile.replace(' <g font-family=', ' </g><g font-family=', 1)
start = mobile.index(' <rect x="54"')
end = mobile.index('</g>\n</g>\n<rect', start)
mobile = mobile[:start] + '''
 <rect x="34" y="35" width="173" height="29" rx="14.5" fill="#a9b9df" fill-opacity=".04" stroke="#b5c4e2" stroke-opacity=".16"/>
 <circle cx="51" cy="49" r="3" fill="#a0d8d2"/>
 <text x="64" y="53" font-size="10" letter-spacing="1.8" fill="#b5c7d9">ENGINEERING STUDENT</text>
 <text x="30" y="286" font-size="68" letter-spacing="-3" font-weight="650" fill="#f2f4fa">Diyan Patel<tspan fill="#9b9de9">.</tspan></text>
 <text x="34" y="340" font-size="27" fill="#c4cad9">Building things that move.</text>
 <text x="34" y="380" font-size="27" fill="#7e899f">And the systems behind them.</text>
 <path d="M34 424H566" stroke="#b8c6e0" stroke-opacity=".12"/>
 <text x="34" y="468" font-size="15" letter-spacing="2" fill="#97a5bd">EMBEDDED SYSTEMS / ROBOTICS</text>
 <text x="34" y="499" font-size="15" letter-spacing="2" fill="#97a5bd">COMPUTER VISION</text>
 <text x="34" y="564" font-size="12" letter-spacing="1.3" fill="#7e8ca4">AHMEDABAD UNIVERSITY</text>
''' + mobile[end:]
(ASSETS / 'banner-mobile.svg').write_text('\n'.join(line.rstrip() for line in mobile.splitlines()) + '\n', encoding='utf-8')
body='<rect x="1" y="1" width="598" height="418" rx="18" fill="#0b1019" stroke="#252d3c"/><g font-family="Segoe UI,Arial,sans-serif">'
for y,num,title,subtitle in [(36,'01','Close to the hardware','Firmware / interfaces / real-time systems'),(176,'02','Thinking in motion','Robotics / control / autonomy'),(316,'03','Making sense of pixels','Computer vision / Python / OpenCV')]:
    if y > 36:
        body += f'<path d="M28 {y-22}H572" stroke="#222b3a"/>'
    body += f'<text x="28" y="{y}" font-size="12" letter-spacing="2" fill="#b6c2df">{num} / FOCUS</text><text x="28" y="{y+38}" font-size="27" fill="#e1e6f0">{title}</text><text x="28" y="{y+70}" font-size="17" fill="#8592a8">{subtitle}</text>'
save('focus-mobile.svg',body+'</g>',600,420,'Embedded systems, robotics and computer vision.')
save('footer-mobile.svg','''<rect x="1" y="1" width="598" height="170" rx="18" fill="#0e131e" stroke="#262e40"/>
<g font-family="Segoe UI,Arial,sans-serif"><text x="28" y="44" font-size="25" fill="#dce3f2">A little curiosity. A lot of building.</text>
<text x="28" y="76" font-size="18" fill="#8998ae">Explore the code behind the ideas.</text>
<rect x="28" y="102" width="246" height="44" rx="22" fill="#b5b9f1" fill-opacity=".08" stroke="#aab4ee" stroke-opacity=".25"/>
<text x="48" y="130" font-size="18" fill="#c7cef3">Explore repositories</text><path d="M245 123h9m-4-4 4 4-4 4" stroke="#c7cef3" fill="none"/></g>''',600,172,'Explore Diyan Patel’s repositories.')
