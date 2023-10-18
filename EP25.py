#เจาะลึก String (ตอนที่ 1)

#1 การเข้าถึงตัวอักษรใน string
print("#1--------------------------------------------------")
name = " Satjaphon : 40 " #index => 0

print(name) #ก่อนถึงจุดสุดท้าย
print("Age :",name[-3:]) #ก่อนถึงจุดสุดท้าย

#2 len function การหาความยาวของ str
print("#2--------------------------------------------------")
print("ความยาวของ string :",len(name))

#3strip ลบช่องว่าง
print("#3--------------------------------------------------")
name2 = name.strip() 
print(name2)
print("ความยาวของ string :",len(name2))
#ลบช่องว่าง left
name3 = name.lstrip() 
print(name3)
print("ความยาวของ string :",len(name3))
#ลบช่องว่าง right
name4 = name.rstrip() 
print(name4)
print("ความยาวของ string :",len(name4))

#4แปลง case ของ string
print("#4--------------------------------------------------")
name5 = "Satjaphon"
print(name5.upper())
print(name5.lower())
#แปลงตัวแรกเป็นตัวพิมพ์ใหญ่
name6 = "satjaphon"
print(name6.capitalize())

#5การแทนที่ replace
print("#5--------------------------------------------------")
name7="Satjaphon อายุ 22 ปี 2022"
print(name7.replace("Sat","SAT"))
print(name7.replace("22","25",1))

#6การเช็คข้อความ
print("#6--------------------------------------------------")
name8="Satjaphon อายุ 22 ปี 2022"
x = "อายุ" in name8
if x:
    name8 = name8.replace("อายุ","Age")

print(name8)

