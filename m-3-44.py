#Write a Python program to find the highest 3 values in a dictionary



s={1:25,2:30,3:45,4:44,5:50}
d=list(s.values())
n=d.sort(reverse=True)
print(d)
print("max high 3 value: ",d[0:3])
