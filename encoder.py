from PIL import Image
from PIL import ImageColor
import os

def encode(text,
           size=(640,640),
           save_as=None,
           with_alpha=True,
           over_image=None,):
    def stbl(text,
             length,
             fill=None,
             prefix="",
             return_filled=False):
        if text != "":
            n = -1
            l = [prefix]
            for i in text:
                n += 1
                if n == length:
                    l += [prefix+i]
                    n = 0
                else:
                    l[-1] += i
            total_length = length+len(prefix)
            if return_filled:
                filled = 0
            if fill != None:
                if len(l[-1]) < total_length:
                    if return_filled:
                        f = total_length-len(l[-1])
                        filled = f
                        l[-1] += fill*f
                    else:
                        l[-1] += fill*(total_length-len(l[-1]))
            if return_filled:
                return (l,filled)
            return l
        else:
            if return_filled:
                return ([],0)
            return []

    def fillStart(text,symbol,length):
        return symbol*(length-len(text))+text

    textHex = text.encode("windows-1251").hex()
    colors,filled = stbl(textHex,8 if with_alpha else 6,"0","#",True)
    if len(colors) > size[0]*size[1]-1:
        raise ValueError("length of text is too long")

    finished_colors = ["#"+fillStart(hex(len(textHex))[2:],"0",8 if with_alpha else 6)]+colors

    if over_image:
        img = Image.open(over_image)
        size = img.size
    else:
        img = Image.new('RGBA'if with_alpha else'RGB',size)

    pixels = img.load()

    close = False

    i = 0
    for x in range(size[0]):
        for y in range(size[1]):
            pixels[x,y] = ImageColor.getcolor(finished_colors[i],
                                  "RGBA"if with_alpha else "RGB")
            i += 1
            if i == len(finished_colors):
                close = True
                break
        if close:
            break

    if save_as != None:
        img.save(save_as)
    return img
