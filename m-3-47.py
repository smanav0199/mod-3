#Write a Python function to calculate the factorial of a number (a nonnegative integer)

num=int(input("enter value here: "))
fact =1
if num>0:
    for i in range(1,num+1):
        fact = fact * i
        print("the factorial of ",num,"is : ",fact)
        i=i-1
        
if num <0:
    print("sorry ,factorial does not exit for negative integer")

elif num == 0:
    print("please enter gerater number ")



