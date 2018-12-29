from functools import reduce

list = [4,2,4]
multiply = reduce((lambda x, y: x * y), list)
print(multiply)

add=reduce((lambda x,y:x+y),list)
print(add)


