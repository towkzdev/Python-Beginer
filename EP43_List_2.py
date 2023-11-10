#การแก้ไขข้อมูล

number = [1,2,3,4,5,6]
'''
print("ก่อนแก้ไข => ",number)

number[2]=9
number[-1]="นายไข่"

print("หลังแก้ไข => ",number)
'''
'''
#Loop for
sum=0
for x in number:
    sum=+x
print("Total",sum)
'''

'''
#การตรวจสอบข้อมูล
fruit=["มะม่วง","มะนาว","มะยม"]
input_data = input("Enter :")
if input_data in fruit:
    print("เป็น")
else:
    print("ไม่เป็น")
'''

#นับจำนวนสมาชิก
number_1 = [1,2,3,4,5,6]
fruit_2=["ส้ม","มะนาว","ทุเรียน"]
print(number_1)
print(fruit_2)
#การเพิ่มข้อมูล
fruit_2.append("มะปราง")
print("หลังเพิ่ม =>",fruit_2)
