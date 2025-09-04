import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Hàm vị trí theo thời gian
def x(t):
    return -4*t + 2*(t**2)

# Tạo mảng thời gian
t = np.linspace(0, 5, 200)  # từ 0s đến 5s
x_vals = x(t)

# Tạo figure và axis
fig, ax = plt.subplots()
ax.set_xlim(0, 5)
ax.set_ylim(min(x_vals)-1, max(x_vals)+1)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Position x(t)")

line, = ax.plot([], [], lw=2, label="x(t)")
point, = ax.plot([], [], 'ro')  # biểu diễn chiếc xe
ax.legend()

# Hàm khởi tạo
def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

# Hàm cập nhật animation
def update(frame):
    line.set_data(t[:frame], x_vals[:frame])
    point.set_data([t[frame]], [x_vals[frame]])
    return line, point

ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=50)

plt.show()
