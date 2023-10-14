#การใช้ And Or Not

age = int(input("Enter your Age : "))
#and
#15 - 20 =>วัยรุ่น
#21 - 29 =>วัยผู้ใหญ่
#30 - 39 =>วัยทำงาน
if age>=15 and age<=20:
    print("วัยรุ่น")
elif age>=21 and age<=29:
    print("วัยผู้ใหญ่")
elif age>=30 and age<=39:
    print("วัยทำงาน")
elif age>=80:
    print("วัยชรา")
else:
    print("วัยเด็ก")
    
#or
if age>=15 or age<=20:
    print("วัยรุ่น")
else:
    print("วัยเด็ก")

#not
if not age>=15:
    print("วัยรุ่น")
else:
    print("วัยเด็ก")