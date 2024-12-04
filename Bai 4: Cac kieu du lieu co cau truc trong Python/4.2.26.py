print ("Họ tên: Phan Thế Đạt")
print ("MSSV: 235752021610094")

# Khởi tạo số dư ban đầu
so_du = 0

while True:
    # Nhận đầu vào giao dịch từ người dùng
    nhat_ky = input("Nhập giao dịch (hoặc nhấn Enter để kết thúc): ")

    # Kiểm tra nếu người dùng kết thúc việc nhập
    if not nhat_ky:
        break

    # Phân tích cú pháp của chuỗi đầu vào
    loai_giao_dich, so_tien = nhat_ky.split()
    so_tien = int(so_tien)

    # Cập nhật số dư dựa trên loại giao dịch
    if loai_giao_dich == 'D':
        so_du += so_tien
    elif loai_giao_dich == 'W':
        so_du -= so_tien

# In kết quả
print("Số tiền thực của tài khoản ngân hàng là:", so_du ,"VND")
