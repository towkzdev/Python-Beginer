# โครงสร้างควบคุมแบบเลือก (if..else)
'''
if เงือนไขเป็นจริง:
    statement(คำสั่งดำเนินการ)
if เงื่อนไขเป็นจริง:
    statement(คำสั่งดำเนินการ)
else:
    statement(คำสั่งดำเนินการ)
'''
age = int(input("Enter your Age : ")) #28
if age>=15:
    print("วัยรุ่น")
elif age>=20:
    print("วัยผู้ใหญ่")
elif age>=30:
    print("วัยทำงาน")
else :
    print("วัยเด็ก")

print("จบโปรแกรม")