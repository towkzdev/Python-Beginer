#service programe

PI = 3.14
ROOT = 1.414


def addition(*args):
    total=0
    for i in range(len(args)):
        total+=args[i]
    print("ผลบวก =",total)

def subtraction(num1,num2):
    print("ผลลบ =",(num1-num2))

def power(num1,m):
    print("ผลการยกกำลัง",num1**2)