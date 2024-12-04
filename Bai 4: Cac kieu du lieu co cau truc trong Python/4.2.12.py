print ("Ho ten: Phan The Dat")
print ("MSSV: 235752021610094")

# Nhập danh sách từ người dùng
input_list = input("Nhập các phần tử của danh sách (cách nhau bằng dấu phẩy): ").split(',')

# Nhập phần tử cần xóa
element_to_remove = input("Nhập phần tử cần xóa: ")

# Kiểm tra xem phần tử có trong danh sách không, rồi xóa
if element_to_remove in input_list:
    input_list.remove(element_to_remove)
    print("Danh sách sau khi xóa:", input_list)
else:
    print(f"Phần tử '{element_to_remove}' không có trong danh sách.")

