def bubblesort(a,n): #bubble/ swap away largest element to end position in each iteration
    for i in range(0,n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
def selection_sort(a,n):
    for i in range(0,n-1):
        min_ind=i
        for j in range(i+1,n):
            if  a[j]<a[min_ind]:
                min_ind=j #finidng for index of i'th minimum element
        if min_ind!=i:
            a[i],a[min_ind]=a[min_ind],a[i]
    return a
def insertion_sort(a,n):
    pass

l=list(map(int,input("enter numbers:").strip().split(" ")))
print(f'Bubble sort:{bubblesort(l,len(l))}')
print(f'selection sort:{selection_sort(l,len(l))}')