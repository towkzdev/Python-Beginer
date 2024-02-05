#จัดการ Exception หลายเหตุการณ์


try:
    number_1= int(input("Enter number :"))
    number_2=int(input("Enter number :"))
    result = number_1+number_2
    print(result)
except ValueError:
    print("ต้องผ้อนตัวเลขเท่านั้น")
except ZeroDivisionError:
    print("ห้ามหารด้วยเลขศูนย์")
except TypeError:
    print("ชนิดข้อมูลไม่ตรงกัน")



#ValueError => ข้อผิดพลาด
#ZwroDivisionError

