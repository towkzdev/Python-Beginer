#Assigment_3 กลุ่มเลขคู่ - เลขคี่

number=[]
odd = [] #เลขคี่
even = [] #เลขคู่
while True:
    x=int(input("Enter your number :"))
    if x<0:
        break
    if x%2 == 0:
        even.append(x)
    else:
        odd.append(x)
    number.append(x)

print("ตัวเลขทั้งหมด : ",number)
print("เลขคี่ : ",odd)
print("เลขคี่ : ",even)
