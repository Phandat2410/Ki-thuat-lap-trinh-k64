print ("Ho ten: Phan The dat")
print ("MSSV: 235752021610094")
a=int(input("Nhap a: "))
b=int(input("Nhap b: "))
total = 0
print(a,end="")
while (a <=4000000-1):
    if a% 2 == 0:
        total += a
    a, b = b, a + b
    print(a,end="")
print("\n Tong cac so chan trong day Fibonacci la: ", total)
