# **kwargs

#*args
def add(*number):
    sum=0
    for i in range(len(number)):
        sum+=number[i]
    print(sum)

def displayData(**kwargs):
    print(kwargs)

displayData(fname="Kla",lanme="Satjaphon",age="23",city="Nan")
displayData(fname="Kla",lanme="Satjaphon",city="Nan")
displayData(fname="Kla",lanme="Satjaphon",age="23")
displayData(lanme="Satjaphon",age="23",city="Nan")