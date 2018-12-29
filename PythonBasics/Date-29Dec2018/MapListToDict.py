import operator
first_List = [85,24,36,25]
second_List = [78,45,16,23]
Sum = list(map(operator.add, first_List,second_List))
print(Sum)