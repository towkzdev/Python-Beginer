#เขียน Text ไฟล์

try:
    fw=open("EP93_test.txt","w",encoding="utf-8")
    fw.write("Hello World\n")
    fw.write("ดีจ้า")
    fw.close
except FileNotFoundError:
    print("หาไฟล์ไม่เจอจ้า")
