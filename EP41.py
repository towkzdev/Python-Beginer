#เกมทายเลขลูกเต๋า
#1,2,3,4,5,6

import random

myrandom = random.randrange(1,7)
#print(myrandom)
k=1
correct=False
print("คุณมีโอกาส 3 ครั้ง \n")

while True:
    number=int(input("ป้อนคำตอบของคุณ :"))
    correct =(number==myrandom)
    
    if not correct:
        if(number>myrandom):
            print("น้อยกว่า")
        if(number<myrandom):
            print("มากกว่า")
            
    if correct:
        print("ตอบถูก")
        break
    
    if number<0 or k==3:
        break
    
    k+=1

if not correct:
    print("ตอบผิด ทำไมโง่จัง!")
    print("เฉลย :",myrandom)