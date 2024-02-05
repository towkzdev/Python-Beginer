#การเขียนลดรูป Exception

try:
    number_1= int(input("Enter number :"))
    number_2=int(input("Enter number :"))
    result = number_1+number_2
    print(result)
except Exception as e:
    print(e)
