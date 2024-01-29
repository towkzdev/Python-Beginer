#ฟังก์ชั่นเช็คจำนวนตัวอักษร

def checkString(message):
    result={"UPPER":0,"LOWER":0}
    for c in message:
        if c.isupper():
            result["UPPER"]=+1
        elif c.islower():
            result["LOWER"]+=1
        else:
            pass
    return result

x=checkString("ASDadasdADAdsf")
print(x)