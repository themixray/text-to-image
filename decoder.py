from PIL import Image

def decode(filename,with_alpha=True):
    if with_alpha:
        img = Image.open(filename)
    else:
        img = Image.open(filename)

    def to_hex(rgb):
        if with_alpha:
            return '%02x%02x%02x%02x' % rgb
        return '%02x%02x%02x' % rgb[0:3]

    def delete_from_start(text,symbol):
        t = ""
        for i in text:
            if i != symbol:
                t += i
        return t

    pixels = img.load()

    count = delete_from_start(to_hex(pixels[0,0])[1:],"0")
    if count == "": count = 0
    else: count = int(count,16)

    close = False
    hex = ""
    i = 0
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if (x,y) == (0,0):
                continue
            hex += to_hex(pixels[x,y])
            i += 1
            if i == count:
                close = True
                break
        if close:
            break

    return bytes.fromhex(hex).decode('windows-1251')
