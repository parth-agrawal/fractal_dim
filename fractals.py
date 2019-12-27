import matplotlib.pyplot as plt 
import matplotlib.patches as pat
import matplotlib.image as mpimg
import numpy as np 


def test_hit(b_size):
    
    # This is because the range() function can't handle floats.
    # Set box size here and increase the min/max by the corresponding 1/b_size ratio.
    r_arr = []

    # Adds rectangles to an array and adds to plot 
    for i in range(0, len(img[0]), b_size) :
        for j in range(0, len(img), b_size) :
            xy = (i, j)
            rect = pat.Rectangle(xy, b_size, b_size, fill = False)
            r_arr.append(rect)

    


    x_values = []
    y_values = []

    
    # determine which pixels are black
    for y in range(0, len(img)):
        for x in range(0, len(img[y])):
            
            pixel = img[y][x]
            if(np.all(pixel) == 0):
                x_values.append(x)
                y_values.append(y)
    
    print("length of x_values", len(x_values))
    print("length of y_values", len(y_values))
    hit_arr = []

    # determine which rects are struck
    for r in r_arr:
        rx = r.get_x()
        ry = r.get_y()
        rw = r.get_width()
        rh = r.get_height()

        for i in range(0, len(x_values)):
            x = x_values[i]
            y = y_values[i]
            if (x >= rx and x < (rx + rw)) and (y >= ry and y < (ry + rh)):
                hit_arr.append(r)
                break
    return (r_arr, hit_arr)


def display_strike(rects, hit_rects):
    # highlight struck rects
    for r in hit_rects:
        r.set_color('gold')

    # display image and rectangles  
    for r in rects:
        ax.add_patch(r)
    
    print("Total boxes: %d, struck boxes: %d" % (len(rects), len(hit_rects))) 

    plt.imshow(img)


    plt.show()


img = mpimg.imread("C:/Users/parth/Dropbox/Projects/Coding/fractal_dim/britain.png")
fig, ax = plt.subplots(1)



pix_count = 0
for r in range(0, len(img)):
    for c in range(0, len(img[r])):
        pix_count += 1

print("total pixels in image %d" % pix_count)


grid, highlighted = test_hit(1)
display_strike(grid, highlighted)






