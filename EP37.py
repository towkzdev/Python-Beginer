#ตัวเลขขั้นบันได

last=int(input("Enter number :"))#input = 5
for row in range(1,last+1):#row = 1,5
    for colume in range(1,row+1):#colume = 1,5
        print(colume,end='')#row1=1 , row2=12
    print("")
#print(row)
#print(colume)
'''
Case sample
input = 3

row1 = 1,3
colume 1,2
1

row2
colume 1,3
12

row3
colume 1,4
123

'''