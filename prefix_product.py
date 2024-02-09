def prefix_product(l):
    pref=[1]*len(l)
    pref[0]=l[0]
    for i in range(1,len(l)):
        pref[i]=pref[i-1]*l[i]
    return pref
l=list(map(int,input("enter list: ").strip().split(" ")))
print(f'list: {l}')
print(f'prefix product: {prefix_product(l)}')