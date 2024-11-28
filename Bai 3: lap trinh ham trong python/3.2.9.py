print ("Ho ten: Phan The dat")
print ("MSSV: 235752021610094")


# This function adds two numbers 
def ham_cong(x, y):
    return x + y
# This function subtracts two numbers 
def ham_tru(x, y):
    return x - y
# This function multiplies two numbers
def ham_nhan(x, y):
    return x * y
# This function divides two numbers
def ham_chia(x, y):
    return x / y

print("Hãy chọn phép tính cần sử dụng.")
print("1. Phép tính cộng")
print("2. phép tính trừ")
print("3. phép tính nhân")
print("4. phép tính chia")

# Take input from the user 
choice = input("Hãy lựa chọn phép tính: ")
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứn hai: "))

if choice == '1':
    print(num1,"+",num2,"=", ham_cong(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=", ham_tru(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=", ham_nhan(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=", ham_chia(num1,num2))
else:
    print("Hãy nhập lại.") 
