#Lamda function

def grtCity(name):
    print(name)
    
'''
lamda argument : expression

'''
x = lambda name:name
sum =lambda x,y : x+y
sum_1 = lambda x,y:x*y


print(sum(5,10))
print(x("Kla"))
print(sum_1(5,10))

result = sum_1(9,10)
print(result)

#x = ตัวเลข
#a = เลขชี้กำลัง

def myPower(x):
    return lambda a:x**a



y=myPower(5) #lambda a:5**a
result = y(2)
print(result)



