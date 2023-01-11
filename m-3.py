#Write a Python program to create a dictionary from a string. 
#Note: Track the count of the letters from the string. Sample string: 'w3resource'

s="w3resource"
d = {}
for i in s:
    if i in d:
        d[i] +=1
    else:
        d[i] =1

print(d,':',d[i])
