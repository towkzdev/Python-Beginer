#โปรแกรมคำนวน BMI
# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง (m)

#input
weight = int(input("ป้อนน้ำหนักของคุณ(kg) : "))
high = int(input("ป้อนส่วนสูงของคุณ(cm) : "))
#print("BMI = ",weight / (high**2))

#process
high = high/100
bmi = weight / (high**2)

print("BMI = ",bmi)

