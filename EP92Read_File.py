#อ่าน Text ไฟล์

#open("ชื่อไฟล์","โหมด","การเข้ารหัส")

try:
    fr=open("EP92.txt","r",encoding="utf-8")
    line = fr.readlines()
    for x in line:
        print(x)
    
    fw=open("EP92.txt","a",encoding="utf-8")
    fw.writelines("สวัสดีชาวโลกจ้า\n")
    
    fw.close()
    fr.close()
except FileNotFoundError:
    print("หาไฟล์ไม่เจอจ้า")