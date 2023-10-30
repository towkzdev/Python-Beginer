#เจาะลึก String (ตอนที่ 2)

fname = "kla"
lname = "satjaphon"
age = "22"
sarary = 22000

text = "ชื่อต้น :{}\tนามสกุล :{}\tอายุ :{}"
print(text.format(fname,lname,age))

text = "ชื่อต้น :{1}\tนามสกุล :{1}\tอายุ :{2}"
print(text.format(fname,lname,age))

text = "ชื่อต้น :{0}\tนามสกุล :{3}\tอายุ :{2}"
print(text.format(fname,lname,age,"โปรแกรมเมอร์"))

text = "ชื่อต้น :{0}\tนามสกุล :{1}\tอายุ :{2}\tเงินเดือน :{3}"
print(text.format(fname,lname,age,sarary))

