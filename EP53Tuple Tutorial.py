#การนิยาม , constructor
print("การนิยาม , constructor")
tup = tuple((1,2,3,4,"kla satjaphon",True,3.99)) #tuple
lis = list([1,2,3,4,"kla satjaphon",True,3.99]) #list

lis[0]="BKK"

print(tup)
print(lis)

#การเข้าถึงข้อมูล
print("การเข้าถึงข้อมูล")
tup_1 = tuple((1,2,3,4,"kla satjaphon",True,3.99)) #tuple

print(tup_1[4])
print(tup_1[1:4])
print(tup_1[-2])
print(tup_1[-3:-1])

#การแก้ไขข้อมูล
print("การแก้ไขข้อมูล")
tup_2 = (1,2,3,4,"kla satjaphon",True,3.99)
lis_1=list(tup_2)

lis_1[0]="Bangkok"

print("ก่อนแก้ไข",tup_2)
print("หลังแก้ไข",lis_1)

#การแสดงผลด้วย Loop
tup_3 = (1,2,3,4,"kla satjaphon",True,3.99)

for item in tup_3:
    print("สมาชิก = ",item)

if True in tup_3:
    print("เป็นสมาชิก")
else:    
    print("ไม่เป็นสมาชิก")

#นับจำนวนสมาชิก(len)
    
print(len(tup_3))

for item in range(len(tup_3)):
    print(tup_3[item])

#การสร้าง

x=()
y=("Satjaphon",)
z=tuple()

print(type(x))
print(type(y))
print(type(z))

#เพิ่มข้อมูล (join)
name=("satjaphon","jojo")
new=("nut",)

newname=name+new
print(newname)

#ทำงานร่วมกับ list
tup_4 = (1,2,3,4,"kla satjaphon",True,3.99)

lis=list(tup_4)
lis[0]="BKK"

tup_5=tuple(lis)
print(tup_5)

city=["กรุงเทพ","อุบล","ชลบุรี"]
tup_6=tup_5+tuple(city)

print(tup_6)

#การลบข้อมูล del
#del tup_6[5]
lis=list(tup_6)
lis.pop(5)
lis.remove("กรุงเทพ")
tup_7=tuple(lis)

print(type(lis))
print(lis)
print(type(tup_7))
print(tup_7)

#ค้นหา(index)และนับจำนวนสมาชิก(Count)
tup_5 = (1,2,3,4,"kla satjaphon",True,3.99)
x=tup_5.count(4) 
y=tup_5.index(4)

print(x)
print(y)

#การ sort ข้อมูล
tup_8=(100,99,98,88,20,1,2,3,4,5,3.99)
print("Before :",tup_8)
lis=list(tup_8)
lis.sort()
lis.reverse()
tup_9=tuple(lis)
print("After :",tup_9)
print("After :",tup_9)


#ค่าใน tuple => ตัวแปร
tup=(10,20,30)
a,b,c=tup
print(a)
print(b)
print(c)
d=a+c
print(d)

#การสลับ tuple
x=(50,60)
y=(88,99)
print("Befor x :",x)
print("Befor y :",y)
x,y = y,x
print("After x :",x)
print("After y :",y)

#tuple => string
character=('k','l','a')
name="".join(character)
print(name)

#reverse tuple
x=(100,20,30,15,5,500)
y=tuple(reversed(x))
print(y)
print(list(y))

#string to tuple
x="kla satjaphon"
y=tuple(reversed(x))
print(y)