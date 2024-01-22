'''
จัดกลุ่มข้อมูลพื้นฐาน
List = [] , ข้อมูลต่างชนิดกัน ,แก้ไขข้อมูลสมาชิกได้ , ข้อมูลซ้ำกันได้ , ซ้ายไปขวา
Tuple = () , ข้อมูลต่างชนิดกัน ,แก้ไขข้อมูลสมาชิกไม่ได้ , ข้อมูลซ้ำกันได้ , ซ้ายไปขวา
Set = {} , ข้อมูลต่างชนิดกัน ,แก้ไขข้อมูลสมาชิกได้ , ข้อมูลซ้ำกันไม่ได้ , ลำดับไม่เเน่นอน
'''

#แบบปกติ
fruit = {"มะม่วง","มะขาม","มะยม"}

lis=["ปลาทู","ปลาตะเพียน"]
#constructor
fish = set(["ปลาดุก","ปลานิล","ปลานิล"])
fish_1=set(lis)
print(fish)
print(fish_1)
print(type(fruit))

#การเพิ่มข้อมุลสมาชิก
fruit.add("ทุเรียน")
fruit.add("สับปะรด")
fruit.add(999)
print(fruit)

#การเพิ่มข้อมูลสมาชิกหลายตัว
fruit.update(lis)
fruit.update(["ตะไคร้","โหระพา","ชะอม"])
print(fruit)

#Loop
for item in fruit:
    print("ช้อมูล =>",item)

#แสดงจำนวนสมาชิก
print(len(fruit))

if "มะเฟือง" in fruit:
    print("มี")
else:
    print("ไม่มี")

#การลบข้อมูล
fruit.remove("ทุเรียน")
fruit.discard("มะนาว")
del fruit
fruit.clear()
print(fruit)