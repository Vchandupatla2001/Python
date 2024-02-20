def checkbit(n,i):
    if (n>>i)&1==1:
        return True
    else:
        return False
def count_set_bits(n):
    count=0
    for i in range(0,32):
        if (checkbit(n,i))==True:
            count+=1
    return count
print(count_set_bits(31))
print(format(-31,'b'))
