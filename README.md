# Text to Image
Encodes text to image (and decodes too)

## Encode
```py
import encoder

encoder.encode(
    text,            # str
    size=(640,640),  # (width,height)
    save_as=None,    # str (path)
    with_alpha=True, # bool
    over_image=None  # str (path)
)                  # returns PIL.Image.Image
```

## Decode
```py
import decoder

text = decoder.decode(
    filename_or_PIL_Image, # str (path) or PIL.Image.Image ()
    with_alpha=True,       # bool
)                        # returns str
```
