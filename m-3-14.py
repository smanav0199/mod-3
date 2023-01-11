#Write a Python program to find the second smallest number in a list


a=int(input("enter min range :"))
b=int(input("enter max range : "))
l=[]
sn=[]

for i in range(a,b):
    l.append(i)
    sn.append(i)

print(l)
sn.sort()
print(sn)
print("second smallest number in list : ",sn[1:2])
