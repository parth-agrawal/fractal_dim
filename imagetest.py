import matplotlib.pyplot as plt 
import matplotlib.patches as pat
import matplotlib.image as mpimg
import numpy as np 

img = mpimg.imread("C:/Users/parth/Dropbox/Projects/Coding/fractal_dim/britain.png")
# print(img)
fig, ax = plt.subplots(1)

plt.imshow(img) 

print(len(img))
print(img[0][0])

black_arr = []

for y in range(0, len(img)):
    for x in range(0, len(img[y])):
        for p in range(0, len(img[y][x])):
            pixel = img[y][x][p]
            if(np.all(pixel == 0)):
                black_arr.append(pixel)
        

print(black_arr)            

plt.show()



