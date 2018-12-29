s="Hello World"
l=['a','e','i','o','u']
s1=s.lower()

[print(x) for x in s1 if x in l]



s="hello"

def m1(s):
    return s in l

l1=list(filter(m1,s))
print(list(l1))

