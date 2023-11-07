#สร้างตารางหมากฮอต

for row in range(8):
    for colume in range(8):
        if (colume+row)%2 == 0:
            print("X",end="")
        else:
            print("O",end="")
#   print("X",end="") if (colume+row)%2 == 0 else print("O",end="")
    print("")