#ค้นหาตัวเลขมากสุด & น้อยสุด

max,min = 0,9999

while True:
    number = int(input("Enter your number :"))
    if number<0:
        break
    if number>max:
        max=number
    if number<min:
        min=number
    #print("Max Number :",max)
    #print("Min Number :",min)

print("Max Number :",max)
print("Min Number :",min)