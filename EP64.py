#ฟังก์ชั่นหาเลขคู่ - เลขคี่

def searchNumber(number):
    if number % 2 == 0:
        print(number,"= เลขคู่")
    else:
        print(number,"= เลขคี่")

a,b,c,d = 12,23,50,40
searchNumber(a)
searchNumber(b)
searchNumber(c)
searchNumber(d)