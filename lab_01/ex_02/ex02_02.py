# 1. Nhập bán kính từ người dùng
ban_kinh = float(input("Nhập bán kính của hình tròn: "))

# 2. Tính diện tích của hình tròn (S = Pi * R^2)
# Sử dụng giá trị Pi là 3.14 như yêu cầu của đề bài
dien_tich = 3.14 * (ban_kinh ** 2)

# 3. In diện tích của hình tròn ra màn hình
print("Diện tích của hình tròn là:", dien_tich)