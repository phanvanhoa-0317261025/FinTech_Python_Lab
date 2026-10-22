# 1. Khai báo dữ liệu
V_goc = 20.0
d_ex_list = [-0.03, 0.0, 0.03]
d_ir_list = [-0.02, -0.01, 0.01, 0.02]

# 2. In tiêu đề bảng
print("=== MA TRẬN PHÂN TÍCH ĐỘ NHẠY GIÁ TRỊ DANH MỤC (TỶ VNĐ) ===")
print(f"Vốn ban đầu: {V_goc} Tỷ VNĐ\n")
print("Lãi suất \\ Tỷ giá |  -3.0%  |   0.0%  |  +3.0%  ")
print("-" * 50)

# 3. Vòng lặp lồng nhau tính toán và in ma trận
for ir in d_ir_list:
    
    print(f"Lãi suất: {ir * 100:+4.1f}% |", end="")

    for ex in d_ex_list:
        # Tính giá trị danh mục mới
        V_moi = V_goc * (1 + 1.5 * ex - 2.0 * ir)
        # In giá trị từng cột trên cùng 1 dòng
        print(f" {V_moi:5.2f} Tỷ |", end="")

    # Xuống dòng sau khi in hết 1 hàng
    print()

print("-" * 50)