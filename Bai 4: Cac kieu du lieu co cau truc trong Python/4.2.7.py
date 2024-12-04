print ("Ho ten: Phan The dat")
print ("MSSV: 235752021610094")



input_string = input("Nhập chuỗi: ")

output_string = ''.join(char for char in input_string if not char.isdigit())

# In ra chuỗi mới
print("Chuỗi sau khi loại bỏ chữ số:", output_string)

