print ("Họ tên: Phan Thế Đạt")
print ("MSSV: 235752021610094")

def fibonacci_less_than_n(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

n = int(input("Nhập số nguyên: "))

fibonacci_numbers = fibonacci_less_than_n(n)

print(f"Các số Fibonacci nhỏ hơn {n} là: {fibonacci_numbers}")
