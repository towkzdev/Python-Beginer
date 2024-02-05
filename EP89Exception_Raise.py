#สร้าง Exception ด้วย Raise


while True:
    try:
        name = input("ป้้อนชื่อผปผู่ใช้โปรแกรม :")
        number_1= int(input("Enter number :"))
        number_2=int(input("Enter number :"))
        if number_1 == 0 and number_2 == 0:
            break
        if number_2 < 0:
            raise Exception("ไม่สามารถป้อนค่าติดลบได้")
        if name == "kla":
            raise Exception("มีชื่อผู้ใช้แล้ว")
        result = number_1/number_2
        print(result)
    except Exception as e:
        print(e)