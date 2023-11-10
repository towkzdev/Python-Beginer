#สร้างขอบตาราง

number=int(input("ป้อนขนาด = "))
for row in range(number):
    for colume in range(number):
        if row == 0 or row==number-1 or colume==0 or colume==number-1:
            print("X",end="")
        else:
            print(" ",end="")
    print(" ")