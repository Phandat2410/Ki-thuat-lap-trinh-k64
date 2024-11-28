print ("Ho ten: Phan The dat")
print ("MSSV: 235752021610094")


import math

def Tinh(R):
    if R <= 0:
        return "Bán kính phải là một số dương"
    
    chu_vi = 2 * math.pi * R

    dien_tich = math.pi * R**2
    
    return chu_vi, dien_tich

R = float(input("Nhập bán kính của hình tròn: "))
ket_qua = Tinh(R)

if isinstance(ket_qua, tuple):
    print(f"Chu vi của hình tròn: {ket_qua[0]:.2f}")
    print(f"Diện tích của hình tròn: {ket_qua[1]:.2f}")
else:
    print(ket_qua)
