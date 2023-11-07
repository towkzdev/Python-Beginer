#หาผลรวมตัวเลข (ปรับเงื่อนไข)

sum = 0
i=1
while True:
    print("จำนวนที่:",i)
    number=int(input(":"))
    sum+=int(number)
    i+=1
    if sum>=100:
        break
    print("ผลรวม =",sum)
    print("-----------------------------")
