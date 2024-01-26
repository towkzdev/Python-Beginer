#Factorial

def factorail(number):
    if number==1:
        return number
    else:
        return number * factorail(number-1)

x=factorail(3)
print(x)
