"""Rebuild original vector artwork and local typing animation (requires Pillow)."""
import math
from pathlib import Path
import sys
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).parent))
from refresh_cards import ASSETS, card, txt, write

body = '''<defs>
<linearGradient id="bg" x2="1" y2="1"><stop stop-color="#080e20"/><stop offset="1" stop-color="#161b39"/></linearGradient>
<linearGradient id="accent"><stop stop-color="#65e6ef"/><stop offset=".5" stop-color="#4d8dff"/><stop offset="1" stop-color="#b298ff"/></linearGradient>
<radialGradient id="halo"><stop stop-color="#4d8dff" stop-opacity=".2"/><stop offset="1" stop-color="#4d8dff" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#819eea" stroke-opacity=".07"/></pattern>
</defs>
<rect width="1280" height="420" rx="22" fill="url(#bg)"/>
<rect width="1280" height="420" rx="22" fill="url(#grid)"/>
<ellipse cx="1000" cy="210" rx="300" ry="260" fill="url(#halo)"/>
<path d="M42 0H1238" stroke="url(#accent)" stroke-width="5"/>
<g fill="none" stroke="#65e6ef" opacity=".25" stroke-width="1.5">
<path d="M790 85h60l35 35h70M775 330h90l40-40h50M1130 100h65v70h85M1130 290h70v50h80"/>
<path d="M780 180h92M765 222h107M1140 208h140M1035 80V20M1035 330v90"/>
</g>
<g transform="translate(1005 207)">
<circle r="130" fill="none" stroke="#9c87ff" stroke-opacity=".35" stroke-dasharray="3 12"/>
<circle r="110" fill="none" stroke="#4d8dff" stroke-opacity=".5"/>
<path d="M-110 0a110 110 0 0 1 110-110M110 0a110 110 0 0 1-110 110" fill="none" stroke="#65e6ef" stroke-width="3"/>
<rect x="-65" y="-65" width="130" height="130" rx="13" fill="#0c152b" stroke="url(#accent)" stroke-width="2"/>
<rect x="-49" y="-49" width="98" height="98" rx="8" fill="#101d37" stroke="#293d60"/>
<g stroke="#7498ca" stroke-width="3">'''
for i in range(-42,43,14):
    body += f'<path d="M{i} -80v15M{i} 65v15M-80 {i}h15M65 {i}h15"/>'
body += '</g><text x="0" y="14" text-anchor="middle" font-family="Consolas,monospace" font-size="42" font-weight="700" fill="#e8f5ff">DP</text></g>'
body += '<g font-family="Segoe UI,Arial,sans-serif">'
body += txt(60,75,'ELECTRICAL & ELECTRONICS / ENGINEERING',16,'#65e6ef',600)
body += txt(56,177,'DIYAN PATEL',76,'#f1f6ff',700)
body += '<rect x="60" y="203" width="84" height="4" rx="2" fill="url(#accent)"/>'
body += txt(60,257,'Electronics. Firmware. Software.',28,'#c1cce2')
body += txt(60,301,'Embedded systems / Robotics / Autonomous vehicles',18,'#8f9fbe')
body += txt(60,377,'AHMEDABAD UNIVERSITY',13,'#8194b5',600)
body += '</g>'
write('banner.svg','<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="420" viewBox="0 0 1280 420">'+body+'</svg>')

for name,num,title,sub,color in [
    ('embedded','01','STM32 Embedded Platform','AUTONOMOUS VEHICLES / FIRMWARE','#65e6ef'),
    ('vision','02','Facial Recognition Attendance','ENR106 / COMPUTER VISION','#b2a3ff')]:
    body = f'<rect x="1" y="26" width="3" height="95" rx="1" fill="{color}"/>'
    body += txt(26,37,sub,12,color,600)+txt(26,86,title,29,'#edf4ff',600)
    body += txt(26,120,'VIEW REPOSITORY  →',12,'#91a8cb',600)
    body += txt(812,97,num,58,'#243451',600)
    write('project-'+name+'.svg',card(920,148,body))

# Compact local badges with distinct language/interface symbols.
for slug,label,icon,color in [
    ('c','C','C','#65e6ef'),('python','Python','Py','#b2a3ff'),
    ('stm32','STM32','µ','#65e6ef'),('freertos','FreeRTOS','RT','#65e6ef'),
    ('cubeide','STM32CubeIDE','▣','#65e6ef'),('opencv','OpenCV','CV','#b2a3ff'),
    ('tkinter','Tkinter','Tk','#b2a3ff')]:
    width = 63+len(label)*8
    body = f'<rect width="{width}" height="32" rx="6" fill="#101a2e" stroke="#293c58"/><rect x="1" y="1" width="35" height="30" rx="5" fill="#1d2c46"/>'
    body += txt(8,21,icon,13,color,600)+txt(45,21,label,13,'#d7e6fa',600)
    write('badge-'+slug+'.svg',f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="32" viewBox="0 0 {width} 32"><g font-family="Segoe UI,Arial,sans-serif">{body}</g></svg>')
write('footer.svg',card(920,75,'<path d="M30 1h860" stroke="#667ed1"/>'+txt(26,44,'DIYAN PATEL',14,'#65e6ef',600)+txt(513,44,'ELECTRONICS · FIRMWARE · SOFTWARE',13,'#92a4c6')))

font_path = Path('C:/Windows/Fonts/consola.ttf')
roles = ['Electrical & Electronics Engineering student','Embedded systems developer','Exploring robotics and autonomy']
font_size = 23
font = ImageFont.truetype(str(font_path),font_size)
while max(font.getlength('> '+role+' _') for role in roles) > 704:
    font_size -= 1
    font = ImageFont.truetype(str(font_path),font_size)
first=Image.new('RGB',(760,64),'#0b1224')
ImageDraw.Draw(first).text((28,17),'> '+roles[0]+' _',font=font,fill='#65e6ef')
frames=[first.copy() for _ in range(16)]
for line in roles:
    for n in range(len(line)+1):
        im=Image.new('RGB',(760,64),'#0b1224'); d=ImageDraw.Draw(im)
        text='> '+line[:n]+' _'
        d.text((28,17),text,font=font,fill='#65e6ef')
        frames.append(im)
    frames.extend([im.copy() for _ in range(22)])
frames[0].save(ASSETS/'engineering-roles.gif',save_all=True,append_images=frames[1:],duration=85,loop=0,optimize=True)
print('Original banner, project cards, badges, footer and typing animation built.')
