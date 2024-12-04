print ("Họ tên: Phan Thế Đạt")
print ("MSSV: 235752021610094")

def check_binary_divisible_by_5(binary_string):
    
    binaries = binary_string.split(',')
    
    divisible_by_5 = []
    
    for binary in binaries:
      
        if len(binary) == 4 and all(bit in '01' for bit in binary):
           
            decimal = int(binary, 2)
            
            if decimal % 5 == 0:
                divisible_by_5.append(binary)

    if divisible_by_5:
        print("Số nhị phân chi hết cho 5:", ', '.join(divisible_by_5))
    else:
        print("Không cố số nhị phân nào chia hết cho 5.")

input_string = input("Nhập chuỗi số nhị phân: ")
check_binary_divisible_by_5(input_string)
