import matplotlib.pyplot as plt 
import matplotlib.patches as pat

fig, ax = plt.subplots(1)

x_values = [1, 2, 3, 7, 4]
y_values = [5, 2, 4, 5, 1]
plt.plot(x_values, y_values)


# This is because the range() function can't handle floats.
# Set box size here and increase the min/max by the corresponding 1/b_size ratio.
b_size = .1
quant = int(1/b_size)

q_x_min = quant * min(x_values)
q_x_max = quant * max(x_values)

q_y_min = quant * min(y_values)
q_y_max = quant * max(y_values)

r_arr = []

# Adds rectangles to an array and adds to plot 
for i in range(q_x_min, q_x_max, 1) :
    for j in range(q_y_min, q_y_max, 1) :
        xy = (i/quant, j/quant)
        rect = pat.Rectangle(xy, b_size, b_size, fill = False)
        r_arr.append(rect)
        ax.add_patch(rect)

hit_arr = []

# determine which rects are struck
for r in r_arr:
    rx = r.get_x()
    ry = r.get_y()
    rw = r.get_width()
    rh = r.get_height()

    for i in range(0, len(x_values)-1):
        x = x_values[i]
        y = y_values[i]
        if (x >= rx and x <= (rx + rw)) and (y >= ry and y <= (ry + rh)):
            hit_arr.append(r)

# highlight struck rects
for r in hit_arr:
    r.fill = True

plt.show()



