def checkbit(n,i):
    if (n>>i)&1==1:
        return True
    else:
        return False
print(format(8,'b'))
print(checkbit(8,3))