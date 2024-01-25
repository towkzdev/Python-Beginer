#Arbitrary Arguments (args)

def add(a,b):
    print(a+b)

def sumTree(a,b,z):
    print(a+b+z)

def sumFour(a,b,z,x):
    print(a+b+z+x)

add(10,20)
sumTree(10,20,30)
sumFour(10,14,23,45)

print("==========================")
#*args

def Add(*agrs):
    sum=0
    for item in agrs:
        sum+=item
    print(sum)

Add(10,20)
