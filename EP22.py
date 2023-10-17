#โปรแกรมแยกธนบัตร

'''
2000 => 1000 = 2 ใบ
1500 => 1000 = 1 , 500 = 1 ใบ
1800 => 1000 = 1 , 500 = 1 , 100 = 3 ใบ
100 => 50 = 2 ใบ
'''
number = int(input("Enter your money : "))

#1000THB
if number >= 1000:
    print("1000 บาท = ",(number//1000),"ใบ")
    number %= 1000

#500THB
if number >= 500:
    print("500 บาท = ",(number//500),"ใบ")
    number = number % 500

#500THB
if number >= 100:
    print("100 บาท = ",(number//100),"ใบ")
    number %= 100

#100THB
if number >= 50:
    print("50 บาท = ",(number//50),"ใบ")
    number %= 50

#20THB
if number >= 20:
    print("20 บาท = ",(number//20),"ใบ")
    number %= 20
