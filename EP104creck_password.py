#โปรแกรม Crack รหัสผ่าน
#รหัสผ่าน ATM=132

import random

atm_Password="Gr19"
result="" #เก็บผลลัพย์
while result!=atm_Password:
    result=""
    for letter in range(len(atm_Password)):
        list_Number=random.choice("0123456789Gr")
        result="".join(list_Number)+str(result)
        print("SERACH :",result)
print("CRACK PASSWORD ATM",result)