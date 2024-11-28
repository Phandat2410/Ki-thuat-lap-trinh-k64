print ("Ho ten: Phan The dat")
print ("MSSV: 235752021610094")

def get_sum(*num):
    tmp = 0
     # duyet cac tham so
    for i in num:
         tmp += i
    return tmp
result = get_sum(1, 4, 3, 6, 5)
print(result)
