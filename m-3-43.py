#Write a Python program to create and display all combinations of letters,
#selecting each letter from a different key in a dictionary. 
#Sample data: {'1': ['a','b'], '2': ['c','d']}

d= {"1": ["a","b"], "2": ["c","d"]}
l=list(d.values())
for j in l[1:]:
    for i in l[0]:
        for x in j:
            print(i+x)

        
