#ฟังก์ชั่นแบบคืนค่า

'''
1.ไม่มีการรับค่าและส่งค่า
def namr():

2.มีการรับค่าเข้าไม่ทำงาน
def nmae(a,b):

3.รับค่าเข้าไปทำงานและส่งออกมา
def mname(a,b)

4.ไม่มีการรับค่าเข้ามา แต่ส่งค่าออกไป
'''


def add(a,b):
    return(a+b)

def shoeNumber():
    return 500
    
x=add(12,20)
print(x)

y=shoeNumber()
print(y)

def randomNumber(z):
    if z == "100" :
        print("คุณถูกหวย")
        return 1000
    else:
        print("เสียใจด้วยจ้า")
        return 0

x=300
money_1=randomNumber("200")        
result=(money_1)-x
print("เงินรางวัล=",money_1)
print("เงินคงเหลือ=",result)
money_2=randomNumber("100")        
result=(money_2)-x
print("เงินรางวัล=",money_2)
print("เงินคงเหลือ=",result)
        