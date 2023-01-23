import numpy as np
import os
import random
from PIL import Image, ImageOps


def concat_images(image_paths, size, shape=None):
    # Open images and resize them
    width, height = size
    images = map(Image.open, image_paths)
    images = [ImageOps.fit(image, size, Image.ANTIALIAS) for image in images]

    # Create canvas for the final image with total size
    shape = shape if shape else (1, len(images))
    image_size = (width * shape[1], height * shape[0])
    image = Image.new('RGB', image_size)

    # Paste images into final image
    for row in range(shape[0]):
        for col in range(shape[1]):
            offset = width * col, height * row
            idx = row * shape[1] + col
            image.paste(images[idx], offset)

    return image


def download(map,col,row):
  filename = "tiles/{}-{}-{}.png".format(map,col,row)
  if not exists(filename):
    url = "https://owsproxy.lgl-bw.de/owsproxy/ows/WMTS_LGL-BW_ALKIS_Basis?layer=ALKIS_{}&style=default&tilematrixset=ADV_25832_Quad&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image%2Fpng&TileMatrix=ADV_25832_Quad%3A12&TileCol={}&TileRow={}&user=ZentrKomp&password=viewerprod".format(map,col,row)
    return wget.download(url, filename)


images = []

#rows = range(3360, 3380)
#cols = range(1632, 1650)
#quality = 12

rows = range(26940, 26975)
cols = range(13115, 13150)
quality = 15


for row in rows:
  for col in cols:
    filename = "merged/{}/{}-{}.png".format(quality, col,row)
    images.append(filename)

print(images)

image = concat_images(images, (256, 256),(len(rows),len(cols)))
image.save('image.png', 'PNG')


