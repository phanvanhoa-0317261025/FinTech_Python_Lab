# 1. Khai báo các thông số của trái phiếu
F = 1_000_000  # Mệnh giá trái phiếu (VNĐ)
c = 0.09  # Lãi suất coupon (9%/năm)
N = 10  # Thời hạn trái phiếu (10 năm)
y = 0.085  # Tỷ lệ lợi suất kỳ vọng thị trường - YTM (8.5%/năm)

# 2. Tính tiền lãi coupon hàng năm
C = F * c

# 3. Tính Giá trị hiện tại (PV) của từng khoản lãi coupon qua 10 năm
tong_pv_coupon = 0.0

print("=== BÁO CÁO ĐỊNH GIÁ TRÁI PHIẾU DOANH NGHIỆP ===")
print(f"Mệnh giá (F): {F:,.0f} VNĐ | Lãi coupon (c): {c*100:.1f}%/năm")
print(
    f"Lợi suất kỳ vọng (YTM - y): {y*100:.1f}%/năm | Tiền lãi coupon/năm (C): {C:,.0f} VNĐ\n"
)

print(f"{'Năm (t)':^8} | {'Dòng tiền Coupon':^20} | {'PV của Coupon':^22}")
print("-" * 56)

for t in range(1, N + 1):
    pv_c = C / ((1 + y) ** t)
    tong_pv_coupon += pv_c
    print(f"{t:^8} | {C:16,.0f} VNĐ | {pv_c:18,.2f} VNĐ")

print("-" * 56)

# 4. Tính PV của mệnh giá gốc nhận lại vào năm thứ 10
pv_f = F / ((1 + y) ** N)

# 5. Giá lý thuyết của trái phiếu (P0)
gia_trai_phieu = tong_pv_coupon + pv_f

# 6. Xác định trạng thái giá trái phiếu
if gia_trai_phieu > F:
    trang_thai = "Cao hơn mệnh giá (Premium - Bán phụ trội)"
elif gia_trai_phieu < F:
    trang_thai = "Thấp hơn mệnh giá (Discount - Bán chiết khấu)"
else:
    trang_thai = "Đúng mệnh giá (Par)"

# 7. In tổng kết kết quả
print(f"Tổng PV của các khoản lãi Coupon: {tong_pv_coupon:18,.2f} VNĐ")
print(f"PV của mệnh giá gốc (năm {N}):     {pv_f:18,.2f} VNĐ")
print("=" * 56)
print(f"GIÁ LÝ THUYẾT TRÁI PHIẾU (P0):   {gia_trai_phieu:18,.2f} VNĐ")
print(f"ĐÁNH GIÁ TRẠNG THÁI:             {trang_thai}")