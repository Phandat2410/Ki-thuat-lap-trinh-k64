print ("Họ tên: Phan Thế Đạt")
print ("MSSV: 235752021610094")

import datetime as dt

format = '%Y-%m-%d %H:%M:%S'

t1 = dt.datetime.strptime('2008-10-12 14:45:52', format)
print('Ngày: ' + str(t1.day))         
print('Tháng: ' + str(t1.month))
print('Năm: ' + str(t1.year))
print('Giờ: ' + str(t1.hour))
print('Phút: ' + str(t1.minute))   
print('Giây: ' + str(t1.second))   

t2 = dt.datetime.now()
print('Ngày, giờ hiện tại: ', t2)

diff = t2 - t1
print('Số ngày chênh lệnh: ' + str(diff.days))
