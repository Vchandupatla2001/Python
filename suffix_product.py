def suffix_product(l,n):
    suff=[1]*n
    suff[-1]=l[-1] # initialise last index of suffix array
    for i in range(n-2,-1,-1): # iterate from right to left start from (n-1) t0
        #print(i)
        suff[i]=suff[i+1]*l[i]
    return suff
l=list(map(int, input("enter list: ").strip().split(" ")))
print(f'list: {l}')
print(f'suffix product: {suffix_product(l,len(l))}')