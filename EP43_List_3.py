#การเพิ่มข้อมูล
number_1 = [1,2,3,4,5,6]
fruit_2=["ส้ม","มะนาว","ทุเรียน"]
print(number_1)
print(fruit_2)
fruit_2.append("แตงโม") #append เพิ่มต่อท้าย
print("หลังเพิ่ม =>",fruit_2)

#insert การแทรก
fruit_2.insert(1,"แอปเปิ้ล")
print("หลังแทรก",fruit_2)

#ลบข้อมูล
#remove
fruit_2.remove("มะนาว")
print("Remove",fruit_2)

#pop ลบล่าสุด
fruit_2.pop()
print("Pop",fruit_2)

#del ลบ index ตำแหน่งหมายเลข
del fruit_2[1]
print("Del",fruit_2)

del fruit_2
print(fruit_2)

#clear ลบสมาชิกออก

fruit_2.clear()
print(fruit_2)