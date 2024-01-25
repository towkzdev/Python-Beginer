#List Parameter

def displayFruit(item):
    for i in range(len(item)):
        print("ผมไม้ชื้นที่",i+1,"=",item[i])

def displayVet(item):
    for i in range(len(item)):
        print("ผักชื้นที่",i+1,"=",item[i])




fruit=["มะม่วง","มะละกอ"]
vet=["ผักกาด","คะน้า"]


displayFruit(fruit)
displayVet(vet)