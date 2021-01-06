from random import choice
import numpy as np
from PIL import Image

face_type = 2
face = True
color = get_rand_rgb()

def get_rand_color():
    return int(choice(range(0, 255)))


def get_rand_rgb():
    r = get_rand_color()
    g = get_rand_color()
    b = get_rand_color()
    return (r, g, b)


data = np.zeros((48, 64, 3), dtype=np.uint8)
data[0:8, 8:16] = get_rand_rgb()
data[0:8, 16:24] = get_rand_rgb()
data[8:16, 0:8] = get_rand_rgb()
data[8:16, 8:16] = get_rand_rgb()
data[8:16, 16:24] = get_rand_rgb()
data[8:16, 24:32] = get_rand_rgb()
data[16:20, 4:8] = get_rand_rgb()
data[16:20, 8:12] = get_rand_rgb()
data[16:20, 20:28] = get_rand_rgb()
data[16:20, 4:8] = get_rand_rgb()
data[16:20, 8:12] = get_rand_rgb()
data[16:20, 20:28] = get_rand_rgb()
data[16:20, 44:48] = get_rand_rgb()
data[16:20, 48:52] = get_rand_rgb()
data[16:20, 28:36] = get_rand_rgb()

data[32:36, 4:8] = get_rand_rgb()
data[32:36, 8:12] = get_rand_rgb()
data[32:36, 44:48] = get_rand_rgb()
data[32:36, 48:52] = get_rand_rgb()

i = 4
val1 = 20
val2 = 32
val3 = 0
val4 = 4
while(True):
    data[val1:val2, val3:val4] = get_rand_rgb()
    val3 = val3+4
    val4 = val4+4
    i = i-1
    if i == 0:
        break
val1 = 20
val2 = 32
val3 = 40
val4 = 44
i = 4
while(True):
    data[val1:val2, val3:val4] = get_rand_rgb()
    val3 = val3+4
    val4 = val4+4
    i = i-1
    if i == 0:
        break

i = 4
val1 = 36
val2 = 48
val3 = 0
val4 = 4
while(True):
    data[val1:val2, val3:val4] = get_rand_rgb()
    val3 = val3+4
    val4 = val4+4
    i = i-1
    if i == 0:
        break
val1 = 36
val2 = 48
val3 = 40
val4 = 44
i = 4
while(True):
    data[val1:val2, val3:val4] = get_rand_rgb()
    val3 = val3+4
    val4 = val4+4
    i = i-1
    if i == 0:
        break

data[20:32, 16:20] = get_rand_rgb()
data[20:32, 28:32] = get_rand_rgb()

data[20:32, 20:28] = get_rand_rgb()
data[20:32, 32:40] = get_rand_rgb()

data[11:12, 9:11] = (255, 255, 255)
data[11:12, 13:15] = (255, 255, 255)

data[11:12, 10:11] = color
data[11:12, 13:14] = color

if face == True:
    data[14:15, 11:13] = (255, 255, 255)
    if face_type == 2:
        data[13:14, 10:11] = (255, 255, 255)
        data[13:14, 13:14] = (255, 255, 255)
    else:
        data[14:15, 10:11] = (255, 255, 255)
        data[14:15, 13:14] = (255, 255, 255)

img = Image.fromarray(data, 'RGB')
img.save("skin_notr.png", "PNG")

img = Image.open('skin_notr.png')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        newData.append((0, 0, 0, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("skin_tr.png", "PNG")
