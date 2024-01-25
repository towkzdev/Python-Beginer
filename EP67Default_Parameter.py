#Default Parameter

def displayData(fname,lname,city="BKK"):
    print("ชื่อ :",fname)
    print("นามสกุล :",lname)
    print("จังหวัด :",city)
    print("===========================")


displayData("Kla","Satjaphon","Nan")
displayData("Kla","Satjaphon")
displayData(fname="Kla",lname="Satjaphon",city="Nan")
