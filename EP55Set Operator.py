#Union
fruitA={"กล้วย","มะยม","มะนาว","แอปเปิ้ล","ทุเรียน"}
fruitB={"แอปเปิ้ล","ทุเรียน","สตอเบอร์รี่","กีวี่","มะม่วง"}

allfruit=fruitA.union(fruitB) #การสร้างsetใหม่
fruitA.update(fruitB)

print(allfruit)
print(fruitA)

#differance
fruitC=fruitA.difference(fruitB)
print(fruitC)

fruitA.difference_update(fruitB)
print(fruitA)

fruitA.intersection_update(fruitB)
print(fruitA)

#superbset
fish={"ปลาดุก","ปลาหมอ","ปลาวาฬ","ปลาโลมา","ปลาฉลาม","ปลาตะเพียน"}
#subset
x={"ปลาหมอ","ปลาซิว"}
y={"ปลาวาฬ","ปลาฉลาม"}

print(x.issubset(fish))
print(fish.issuperset(x))
print(y.issubset(fish))
print(fish.issuperset(y))

#min,max
number = {3,4,5,100,80,900,1000,500,300,-100,-8,-150}

print(min(number))
print(max(number))
