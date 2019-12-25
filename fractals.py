import matplotlib.pyplot as plt 
import matplotlib.patches as pat

fig, ax = plt.subplots(1)

x_values = [1, 2, 3, 7, 4]
y_values = [5, 2, 4, 5, 1]
plt.plot(x_values, y_values)

# xy = (2,2)
# r1 = pat.Rectangle(xy, 2, 2)
# ax.add_patch(r1)

q_x_min = 4 * min(x_values)
q_x_max = 4 * max(x_values)

q_y_min = 4 * min(y_values)
q_y_max = 4 * max(y_values)


# x_range = x_max - x_min
# y_range = y_max - y_min

for i in range(q_x_min, q_x_max, 1) :
    for j in range(q_y_min, q_y_max, 1) :
        xy = (i/4, j/4)
        rect = pat.Rectangle(xy, .25, .25, fill = False)
        ax.add_patch(rect)



plt.show()



