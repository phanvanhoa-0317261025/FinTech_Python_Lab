# 1. Nhập vào Họ Tên đầy đủ
ho_ten = input("Nhập Họ Tên đầy đủ: ")

# 2. Nhập vào Năm sinh
nam_sinh = input("Nhập Năm sinh: ")

# 3. Tách lấy từ cuối cùng (phần Tên) và lấy 3 ký tự đầu viết hoa
ten_chinh = ho_ten.split()[-1]
ten_ngan = ten_chinh[0:3].upper()

# Tạo mã ưu đãi
promo_code = f"{ten_ngan}-{nam_sinh}-VIP"

# In kết quả ra màn hình
print("Mã ưu đãi của bạn là:", promo_code)
