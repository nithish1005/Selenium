from functools import reduce

list = [4,2,21,25,54,4]

max= reduce((lambda x,y:x if x>y else y),list)

print(max)

