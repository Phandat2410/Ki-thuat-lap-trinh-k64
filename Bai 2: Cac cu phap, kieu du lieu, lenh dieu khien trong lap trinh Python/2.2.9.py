print ("Ho ten: Phan The Dat")
print ("MSSV: 235752021610094")
str=input("Nhap mot chuoi: ")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict [n] += 1
    else:
        dict [n] = 1
print (dict)
