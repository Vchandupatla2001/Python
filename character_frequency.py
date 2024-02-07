s=str(input())
chars={}
for i in s:
    if i in chars:
        chars[i]=chars[i]+1
    else:
        chars[i]=1
#printing the character frequency in order of occurance
dup=chars.copy() #create dupliacte of chars
print("Print character frequency in order of occurance ")
for j in s:
    if chars[j]!=0:
        print(j+str(chars[j]),end="")
        chars[j]=0
print("\n")
#sort the map with values as key
res={k:v for k,v in sorted(dup.items(),key=lambda items:items[1])}
print("Print character frequency in ascending order ")
for i in res.keys():
    print(i+str(res[i]),end="")