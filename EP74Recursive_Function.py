#Recursive Function
'''
หาจุดวงช้ำ
หาจุดออก funcetion(return)
ต้องมี Parameter

1-5 โดยไม่ใช้คำสั่ง Loop
'''

def addNumber(number):
    if number==5:
        return
    print(number)
    number+=1
    addNumber(number)

def summation(number):
    if number==1:
        return number
    else:
        return number+summation(number-1)



addNumber(0)
x=summation(5)
print(x)