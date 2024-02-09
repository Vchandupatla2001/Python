def product_except_self(l,n):
    pref=[1]*n 
    suff=[1]*n
    res=[1]*n
    for i in range(1,n):
        pref[i]=pref[i-1]*l[i-1] # insted if multiplying pref[i]=pref[i-1]*l[i] we multiply with l[i-1] 
        #as we want to avoid multiplying curr element
    for i in range(n-2,-1,-1):
        suff[i]=suff[i+1]*l[i+1]# insted if multiplying suff[i]=suff[i+1]*l[i] we multiply with l[i+1] 
        #as we want to avoid multiplying curr element
    for i in range(0,n):
        res[i]=suff[i]*pref[i]
    return res
l=list(map(int,input("enter list ").strip().split(" ")))
print(l)
print(product_except_self(l,len(l)))