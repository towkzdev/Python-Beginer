#ฟีโบนัชชี (Fibonacci)

#0,1,1,2,3,5,8.,...
#f0=? , f1=?

def fibonacci(number):
    if number<=1:
        return number# 2 ลำดับแรก
    else:
        return fibonacci(number-1) + fibonacci(number-2) #เลขลำดับถัดไป

for i in range(10):
    print(fibonacci(i))



'''
i = 0
i = 1
i = 2
i = 3
i = 4

0,1,9,9,9
'''

#fibonacci
'''
i = 0
i = 1
i = 2
i = 3
i = 4

0,1,fibonacci(number-1) + fibonacci(number-2)
0,1,1,
'''