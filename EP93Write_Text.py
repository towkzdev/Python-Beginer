#เขียน Text ไฟล์

try:
    fw=open("EP93_test.txt","w",encoding="utf-8")
    for i in range(5):
        name = input("ป้อนข้อความที่ต้องการ :")
        fw.writelines(name+"\n")
    
    fw.close()
except FileNotFoundError:
    print("หาไฟล์ไม่เจอจ้า")
