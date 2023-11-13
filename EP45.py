#Assignment_2 หาค่าตัวเลขต่ำสุด - สูงสุด (.sort)
number=[]
while True:
    x=int(input("Enter your number :"))
    if x<0:
        break
    number.append(x)


print("Set =>",number)
print("ค่าที่น้อยที่สุด =>",min(number))
print("ค่าที่มากที่สุด =>",max(number))
print("ผลรวม =>",sum(number))
print("End Programe")