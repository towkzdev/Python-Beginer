#break(หยุดการทำซ้ำ) / continue(กระโดดข้ามการทำงาน)

i=int(input("Loop while break :"))
while i<=10:
    print("รอบที่ :",i)
    if(i==5):
        break
    i+=1
else:
    print("จบการทำงาน")

print("-------------------------------------")

i=int(input("Loop while continue :"))
while i<=10:
    i+=1
    if(i==5):
        continue
    print("รอบที่ :",i)
else:
    print("จบการทำงาน")

print("-------------------------------------")

i=int(input("Loop for continue :"))
for i in range(1,11):
    if(i%2 == 0):
        continue
    print("รอบที่ :",i)

print("จบการทำงาน")

print("-------------------------------------")

i=int(input("Loop for break :"))
for i in range(1,11):
    if(i%2 == 0):
        break
    print("รอบที่ :",i)

print("จบการทำงาน")