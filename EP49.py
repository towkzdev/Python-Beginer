#กลุ่มสมาชิกเลขยกกำลัง

number_1 = [1,2,3,4,5,6,7]
number_2 = [1,2,3,4,5,6,7]

#ปกติ
for i in range(len(number_1)):
    number_1[i]=number_1[i]*number_1[i]
print(number_1)

#ลดรูป
number_2 = [i*i for i in number_2]
print(number_2)