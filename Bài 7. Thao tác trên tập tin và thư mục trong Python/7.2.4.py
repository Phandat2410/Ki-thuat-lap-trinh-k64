print ("Họ tên: Phan Thế Đạt")
print ("MSSV: 235752021610094")

def read_first_n_lines(filename, n):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for i in range(n):
                line = file.readline()
                if not line:
                    break
                print(line.strip())
    except FileNotFoundError:
        print(f"Không tìm thấy tệp '{filename}'.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        
def total_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print(f"Không tìm thấy tệp '{filename}'.")
        return 0
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        return 0

def main():
    filename = input("Nhập tên tệp (bao gồm phần mở rộng, ví dụ: 'data.txt'): ")
    total = total_lines(filename)
    print(f"Tổng số dòng trong tệp: {total}")
    n = int(input("Nhập số dòng bạn muốn đọc: "))
    read_first_n_lines(filename, n)
    

if __name__ == "__main__":
    main()
