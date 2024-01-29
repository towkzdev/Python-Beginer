#ค้นหาเบอร์โทรศัพท์

data = {"191":"ตำรวจ","1669":"2","1112":"3"}

def searchNumber(message):
    for key , value in data.items():
        if value==message:
            print("เบอร์ติดต่อ",key)
            return
        else:
            pass#print("ไม่มีข้อมูล")
        


message = input("ป้อนข้อมูลที่ต้อการ: ")
searchNumber(message)