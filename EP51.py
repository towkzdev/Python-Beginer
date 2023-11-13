#กลุ่มสมาชิกคำทักทาย

'''
Hi , Hello
ก้อง , แก้ม

Hi ก้อง , Hi แก้ม , Hello ก้อง , Hello แก้ม

'''

greeting = ["สวัสดี","Hi","Hello", "Good bye"]
people = ["ก้อง","โจ","แก้ม"]
result=[]
#แบบปกติ
for x in greeting:
    for y in people:
        result.append(x+y)

print("1:",result)

#ลดรูป

result=[x+y for x in greeting for y in people]
print("2:",result)

