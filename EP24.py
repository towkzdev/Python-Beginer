#เกณฑ์คำนวณค่าดัชนีมวลกาย (BMI)
'''
<18 ต่ำกว่าเกณฑ์
18.5 - 22.9 = สมส่วน
23.0 - 24.9 = น้ำหนักเกิน
25.0 - 29.9 = โรคอ้วนระดับที่ 1
>30 = โรคอ้วนระดับอันตราย
'''


weight = int(input("Enter your weight (kg):"))
height = int(input("Enter your height (cm):"))/100
bmi = weight/height**2

if bmi<18.0:
    result="ต่ำกว่าเกณฑ์"
elif bmi>=18.5 and bmi<=22.9:
    result="สมส่วน"
elif bmi>=23.0 and bmi<=24.9:
    result="น้ำหนักเกิน"
elif bmi>=25.0 and bmi<=29.9:
    result="โรคอ้วนระดับที่ 1"
elif bmi>30:
    result="โรคอ้วนระดับอันตราย"
else:
    result = "ไม่ทราบค่าที่ชัดเจน"

print("BMI = ",bmi,"ทำนายว่า",result)
