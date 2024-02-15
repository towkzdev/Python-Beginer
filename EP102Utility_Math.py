import math

#ฟังก์ชั่นทางคณิตศาสตร์

x=min(4,3,2,1,23,34,45,6,7)
print(x)

y=max(4,3,2,1,23,34,45,6,7)
print(y)

z=abs(-50) #Absolut
print(z)

a=pow(5,2) #ยกกำลัง
print(a)

c=math.sqrt(64)     #import math
print(c)

score = math.floor(80.4)    #ปัดเศษลง
print(score)

score = math.ceil(80.4)    #ปัดเศษขึ้น
print(score)

#ค่าคงที่
print(math.pi)

#ค่าตรีโกน sin cos tan
convert=math.radians(90) #แปลง radians เป็นองศา
print(convert)
print(math.sin(convert))
print(math.cos(90))
print(math.tan(30))

#ระยะห่างระหว่าจุดสองจุด
point_1=[2,-3]
point_2=[7,-3]

d=math.dist(point_1,point_2)
print(d)

#Log
e=math.log10(1000)
print(e)
f=math.log2(32)
print(f)

