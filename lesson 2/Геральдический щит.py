import json
import math
from PIL import Image, ImageDraw

with open('coat_of_arms.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

img = Image.new('RGB', (800, 800), color=data['background'])
draw = ImageDraw.Draw(img)

draw.rectangle(
    [0, 0, img.width - 1, img.height - 1],
    outline=data['border']['color'],
    width=data['border']['width']
)

emblem = data['emblem']
x, y = emblem['position']

if emblem['shape'] == 'circle':
    radius = emblem['radius']
    xyxy = [x - radius, y - radius, x + radius, y + radius]
    draw.ellipse(xyxy, fill=emblem['color'])
else:  # square
    half = emblem['side'] / 2
    xyxy = [x - half, y - half, x + half, y + half]
    draw.rectangle(xyxy, fill=emblem['color'])

for el in data['symbols']:
    cx, cy = el['position']

    if el['shape'] == 'cross':
        s = el['size'] / 2
        t = el['size'] / 10

        points = [
            (cx - t, cy - s), (cx + t, cy - s),
            (cx + t, cy - t), (cx + s, cy - t),
            (cx + s, cy + t), (cx + t, cy + t),
            (cx + t, cy + s), (cx - t, cy + s),
            (cx - t, cy + t), (cx - s, cy + t),
            (cx - s, cy - t), (cx - t, cy - t),
        ]
        draw.polygon(points, fill=el['color'])

    elif el['shape'] == 'star':
        outer_radius = el['size'] / 2
        inner_radius = el['size'] / (5 * math.sqrt(2))

        points = []
        for i in range(8):
            angle = math.pi / 4 * i - math.pi / 2
            r = outer_radius if i % 2 == 0 else inner_radius
            px = cx + r * math.cos(angle)
            py = cy + r * math.sin(angle)
            points.append((px, py))
        draw.polygon(points, fill=el['color'])

img.save('narnia_shield.png')