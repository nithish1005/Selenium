import itertools

list1=[23,45,65,67,78]
list2=[23,56,77,87,56]
[list1.append(i) for i in list2]
print(sorted(list1))



list3=[23,45,65,67,78]
list4=[23,56,77,87,56]

merged_list=sorted([i for i in itertools.chain(list3,list4)])
print(merged_list)
