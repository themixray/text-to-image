from PIL import Image

img = Image.open("image.png")

def rgba_to_hex(rgba):
    return '%02x%02x%02x%02x' % rgba

def delete_from_start(text,symbol):
    t = ""
    for i in text:
        if i != symbol:
            t += i
    return t

pixels = img.load()

count = delete_from_start(rgba_to_hex(pixels[0,0])[1:],"0")
if count == "": count = 0
else: count = int(count,16)

close = False
hex = ""
i = 0
for x in range(640):
    for y in range(640):
        if (x,y) == (0,0):
            continue
        hex += rgba_to_hex(pixels[x,y])
        i += 1
        if i == count:
            close = True
            break
    if close:
        break

print(bytes.fromhex(hex).decode('windows-1251'))
