from PIL import Image

im = Image.open("enc.png")

width,height = im.size

# print(im.mode)
# print(im.size)

pixels = im.load()

key = 'eCGeIOSY'
k = []

for i in key:
    k.append(ord(i))

decrypted = Image.new(im.mode,im.size)
out = decrypted.load()

for i in range(0,256,2):
    for j in range(0,256,2):
        pixels[i,j] = (pixels[i,j] ^ k[4])
        pixels[i+1,j] = (pixels[i+1,j] ^ k[5])
        pixels[i,j+1] = pixels[i,j+1] ^ k[6]
        pixels[i+1,j+1] = pixels[i+1,j+1] ^ k[7]


# # # access pixel i,j by pixels[i,j]
for i in range(256):
    for j in range(256):
        xa = (k[0] + k[1]*i) % width
        ya = (k[2] + k[3]*j) % height
        out[i,j] = pixels[xa,ya]

# ans.save('ans.png')



decrypted.save("dec.png")
