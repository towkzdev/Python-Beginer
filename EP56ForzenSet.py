#FrozenSet

fruit=set(["กล้วย","มะยม","มะนาว","แอปเปิ้ล","ทุเรียน"])
fruit.add("ลิ้นจี่")
fruit.discard("มะยม")
print(fruit)

fruit=frozenset(["กล้วย","มะยม","มะนาว","แอปเปิ้ล","ทุเรียน"]) #frozenset ไม่สามารถแก้ไขข้อมูลได้
fruit.add("ลิ้นจี่")
fruit.discard("มะยม")
print(fruit)
