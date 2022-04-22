from PIL import Image
from PIL import ImageColor
import os

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

size = (640,640)

def start():
    t = input("Text > ")
    h = t.encode("windows-1251").hex()
    c,f = stbl(h,8,"0","#",True)
    if len(c) > size[0]*size[1]:
        return start()
    return t,h,c,f

text,textHex,colors,filled = start()

finished_colors = ["#"+fillStart(hex(len(textHex))[2:],"0",8)]+colors

img = Image.new('RGBA',size)

pixels = img.load()

close = False

i = 0
for x in range(size[0]):
    for y in range(size[1]):
        pixels[x,y] = ImageColor.getcolor(finished_colors[i],"RGBA")
        i += 1
        if i == len(finished_colors):
            close = True
            break
    if close:
        break

img.save("image.png")

os.system('explorer /select,"image.png"')
