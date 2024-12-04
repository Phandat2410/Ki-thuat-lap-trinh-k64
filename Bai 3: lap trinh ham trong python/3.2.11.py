print ("Họ tên: Phan Thế Đạt")
print ("MSSV: 235752021610094")

def benefit(t, n, k):
    return n * (1 + t / 100) ** k

# Ví dụ sử dụng hàm:
t = float(input("Nhập lãi suất tiết kiệm (%/tháng): "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))

tong_tien = benefit(t, n, k)
print(f"Số tiền nhận được sau {k} tháng là: {tong_tien:.2f}")
