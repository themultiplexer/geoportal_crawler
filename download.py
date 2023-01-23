import wget
try:
    from PIL import Image
except ImportError:
    import Image
from os.path import exists

def download(map,col,row,qual):
  filename = "tiles/{}/{}-{}-{}.png".format(qual,map,col,row)
  if not exists(filename):
    url = "https://owsproxy.lgl-bw.de/owsproxy/ows/WMTS_LGL-BW_ALKIS_Basis?layer=ALKIS_{}&style=default&tilematrixset=ADV_25832_Quad&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image/png&TileMatrix=ADV_25832_Quad:{}&TileCol={}&TileRow={}&user=ZentrKomp&password=viewerprod".format(map,qual,col,row)
    #print(url)
    return wget.download(url, filename)
  return filename

#rows = range(3360, 3380)
#cols = range(1632, 1650)
#quality = 12

rows = range(26940, 26975)
cols = range(13115, 13150)
quality = 15

for row in rows:
  for col in cols:

    print(row - rows[0])
    print("C:", col - cols[0])
    print("")
    a = download("Basis",col, row, quality)
    b = download("Beschriftung",col, row, quality)

    merged_name = "merged/{}/{}-{}.png".format(quality, col,row)

    if not exists(merged_name):
      background = Image.open(a)
      overlay = Image.open(b)


      background.paste(overlay, (0, 0), overlay)
      background.save(merged_name, "PNG")
