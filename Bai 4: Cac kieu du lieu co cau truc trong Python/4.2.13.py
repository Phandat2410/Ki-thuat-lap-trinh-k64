print ("Họ tên: Phan Thế Đạt")
print ("MSSV: 235752021610094")

s = input("Nhập chuỗi: ").split()

Phan_tu_can_tim = input("Nhập từ cần tìm: ")

try:
    index = s.index(Phan_tu_can_tim)
    print(f"Vị trí của chuỗi {Phan_tu_can_tim} ở vị trí: {index}")
except ValueError:
    print(f"{Phan_tu_can_tim} không có trong danh sách.")
