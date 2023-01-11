#Write a Python program to generate and print a list of first and last 5 
#elements where the values are square of numbers between 1 and 30

l=[]
for i in range(1,31):
    l.append(i*i)

l2=l[:5]+l[-5:]
    

print("list : ",l)
print("list of first and last 5 square of numbers : ",l2)



