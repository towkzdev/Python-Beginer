#Try..Except ทำงานร่วมกับ While


while True:
    try:
        number_1= int(input("Enter number :"))
        number_2=int(input("Enter number :"))
        if number_1 == 0 and number_2 == 0:
            break
        result = number_1/number_2
        print(result)
    except ValueError:
        print("ต้องผ้อนตัวเลขเท่านั้น")
    except ZeroDivisionError:
        print("ห้ามหารด้วยเลขศูนย์")
    except TypeError:
        print("ชนิดข้อมูลไม่ตรงกัน")
    finally:
        print("ทำงานต่อไป.......")