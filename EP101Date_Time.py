#Utility Module
#จัดการวันและเวลา

import datetime

result = datetime.datetime.now() #ดึกเวลานะปัจจุบันมาใช้งาน
print(result)
print(result.year)
print(result.month)

newdate = datetime.datetime(2020,6,20)
print(newdate)


#รูปแบบการแสดงผล

print("เริ่มต้น",result)
print("หลัง",result.strftime("%x"))# m/d/y สั้น
print("หลัง",result.strftime("%X"))# time
print("หลัง",result.strftime("%c"))# บอกชื่อวัน เดือน

print(result.strftime("%H:%M:%S %p"))
print(result.strftime("%H:%M:%S %a"))
print(result.strftime("%H:%M:%S %A"))

#1-366

print(result.strftime("%j"))


#date
print(result.strftime("%a"))  # day
print(result.strftime("%A"))  # day
print(result.strftime("%w"))  # 0-sunday 1-monday
print(result.strftime("%d"))  # วันที่
print(result.strftime("%b"))  # เดือน
print(result.strftime("%B"))  # เดือน
print(result.strftime("%d %A %B"))  # เขียนรวมกัน

#ว/ด/ป
print(result.strftime("%d / %m /%Y"))


