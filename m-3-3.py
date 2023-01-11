#Write a Python program to count the number of strings where the string 
#length is 2 or more and the first and last character are same from a given list of strings

l=['abc', 'zyz', 'aba', '1221']
r=0
for i in l:
    if len(i)>1 and i[0]==i[-1]:
      r += 1


print(r)
