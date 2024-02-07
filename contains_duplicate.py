
#given a list of numbers, return true if a number repates atleast once else false
def contains_duplicate(nums):
    exist=set()
    for i in nums:
        if i in exist:
            return True
        exist.add(i)
    return False #no duplicate found in nums
nums=list(map(int,input().strip().split(" ")))
print(contains_duplicate(nums))