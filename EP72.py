#ฟังก์ชั่นเรียกฟังก์ชั่น

def compareMax(x,y):
    if x>y:
        return x
    else:
        return y

def equal(x,y,z):
    #ฟังก์ชันเรียกใช้ฟังก์ชัน
    return compareMax(compareMax(x,y),z)
    '''
    a=compareMax(x,y)
    z=compareMax(a,z)
    return z
    '''

max_1=compareMax(10,45)
print("ค่ามากที่สุด: ",max_1)


max_2=equal(10,45,63)
print("ค่ามากที่สุด: ",max_2)