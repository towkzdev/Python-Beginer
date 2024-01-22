#list,tuple
lis=["สีแดง","สีเหลือง","สีเหลือง"]
tup=("สีแดง","สีเหลือง","สีเหลือง")

#Dictionary => key (การเข้าถึงข้อมูล) , value(ค่าของข้อมูล)
#list,index => index,value

#การสร้าง dictnary
#ชื่อตัวแปร = {key:value,key:value,key:value}

colors={"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว"}
city={"bangkok":"กรุงเทพ"}
animal={"ไก่":"chicken","แมว":"cat","น้องหมา":"dog"}
student={"ก้อง":40,"โจ้":40,"กล้า":40}
room={"นาย A":101,"นาย B":102,"นาย C":103}
print(colors["red"])

#แบบ constructor
animals=dict(cat="แมว",dog="น้องหมา",duck="เป็ด",)
print(animals["cat"])
print(animals.get("cat"))

#แก้ไขข้อมูล
colors[100]="บ้านสวน"
print(colors)

#เพิ่มข้อมูล
colors.update({"blue":"สีน้ำเงิน","orange":"สีส้ม"})
print(colors)

#loop
for item in colors.values():
    print("---",item)

for k,v in colors.items():
    print("key =",k,"Value = ",v)

#การลบข้อมูล
print(colors)
colors.pop("red")
colors.popitem() #ลบตัวหลังสุด
print(colors)

#การคัดลอกข้อมูล
x=colors.copy()
print("X = ",x)

#Net step dict
market={
    "ร้าน A":{
        "name":"ป้าพร",
        "menu":["กะเพราไก่","ก๋วยเตี๋ยว"],
        "zone":"ตะวันออก"
        },
    "ร้าน B":{
        "name":"ลุงป้อม",
        "menu":["มะม่วง","ทุเรียน"],
        "zone":"ทางเข้าตลาด"
        },
    "ร้าน C":{
        "name":"พี่ใจ",
        "menu":["ชานม","น้ำอัดลม"],
        "zone":"ข้าง 7-11"
        }
}
print("----------------",market)
print(market["ร้าน A"]["menu"])


print("ก๋วยเตี๋ยว" in market["ร้าน A"]["menu"])
if "ก๋วยเตี๋ยว" in market["ร้าน A"]["menu"]:
    print(True)
else:
    print(False)

    