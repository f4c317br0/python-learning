import random
from PIL import Image

img = Image.open("winter.png")
pixels = img.load()
x, y = img.size

gray_pixels = []
for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        if r == g == b and 50 <= r <= 200:
            gray_pixels.append((i, j))

count = int(len(gray_pixels) * 0.3)
selected = random.sample(gray_pixels, count)

for (i, j) in selected:
    pixels[i, j] = (34, 139, 34)

img.save('spring.png')
