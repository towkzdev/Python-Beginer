number_1 = [1,2,3,4,5,6]
fruit_2=["ส้ม","มะนาว","ทุเรียน"]
number_2 = [11,22,33,44,55,56,56,66]
#การคัดลอกข้อมูล
x=[]
print(x)
x=fruit_2.copy()
print(x)

#การรวมสมาชิก (+)

allGroup_1=number_1+fruit_2
print("+",allGroup_1)

#extend
number_2.extend(fruit_2)
print("Extrend",number_2)

#การค้นหาสมาชิก
number_3 = [1,2,3,4,5,6,1,2,3,4,5,6,3,4,5,6]
z=number_3.count(5)
print(z)