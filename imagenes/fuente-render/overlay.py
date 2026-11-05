from PIL import Image, ImageDraw, ImageFont
F="/root/.claude/skills/synced/2ecf417f-8b50-4e03-9575-ed416e8c89f8_ab5812a9-31af-4999-9053-b2d27f075c59/canvas-design/canvas-fonts/"
im=Image.open("render.png").convert("RGB"); W,H=im.size
ov=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
# soft top gradient for legibility
for y in range(0,560):
    a=int(150*(1-y/560)**1.4); d.line([(0,y),(W,y)],fill=(6,10,22,a))
for y in range(H-150,H):
    a=int(170*((y-(H-150))/150)); d.line([(0,y),(W,y)],fill=(6,10,22,a))
im=Image.alpha_composite(im.convert("RGBA"),ov); d=ImageDraw.Draw(im)
CREAM=(243,239,230); M=72
mono=ImageFont.truetype(F+"DMMono-Regular.ttf",22); serif=ImageFont.truetype(F+"InstrumentSerif-Regular.ttf",76)
d.text((M,M),"OCHIN KRASO",font=mono,fill=CREAM)
d.text((W-M,M),"COMERCIO AGÉNTICO",font=mono,fill=CREAM,anchor="ra")
d.line([(M,M+40),(W-M,M+40)],fill=CREAM+(160,),width=1)
lines=["¿Quién responde cuando","el agente al que dimos permiso","para comprar se equivoca?"]
y=M+90
for ln in lines:
    assert d.textlength(ln,font=serif)<W-2*M, ln
    d.text((M,y),ln,font=serif,fill=CREAM); y+=86
small=ImageFont.truetype(F+"DMMono-Regular.ttf",18)
d.text((M,H-M+18),"Escena ficticia. Imagen generada por ordenador (render 3D).",font=small,fill=CREAM,anchor="ls")
d.text((W-M,H-M+18),"ochinkraso",font=small,fill=CREAM,anchor="rs")
im.convert("RGB").save("/home/user/MSillaFranco/imagenes/2026-11-05-comercio-agentico-realista.png",quality=95)
print(y)
