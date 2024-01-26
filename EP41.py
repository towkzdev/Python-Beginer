#เกมทายเลขลูกเต๋า
#1,2,3,4,5,6

import random

myrandom = random.randrange(1,10)
#print(myrandom)
k=1
correct=False
print("คุณมีโอกาส 3 ครั้ง \n")

while True:
    number=str(input("ป้อนคำตอบของคุณ :"))
    correct =(number==myrandom)
    
    if not correct:
        if(number>myrandom):
            print("****")
        if(number<myrandom):
            print("****")
            
    if correct:
        print("ตอบถูก")
        break
    
    if number<0 or k==3:
        break
    
    k+=1

if not correct:
    print("ตอบผิด ทำไมโง่จัง!")
    print("เฉลย :",myrandom)