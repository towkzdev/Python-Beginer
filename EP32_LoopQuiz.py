#แม่สูตรคูณ

start=int(input("แม่สูตรคูณเริ่มต้น : "))
stop=int(input("แม่สูตรคูณแม่สุดท้าย : "))

for x in range(start,stop+1):
    print("สูตรคูณแม่ : ",x)
    for i in range(1,13):
        print(x,"x",i,"เท่ากับ",(x*i))