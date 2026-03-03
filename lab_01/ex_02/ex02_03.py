# Nhập số nguyên từ người dùng
so = int(input("Nhập một số nguyên: "))

# Kiểm tra chẵn lẻ
if so % 2 == 0:
    print(so, "là số chẵn.")
else:
    print(so, "là số lẻ.")