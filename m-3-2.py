#Write a Python function to get the largest number, smallest num and sum 
#of all from a list.

l=[1, 22, 3333, 45, 456]

#print largest number
l.sort(reverse=True)
print(l)
print(l[0])

#print smallest number
l.sort()
print(l[0])

#sum of all from list
total=sum(l)
print(total)
