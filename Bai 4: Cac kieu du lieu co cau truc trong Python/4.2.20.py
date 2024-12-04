print ("Họ tên: Phan Thế Đạt")
print ("MSSV: 235752021610094")

def Tam_giac_Pascal(n):
    Tam_giac = []
    for i in range(n):
        So_hang = [1] * (i + 1)
        for j in range(1, i):
            So_hang[j] = Tam_giac[i - 1][j - 1] + Tam_giac[i - 1][j]
        Tam_giac.append(So_hang)
    for So_hang in Tam_giac:
        print(' '.join(map(str, So_hang)))

n = int(input("Nhập số dòng của tam giác Pascal: "))
Tam_giac_Pascal(n)
