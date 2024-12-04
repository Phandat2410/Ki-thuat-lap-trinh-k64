print ("Ho ten: Phan The dat")
print ("MSSV: 235752021610094")

# Nhập dãy các từ từ bàn phím, ngăn cách bởi khoảng trắng
words = input("Nhập dãy các từ: ").split()

# Tìm độ dài của từ dài nhất
max_length = max(len(word) for word in words)

# In ra mọi từ có cùng độ dài nhất
longest_words = [word for word in words if len(word) == max_length]

print("Từ dài nhất có độ dài:", max_length)
print("Các từ dài nhất là:", longest_words)
