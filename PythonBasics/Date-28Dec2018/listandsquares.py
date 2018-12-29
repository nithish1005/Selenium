num=[1,2,3,4,5]
x=list(map(lambda x:x*x,num))
print(x)

l=[(x,x*x) for x in num]
print(l)