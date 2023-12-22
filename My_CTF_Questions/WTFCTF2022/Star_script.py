import binascii
from PIL import Image
 
img = Image.open('starswtfctf.png')
pix = img.load()
 
i = 238
x = ""
while i <= 254:
  for h in range(img.size[1]):
    for w in range(img.size[0]):
      p = pix[w,h]
      if p[3] == i:
        j = 0
        for j in range(3):
          if p[j] == 1 or p[j] == 0:
            x = x + str(p[j])
  x = x + " "    
  i = i + 1
x = x.strip()
print(x)