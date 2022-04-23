from PIL import Image

def decode(filename_or_PIL_Image,with_alpha=True):
    if type(filename_or_PIL_Image) != Image.Image:
        filename = filename_or_PIL_Image
        img = Image.open(filename)
    else:
        img = filename_or_PIL_Image

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
            c = to_hex(pixels[x,y])
            hex += c
            i += len(c)
            if i >= count:
                close = True
                break
        if close:
            break
    hex = hex[:count]

    return bytes.fromhex(hex).decode('windows-1251')

if __name__ == '__main__':
    decode("image.png",False)
