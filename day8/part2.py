width = 25
height = 6
area = width * height

with open('input.txt') as f:
    image = list(f.readline()[:-1])

res = ['3' for x in range(area)]
while image:
    image, layer = image[:-area], image[-area:]
    for i in range(area):
        if layer[i] == '0' or layer[i] == '1':
            res[i] = layer[i]

for y in range(height):
    for x in range(width):
        print(res[width * y + x],end='')
    print()
