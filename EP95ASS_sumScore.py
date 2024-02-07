#โปรแกรมคำนวณเกรดนักเรียน

try:
    #fw=open("score.txt","w",encoding="utf-8")
    #while True:
    #   studentId=input("ป้อนจ้อมูลนักเรียน :",)
    #   if studentId == "x":
    #       break
    #    fw.writelines(studentId+"\t"+score+"\n")
    #fw.close()
    
    fr=open("score.txt","r",encoding="utf-8")
    fw=open("grade.txt","w",encoding="utf-8")
    grade=None
    for line in fr.readlines():
        score = line[-4:].strip()   #คะแนน
        studentId=line[:-4].strip() #รหัสนักเรียน
        #print("รหัสนักเรียน:",studentId,"คะแนน :",score)
        score=int(score)
        if score>=80:
            grade = "A"
        elif score >=70 and score<80:
            grade = "B"
        elif score >=50 and score<=69:
            grade = "C"
        else:
            grade = "F"
            
        #print("รหัสนักเรียน:",studentId,"คะแนน :",score,"เกรด :",grade)
        fw.writelines(studentId+"\t"+str(score)+"\t"+grade+"\n")
    fw.close()
except Exception as e:
    print(e)
