#!/bin/python
import json
from PIL import Image

f = open("../scanner/nauvis.json", "r").read()
d = json.loads(f)

xmin = 999999999
xmax = -999999999
ymin = 999999999
ymax = -999999999

for t in d["water"]:
    x, y = t
    xmin = min(xmin, x)
    ymin = min(ymin, y)
    xmax = max(xmax, x)
    ymax = max(ymax, y)

w = abs(xmin - xmax)
h = abs(ymin - ymax)

print(xmin, ymin)
print(xmax, ymax)
print(w, h)

im = Image.new("RGB", (w+1, h+1), "#003000")

pixels = im.load()

for t in d["water"]:
    x, y = t
    x -= xmin
    y -= ymin
    pixels[x, y] = (34, 138, 215)


for t in d["resources"]["stone"]:
    x, y, a = t
    x -= xmin
    y -= ymin
    pixels[x, y] = (105, 82, 49)

for t in d["resources"]["iron-ore"]:
    x, y, a = t
    x -= xmin
    y -= ymin
    pixels[x, y] = (61, 91, 114)

for t in d["resources"]["copper-ore"]:
    x, y, a = t
    x -= xmin
    y -= ymin
    pixels[x, y] = (138, 63, 33)

for t in d["resources"]["crude-oil"]:
    x, y, a = t
    x -= xmin
    y -= ymin
    pixels[x, y] = (0, 0, 18)

for t in d["resources"]["coal"]:
    x, y, a = t
    x -= xmin
    y -= ymin
    pixels[x, y] = (28, 24, 29)

im.save("out.png")
