#return

def reandomNumber(x):
    if len(x)<3:
        return
    if x == "100":
        print("ถูกหวย")
        return 1000
    else:
        print("ไม่ถูกหวย")
        return 0

money=reandomNumber("500")
print("รางวัล: ",money)