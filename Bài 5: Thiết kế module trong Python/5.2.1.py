print ("Họ tên: Phan Thế Đạt")
print ("MSSV: 235752021610094")

## File: mymath.py ##
def square(n):
    return n*n
def cube(n):
    return n*n*n
def average(values):
    nvals = len(values)
    sum = 0.0
    for v in values:
        sum += v
    return float(sum)/nvals
