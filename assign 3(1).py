import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Hut points (x, y)
x = [40, 50, 50, 45, 40, 40]
y = [10, 10, 30, 40, 20, 10]

fig, ax = plt.subplots()
ax.set_xlim(-70, 70)
ax.set_ylim(-70, 70)
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'b-o')
fill = ax.fill([], [], 'green', alpha=0.4)[0]

# Rotate formula (direct)
def update(angle):
    rad = np.radians(angle)
    rx = [x[i]*np.cos(rad) - y[i]*np.sin(rad) for i in range(len(x))]
    ry = [x[i]*np.sin(rad) + y[i]*np.cos(rad) for i in range(len(y))]

    line.set_data(rx, ry)
    fill.set_xy(list(zip(rx, ry)))
    ax.set_title(f"Rotation : {angle}°")
    return line, fill

ani = FuncAnimation(fig, update, frames=range(0, 360, 5), interval=50)
plt.show()
