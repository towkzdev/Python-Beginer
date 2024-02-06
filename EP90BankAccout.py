#โปรแกรมบัญชีธนาคาร

#data
accout = {"นาย A":5000,"นาย B":0}

def getbalance():
    print("ยอดเงินคงเหลือในบัญชี :",accout)

def deposit(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("กรุณาป้อนตัวเลข")
    if money<=0:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    print("ฝากเงินเข้าบัญชี :",money)
    accout["นาย A"]+=money

def withdraw(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("กรุณาป้อนตัวเลข")
    if money<=0:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money>accout["นาย A"]:
        raise Exception("ยอดเงินในบัญชีไม่พอ")
    print("ถอนเงินจากบัญชี A :",money)
    accout["นาย A"]-=money

def transfer(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("กรุณาป้อนตัวเลข")
    if money<=0:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money>accout["นาย A"]:
        raise Exception("ยอดเงินในบัญชีไม่พอ")
    print("โอนเงินไปที่บัญชี B :",money)
    accout["นาย B"]+=money
    accout["นาย A"]-=money


try:
    getbalance()
    deposit(5000)
    getbalance()
    withdraw(6000)
    transfer(1000)
    getbalance()
except Exception as e:
    print(e)