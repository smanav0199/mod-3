#Write a Python function that takes a list and returns a new list with unique elements of the first list.


l=[1,2,3,23,4,5,2,3,44,45,77]
s2=[]
for i in l:
    if i not in s2:
        s2.append(i)
print(s2)
                
