s=str(input())
rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
print(rev)
#option 2 string slicing 
print(s[::-1])
#option 3 reversed()
print(reversed(s))