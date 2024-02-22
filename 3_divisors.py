#given a number n print the number of divisors
import math
def divisors(n):
    count=0
    i=1
    while i<=math.sqrt(n):
        if (n%i==0):
            count+=2
            if i==math.sqrt(n):
                #print(i,end=" ")
                count-=1
        i+=1
    return count
print(divisors(100))
