#หาผลรวมเลข

i=1
summation = 0
avg = 0
count = int(input("Enter Number : "))
while i<=count:
    summation+=i
    print("รอบที่ ",i,"ผลรวม =",summation)
    i+=1
avg = summation/count
print("ผลรวม =",summation)
print("ค่าเฉลี่ย =",avg)