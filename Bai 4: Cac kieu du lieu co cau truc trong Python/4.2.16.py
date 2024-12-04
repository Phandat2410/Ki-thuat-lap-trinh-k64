print ("Họ tên: Phan Thế Đạt")
print ("MSSV: 235752021610094")

n = input("Nhập chuỗi các số nhị phân (cách nhau bởi dấu phẩy): ")

So_nhi_phan = n.split(',')
print("Các số nhị phân đã nhập là:")
for nhi_phan in So_nhi_phan:
    print(nhi_phan.strip())  
