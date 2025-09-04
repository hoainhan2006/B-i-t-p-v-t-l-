import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

# Đọc và xử lý ảnh để bỏ nền trắng caro (nếu cần)
# Mở ảnh bằng PIL và chuyển sang RGBA
img = Image.open("xe_clean.png").convert("RGBA")

# Lọc bỏ nền trắng (trong suốt hóa)
datas = img.getdata()
new_data = []
for item in datas:
    # Nếu là trắng hoặc gần trắng => trong suốt
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        new_data.append((255, 255, 255, 0))  # Alpha = 0 (trong suốt)
    else:
        new_data.append(item)

img.putdata(new_data)
img.save("xe_clean.png")  # Lưu ảnh đã xử lý


# ===============================

# Hàm vị trí theo thời gian: x(t)
def x(t):
    return -4 * t + 2 * (t ** 2)


# Mảng thời gian từ 0 đến 5 giây
t = np.linspace(0, 5, 200)
x_vals = x(t)

# Tạo figure và axis
fig, ax = plt.subplots()
ax.set_xlim(min(x_vals) - 1, max(x_vals) + 1)
ax.set_ylim(-1, 1)  # Chạy trên y = 0
ax.set_xticks(np.arange(np.floor(min(x_vals)), np.ceil(max(x_vals))+2, 2))

# Ẩn trục y, chỉ hiển thị trục x
ax.set_xlabel("Position x(t)")
ax.get_yaxis().set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.axhline(y=0, color='black', linewidth=1)  # Đường chạy

# Đọc ảnh xe đã xử lý (nền trong suốt)
car_img = mpimg.imread("xe_clean.png")
imagebox = OffsetImage(car_img, zoom=0.15)  # Chỉnh zoom nếu cần
car = AnnotationBbox(imagebox, (x_vals[0], 0), frameon=False)
ax.add_artist(car)

# Hiển thị thời gian
time_text = ax.text(0.95, 0.85, '', transform=ax.transAxes,
                    ha='right', va='top',
                    fontsize=12, bbox=dict(boxstyle="round", facecolor="white", alpha=0.7))

# Thêm sau dòng tạo time_text
position_text = ax.text(0.95, 0.78, '', transform=ax.transAxes,
                        ha='right', va='top',
                        fontsize=12, bbox=dict(boxstyle="round", facecolor="white", alpha=0.7))

# Hàm khởi tạo
def init():
    car.set_visible(True)
    time_text.set_text('')
    position_text.set_text('')   # reset text vị trí
    return car, time_text, position_text

# Hàm cập nhật
def update(frame):
    current_time = t[frame]
    current_x = x_vals[frame]

    car.xybox = (current_x, 0)
    time_text.set_text(f'Time: {current_time:.2f} s')
    position_text.set_text(f'Position: {current_x:.2f}')
    return car, time_text, position_text

# Tạo animation
ani = animation.FuncAnimation(
    fig, update, frames=len(t), init_func=init,
    blit=True, interval=50, repeat=False
)

plt.show()
