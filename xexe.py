from PIL import Image

# Mở ảnh JPEG
img = Image.open("xe.jpg").convert("RGBA")

# Lấy dữ liệu pixel
datas = img.getdata()

# Màu caro phổ biến (trắng và xám nhạt) sẽ được làm trong suốt
new_data = []
for item in datas:
    r, g, b, a = item

    # Điều kiện nền caro giả (xám nhạt hoặc trắng)
    if (r > 200 and g > 200 and b > 200) or (180 < r < 220 and 180 < g < 220 and 180 < b < 220):
        # Biến thành trong suốt
        new_data.append((255, 255, 255, 0))
    else:
        # Giữ nguyên pixel
        new_data.append((r, g, b, a))

# Gán lại dữ liệu ảnh
img.putdata(new_data)

# Lưu ảnh mới với nền trong suốt
img.save("xe_clean.png")

print("✅ Đã xử lý và lưu ảnh trong suốt: xe_clean.png")
