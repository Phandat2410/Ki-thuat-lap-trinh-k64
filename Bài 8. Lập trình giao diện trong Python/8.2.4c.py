print ("Họ tên: Phan Thế Đạt")
print ("MSSV: 235752021610094")

from tkinter import *

# a, Tạo cửa sổ đồ họa
window = Tk()
window.title("Đại Học Vinh")
# Đặt kích thước cửa sổ
window.geometry('350x200')   

# Thêm nhãn (Label) với nội dung ban đầu là "Xin Chào"
lbl = Label(window, text="Xin Chào")
lbl.grid(column=0, row=0)


