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

# Hàm xử lý sự kiện khi nhấn nút
def clicked():
    # c, Thay đổi nội dung của nhãn khi nhấn nút
    lbl.configure(text="Nhấp vào đây!!")  

# b, Thêm nút bấm (Button), Nút có màu nền xanh và chữ trắng
btn = Button(window, text="Ok", command=clicked, bg="blue", fg="white") 
btn.grid(column=1, row=0)

# Khởi động vòng lặp chính của cửa sổ
window.mainloop()
