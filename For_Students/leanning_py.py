'''
#การสร้าง comment(code ในบรรทัดนั้นจะไม่ run) บน coding ภาษา python 
#1. ใช้สัญลักษณ์ (#)
    #comment เป็นบรรทัด
    
#2.ใช้สัญลักษณ์ "(bubble code)
"""(เปิด)
ตัวอย่างการทำงาน
a = 10
b = 5
c = a+b
print(C)
(ปิด)"""

#3.ใช้สัญลักษณ์ '(single code)
(เปิด)
ตัวอย่างการทำงาน
(ปิด)

print("test_COMMENT")
z=20
x=5
y=x-z
print(y)
'''
#function print() หรือ การแแสดงผลออกทางหน้าจอ (output)
print("ตัวดำเนินการ") #ใน () คือตัวดำเนินการ
print("ข้อความ")
print("Hello word")
print(10)
print(-5)

#การแสดงผลรูปแบบข้อความจะอยู่ในเครื่องหมาย "" หรือ '' (String)
print("-5")
print('10')
print('สวัสดี')
print("Hello")

a = "10"
b = "5"
c = a+b #การต่อ string
print("Output :",c) #c = 105

#number => ตัวเลข integer(จำนวนเต็ม) , float(ทศนิยม)
print(1) #int
print(-1) #int
print(0) #int
print(3.99) #float
print(1+9) #int

#boolean(ค่าความจริง) => true(เป็นจริง,1) , false(เป็นเท็จ,0) แสดงค่าในรูปแบบค่าความจริง
print(True)
print(False)

#data type & variable ชนิดเเละรูปแบบของข้อมูล
'''
int(ตัวเลข-จำนวนเต็ม)
float(ตัวเลข-ทศนิยม)
boolean(ค่าความจริง)
str(string-ข้อความ)
'''

# กฏการตั้งชื่อ
'''
1.ตัวเลข ตัวอัษร เครื่องหมายพิเศษ ( - , _ , . )
2.ห้ามขึ้นต้นด้วยตัวเลขและสัญลักษณ์ ยกเว้น...
3.ห้ามซ้ำกับ Keyword ("print","input","output","True","int")
4.case sensitive
'''

_a = 10
a_1 = 10

#การแปลงชนิดข้อมูล (Type Conversion)

a = 10  #->> int , str

b = int(a) #--> int
c = str(a) #--> str
d = float(a) #--> float
print(type(b))
print(type(c))
print(type(d))

#input function

name = input("กรุณาป้อนชื่อ : ") #Gr --> name = Gr
print("ชื่อ : "+name) #ชื่อ : Gr
print(type(name))# class : <'str'>

#ตัวดำเนินการทางคณิต
x = 10
y = 3
print("ผลบวก = ",x+y)
print("ผลลบ = ",x-y)
print("ผลคูณ = ",x*y)
print("ผลหาร = ",x/y)
print("ผลหาร = ",int(x/y))
print("ยกกำลัง = ",x**y)
#mod หารเอาเศษ
print("หารเอาเศษ", x%y)

#ตัวดำเนินการทางตรรกศาสตร์(ค่าความจริง= และ หรือ ถ้าแล้ว ก็ต่อเมื่อ)
#and or not -->True , False
x = (5>10) #False
y = (10==5) #False
z = x and y #z = False and False --> z = False
print("ผล Z :",z)
a = x or y # a = False or False --> a = False
print("ผล :",a)
print("ผล :",not(a)) # not(a) = True

#Compound Assignment (การลดรูปตัวดำเนินการ)
x = 10
print("ก่อน :",x)
x+=5 #x = x+5
#x-=5 #x = x+5
#x*=5 #x = x-5
#x/=5 #x = x*5
#x//=5 #x = x/5
#x//=5 #x = x//5
#x**=5 #x = x**5#x%=5 #x = x%5
print("หลัง :",x)

#ลำดับความสำคัญของตัวดำเนินการ
'''แบบเลือกลำดับ
if เงือนไขเป็นจริง:
    statement(คำสั่งดำเนินการ)
else:
    statement(คำสั่งดำเนินการ)
'''

#Ex.
age = int(input("Enter your Age : "))
if age>=15:
    print("คำนำหน้าเป็น นาย/นางสาว")
else:
    print("จบโปรแกรม")
print("Good bye")

# โครงสร้างควบคุมแบบเลือก (if..else)
'''
if เงือนไขเป็นจริง:# a<10 :
    statement(คำสั่งดำเนินการ)
if เงื่อนไขเป็นจริง:
    statement(คำสั่งดำเนินการ)
else:
    statement(คำสั่งดำเนินการ)
'''
age = int(input("Enter your Age : ")) #28
if age>=15:
    print("วัยรุ่น")
elif age>=20:
    print("วัยผู้ใหญ่")
elif age>=30:
    print("วัยทำงาน")
else :
    print("วัยเด็ก")

print("จบโปรแกรม")

#การใช้ And Or Not(ตรงกันข้าม:จะใช้กับค่าความจริง(True,False)
yy = not(True)
xx = not(False)
print(xx)
print(yy)
age = int(input("Enter your Age : "))

#and
#15 - 20 =>วัยรุ่น
#21 - 29 =>วัยผู้ใหญ่
#30 - 39 =>วัยทำงาน
if age>=15 and age<=20:
    print("วัยรุ่น")
elif age>=21 and age<=29:
    print("วัยผู้ใหญ่")
elif age>=30 and age<=39:
    print("วัยทำงาน")
elif age>=80:
    print("วัยชรา")
else:
    print("วัยเด็ก")
    
#or
if age>=15 or age<=20:
    print("วัยรุ่น")
else:
    print("วัยเด็ก")

#not
if not age>=15:
    print("วัยรุ่น")
else:
    print("วัยเด็ก")

#if ซ้อน if

age = int(input("Enter your Age : ")) #14

if age<=15:
    if age==15:
        print("ม.3")
    elif age==14:
        print("ม.2")
    elif age==13:
        print("ม.1")
    else:
        print("ประถมศึกษา")
else:
    print("ม.ปลาย")


#input
id = str(input("Enter Student Id: "))#student id
#surname
#lastname
income = 0#income

#process
if income >= 0 and income<= 150000:
    tax_5 = 5
    tax = income*(5/100)#รายได้ไม่เกิน 150000 : 0 <= income <= 150000 ;0%
#รายได้ 150001-300000 : 150001 <= income <= 300000 ;5%
#รายได้ 150001-300000 : 300001 <= income <= 500000 ;10%
#รายได้ 150001-300000 : income >= 500000 ;20%

#Output
#student id
#surname
#lastname
#income
print("Tax:",tax_5,"%")#tax%
print("Tax",tax,"THB")#tax THB

