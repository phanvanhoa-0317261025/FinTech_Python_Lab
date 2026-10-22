# 1. Khởi tạo các biến ban đầu theo yêu cầu đề bài
tuoi = 25
so_du = 0.0
tien_gui = 60000000.0  # 60 triệu VNĐ năm đầu
lai_suat = 0.10  # Tỷ suất sinh lời 10%/năm
tang_tien_gui = 0.08  # Tăng trưởng khoản gửi 8%/năm
muc_tieu = 10000000000.0  # Mục tiêu 10 tỷ VNĐ

nam = 1

# 2. In tiêu đề báo cáo
print("=== BÁO CÁO MÔ PHỎNG KẾ HOẠCH HƯU TRÍ TỰ ĐỘNG ===")
print(f"Mục tiêu tài sản: {muc_tieu:,.0f} VNĐ")
print("Năm | Tuổi | Tiền gửi mới | Tiền lãi phát sinh | Dư nợ/Tài sản cuối năm")
print("-" * 73)

# 3. Vòng lặp while tính toán tích lũy cho đến khi đạt hoặc vượt mục tiêu
while so_du < muc_tieu:
    # Tính tiền lãi trong năm (đầu kỳ chưa có tiền lãi cho năm 1)
    tien_lai = so_du * lai_suat

    # Cập nhật số dư cuối năm
    so_du = so_du + tien_lai + tien_gui

    # In kết quả từng năm
    print(
        f"{nam:<3} | {tuoi:<4} | {tien_gui:12,.0f} VNĐ | {tien_lai:15,.0f} VNĐ | {so_du:18,.0f} VNĐ"
    )

    # Cập nhật thông số chuẩn bị cho bước lặp năm sau
    tien_gui = tien_gui * (1 + tang_tien_gui)
    tuoi += 1
    nam += 1

print("-" * 73)

# 4. In kết luận
tong_so_nam = nam - 1
tuoi_nghi_huu = tuoi - 1
print(
    f"KẾT LUẬN: Khách hàng sẽ đạt mục tiêu nghỉ hưu sau {tong_so_nam} năm (lúc {tuoi_nghi_huu} tuổi)."
)