#จับคู่สินค้าและราคา

fruit = ["มะม่วง","มะนาว","มะยม","ทุเรียน"]
price = [1,2,3,4]

for x,y in zip(fruit,price):
    print("สินค้า",x,"ราคา",y)