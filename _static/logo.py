from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGBA',
                (840, 450),
                color = (255, 255, 255,0))

fnt = ImageFont.truetype('Le Havre Light.ttf',
                         500)
d = ImageDraw.Draw(img)
d.text((0,0),
       "le AB",
       font=fnt,
       fill=(0, 0, 0))

img.save('logo_le_ab.png')