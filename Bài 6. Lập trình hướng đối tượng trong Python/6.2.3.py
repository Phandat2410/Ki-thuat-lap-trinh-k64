print ("Họ tên: Phan Thế Đạt")
print ("MSSV: 235752021610094")

class Nguoi(object):
    def getGender( self ):
        return "Unknown"

class Nam( Nguoi ):
    def getGender( self ):
        return "Nam"

# Code by Quantrimang.com
class Nu( Nguoi ):
    def getGender( self ):
        return "Nữ"

aNam = Nam()
aNu= Nu()
print (aNam.getGender())
print (aNu.getGender())  
