def longest_common_prefix(strs):
    shortest=min(strs,key=len)
    res=""
    for i in range(len(shortest)):
        curr=strs[0][i]
        if (all(words[i]==curr for words in strs)): #checks  ith char for all the words in strs 
            res=res+(str(curr))
        else:
            break
    return res
strs=['flower',"fllight","flight"]
print(longest_common_prefix(strs))