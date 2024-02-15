#ฟังก์ชั่นการสุ่ม (Random Module)
import random

x=random.random() # 0.0-1.0
print(x)

print("=============================================")

for i in range(10):
    y=random.random()
    print(y)

print("=============================================")

for i in range(15):
    z=random.uniform(-5,10) #สุ่มในช่วง -5 <= z <= 10
    print(z)

print("=============================================")

for i in range(15):
    v=random.randrange(1,10,2) #สุ่มในช่วง 1 <= v <= 10  เป็นจำนวนเต็ม +2 ทีละ step
    print(v)

print("=============================================")

for i in range(15):
    vs=random.randint(-4,5) #เป็นจำนวนเต็ม
    print(vs)

print("=============================================")
items_1=[1,2,3,4,5,"A","B","C"]
for i in range(15):
    it=random.choice(items_1)
    print(it)
print("=============================================")
for i in range(15):
    rd=random.choice("ABCasd123asdH")
    print(rd)
print("=============================================")
items_2=[1,2,3,4,5,"A","B","C"]
for i in range(15):
    random.shuffle(items_2)
    print(items_2)