#!/bin/python
import json
from PIL import Image

f = open("../scanner/nauvis.json", "r").read()
d = json.loads(f)

xmin, xmax, ymin, ymax = 999999999, -999999999, 999999999, -999999999

for t in d["water"]:
    x, y = t
    xmin = min(xmin, x)
    ymin = min(ymin, y)
    xmax = max(xmax, x)
    ymax = max(ymax, y)

w = abs(xmin - xmax)
h = abs(ymin - ymax)

im = Image.new("RGB", (w + 1, h + 1), "#003000")
pixels = im.load()

for t in d["water"]:
    x, y = t
    x -= xmin
    y -= ymin
    pixels[x, y] = (34, 138, 215)

colors = [(105, 82, 49), (61, 91, 114), (138, 63, 33), (0, 0, 18), (28, 24, 29)]

i = 0
for r in d["resources"].keys():
    for t in d["resources"][r]:
        x, y = t[0], t[1]
        x -= xmin
        y -= ymin
        pixels[x, y] = colors[i]
    i += 1

nearest = {}

for r in d["resources"].keys():
    nearest_x = 9999
    nearest_y = 9999
    nearest_d = 9999
    for t in d["resources"][r]:
        x, y, a = t
        dis_to_0 = abs(x) + abs(y)
        if dis_to_0 < nearest_d:
            nearest_x = x
            nearest_y = y
            nearest_d = dis_to_0
    nearest[r] = [nearest_x, nearest_y]

print(nearest)

for n in nearest.values():
    x, y = n[0], n[1]
    x -= xmin
    y -= ymin
    pixels[x, y] = (256, 0, 0)

im.save("out.png")

# Todo:
# Water can be between nearest ore patch and 0, 0

# Algorithm thig
# analyze base design blueprint book
# Place ore miners on patches
# One by one place building kina near eachother maybe backpack algorithm or something with graphs
