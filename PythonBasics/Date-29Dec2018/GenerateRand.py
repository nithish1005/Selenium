import random as r
n=int(input("Enter how many random number to generated"))
l=[]
for i in range(n):
    l.append(r.randint(1,20))

print(l)