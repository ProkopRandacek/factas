#!/bin/python
import json

f = open("../scanner/nauvis.json", "r").read()
d = json.loads(f)

print(d["water"])

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

print(xmin, ymin)
print(xmax, ymax)

