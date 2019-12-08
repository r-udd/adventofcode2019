from collections import Counter
width = 25
height = 6
area = width * height

with open('input.txt') as f:
    image = list(f.readline()[:-1])

fewest = area
res = -1
while image:
    layer, image = image[:area], image[area:]
    c = Counter(layer)
    if c['0'] < fewest:
        res = c['1'] * c['2']
        fewest = c['0']
print(res)