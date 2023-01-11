#Write a Python function that takes two lists and returns true if they have at least one common member.

l1=[1,2,3,44,5,6,True,10]
l2=[1,13,14,44,6,45]

for x in l1:
    for y in l2:
        if x==y:
            print("true")
