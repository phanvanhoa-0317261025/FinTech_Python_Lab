# 1. Yêu cầu nhập một địa chỉ email
email = input("Nhập địa chỉ email: ")

# 2. Dùng split("@") để tách phần tên đăng nhập và tên miền (domain)
username, domain = email.split("@")

# 3. Trích xuất 3 ký tự đầu tiên của tên đăng nhập (dùng Slicing [0:3])
first_3_chars = username[0:3]

# 4. Ghép 3 ký tự đầu + chuỗi "***@" + tên miền
masked_email = first_3_chars + "***@" + domain

# In kết quả ra màn hình
print("Email bảo mật:", masked_email)
