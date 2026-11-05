from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
F="/root/.claude/skills/synced/2ecf417f-8b50-4e03-9575-ed416e8c89f8_ab5812a9-31af-4999-9053-b2d27f075c59/canvas-design/canvas-fonts/"
sans=lambda s:ImageFont.truetype(F+"InstrumentSans-Regular.ttf",s)
sansb=lambda s:ImageFont.truetype(F+"InstrumentSans-Bold.ttf",s)
mono=lambda s:ImageFont.truetype(F+"DMMono-Regular.ttf",s)
# laptop screen 1600x1000
im=Image.new("RGB",(1600,1000),(246,247,249)); d=ImageDraw.Draw(im)
d.rectangle([0,0,1600,90],fill=(22,33,56)); d.text((60,28),"Agente de compras",font=sansb(34),fill=(240,240,240))
d.text((1540,32),"Pedido n.º 48213",font=mono(26),fill=(200,205,215),anchor="ra")
d.ellipse([60,150,130,220],fill=(46,140,90)); d.line([(78,186),(92,200),(114,170)],fill="white",width=8)
d.text((160,150),"Pedido confirmado",font=sansb(56),fill=(22,33,56))
d.text((160,222),"Compra realizada automáticamente en tu nombre",font=sans(30),fill=(90,100,115))
y=320
rows=[("Sillas de oficina ergonómicas","x 40","11.960,00 €"),("Envío urgente","","180,00 €"),("Instalación","","0,00 €")]
d.line([(60,y-20),(1540,y-20)],fill=(220,223,228),width=2)
for a,b,c in rows:
    d.text((60,y),a,font=sans(34),fill=(30,40,60)); d.text((1000,y),b,font=sans(34),fill=(30,40,60)); d.text((1540,y),c,font=sans(34),fill=(30,40,60),anchor="ra"); y+=70
d.line([(60,y),(1540,y)],fill=(220,223,228),width=2); y+=30
d.text((60,y),"Total cargado",font=sansb(40),fill=(22,33,56)); d.text((1540,y),"12.140,00 €",font=sansb(40),fill=(22,33,56),anchor="ra"); y+=100
d.rectangle([60,y,1540,y+150],fill=(253,240,236),outline=(196,62,38),width=3)
d.text((90,y+25),"Solicitud original: 4 sillas",font=sansb(34),fill=(160,45,25))
d.text((90,y+80),"Aprobado por: —",font=sans(32),fill=(160,45,25))
im.save("tex/screen.png")
# document 1240x1754 (A4)
im=Image.new("RGB",(1240,1754),(250,248,243)); d=ImageDraw.Draw(im)
d.text((110,140),"MANDATO DE COMPRA",font=mono(40),fill=(30,35,50))
d.text((110,210),"Autorización para agente de IA",font=sans(46),fill=(30,35,50))
d.line([(110,300),(1130,300)],fill=(60,60,70),width=3)
items=[("Límite por operación","500 €"),("Proveedores","Solo homologados"),("Plazo","Noviembre 2026"),("Confirmación humana","A partir de 300 €"),("Registro","Obligatorio")]
y=360
for a,b in items:
    d.text((110,y),a,font=sans(36),fill=(50,55,70)); d.text((1130,y),b,font=sans(36),fill=(50,55,70),anchor="ra"); y+=80
for i in range(9):
    yy=y+40+i*48; w=random.randint(700,1020); d.line([(110,yy),(110+w,yy)],fill=(175,175,180),width=6)
y=y+520
d.text((110,y),"Responsable:",font=sans(36),fill=(50,55,70)); d.line([(380,y+42),(1130,y+42)],fill=(60,60,70),width=3)
d.text((110,y+130),"Firma:",font=sans(36),fill=(50,55,70)); d.line([(270,y+172),(1130,y+172)],fill=(196,62,38),width=4)
im.save("tex/document.png")
# city bokeh window
random.seed(3); im=Image.new("RGB",(2000,1200),(8,14,30)); d=ImageDraw.Draw(im,"RGBA")
for _ in range(700):
    x=random.randint(0,2000); yv=random.randint(350,1200); r=random.randint(3,9)
    c=random.choice([(255,190,110),(255,220,160),(170,200,255),(255,240,220)])
    d.ellipse([x-r,yv-r,x+r,yv+r],fill=c+(random.randint(90,220),))
for _ in range(40):
    x=random.randint(0,2000); w=random.randint(60,200); h=random.randint(300,800)
    d.rectangle([x,1200-h,x+w,1200],fill=(14,22,44,200))
im=im.filter(ImageFilter.GaussianBlur(10)); im.save("tex/city.png")
print("ok")
