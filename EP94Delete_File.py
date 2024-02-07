#ลบ Text ไฟล์

import os

try:
    if os.path.exists("EP93_test.txt"):
        os.remove("EP93_test.txt")
        print("ลบไฟล์แล้ว")
    else:
        print("ไม่พบไฟล์นี้นะครับ")
except Exception as e:
    print(e)