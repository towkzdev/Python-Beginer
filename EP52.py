#ค้นหาจำนวนตัวอักษร

message = ["aa","aab","cba","abb","aba","cca","aaa","aac","aaadbca"]
result=[]

for item in message:
    result.append(item.count("a"))
print(result)