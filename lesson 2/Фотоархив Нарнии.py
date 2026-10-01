import os
from PIL import Image
import zipfile

source = 'narnia_photos'
output = 'narnia_thumbnails'
os.makedirs(output, exist_ok=True)

for el in os.listdir(source):
    if el.endswith('.png'):
        inpath = os.path.join(source, el)
        img = Image.open(inpath)

        width, height = img.size
        side = min(width, height)
        cropped = img.crop((0, 0, side, side))

        resized = cropped.resize((100, 100), Image.Resampling.LANCZOS)

        outpath = os.path.join(output, el)
        resized.save(outpath)

with zipfile.ZipFile('narnia_thumbnails.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    for filename in os.listdir(output):
        file_path = os.path.join(output, filename)
        zf.write(file_path, arcname=filename)
