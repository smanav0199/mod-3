#write a Python program to generate and print a list of first and last 5 
#elements where the values are square of numbers between 1 and 30.

l=list(range(1,6))
l2=[]
for i in l:
	l2.append(i**2)

print("generate 1 to 5 :",l)
print("square of that number :",l2)
