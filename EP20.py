#โปรแกรมเปรียบเทียบตัวเลข

a=int(input("Enter number 1 :"))
b=int(input("Enter number 2 :"))

if a>b :
    print(str(a)+ " มากกว่า " + str(b))
elif a==b:
    print(str(a)+ " เท่ากับ " + str(b))
else :
    print(str(b)+ " มากกว่า " + str(a))