#Assignment รับและเรียงบลำดับข้อมูลตัวเลข
number=[]
while True:
    x=int(input("Enter your number :"))
    if x<0:
        break
    number.append(x)


print("ก่อนเรียง =>",number)
number.sort()
print("น้อยไปมาก =>",number)

number.reverse()
print("มากไปน้อย =>",number)
print("End Programe")