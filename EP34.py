#ป้อนตัวเลขเพื่อหาผลรวม

start,stop = 1,5
sum = 0
i=1
while(start<=stop):
    print("จำนวนที่:",i)
    number=int(input(":"))
    sum+=int(number)
    start+=1
    i+=1

print("ผลรวม =",sum)
print("ค่าเฉลี่ย: ",(sum/stop))