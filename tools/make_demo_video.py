from PIL import Image, ImageDraw, ImageFont
import os
F='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
segs=[("Was ist eine Zelle?",["Kleinste Einheit des Lebens","Prokaryoten: kein Zellkern (Bakterien)","Eukaryoten: mit Zellkern (Pflanze, Tier, Pilz)"],'cell'),
("Der Zellkern",["Enthält die DNA – die Bauanleitung","Kernhülle: Doppelmembran","mRNA verlässt den Kern durch Kernporen"],'nuc'),
("Energie: Mitochondrien",["Zellatmung liefert ATP","Glucose + O₂ → CO₂ + H₂O","Eigene DNA → Endosymbiontentheorie"],'mito')]
W,H=640,360; n=0
for si,(t,bul,pic) in enumerate(segs):
  for k in range(3):
    im=Image.new('RGB',(W,H),'#f7f8fb'); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,46],fill='#1f2f8c'); d.text((20,12),'Biologie 1 · Die Zelle',font=ImageFont.truetype(F,18),fill='white')
    d.text((W-90,12),f'{si+1}/3',font=ImageFont.truetype(F,18),fill='white')
    d.text((24,62),t,font=ImageFont.truetype(FB,28),fill='#1f2f8c')
    for j in range(k+1):
      d.ellipse([28,122+j*48,38,132+j*48],fill='#d0302f'); d.text((50,114+j*48),bul[j],font=ImageFont.truetype(F,19),fill='#222')
    cx,cy=540,250
    if pic=='cell': d.ellipse([cx-70,cy-55,cx+70,cy+55],outline='#23763a',width=4); d.ellipse([cx-20,cy-20,cx+20,cy+20],fill='#9bb5e8')
    if pic=='nuc': d.ellipse([cx-60,cy-60,cx+60,cy+60],outline='#1f2f8c',width=6); d.ellipse([cx-52,cy-52,cx+52,cy+52],outline='#1f2f8c',width=2); [d.arc([cx-40,cy-30+i*15,cx+40,cy-10+i*15],0,180,fill='#d0302f',width=3) for i in range(4)]
    if pic=='mito': d.ellipse([cx-80,cy-40,cx+80,cy+40],outline='#d0302f',width=4); d.line([(cx-60,cy),(cx-40,cy-25),(cx-20,cy+25),(cx,cy-25),(cx+20,cy+25),(cx+40,cy-25),(cx+60,cy)],fill='#d0302f',width=3)
    for f in range(7 if k<2 else 6):
      im.save(f'f{n:03d}.png'); n+=1
print(n)
