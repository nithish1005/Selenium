# list=[1,3,4,6,9,2]
# max = max(list)
# ele_index = list.index(max)
#
# print(max)
# print(ele_index)

l=[15,59,43,34,58]

l=[l[i] if l[i]>l[i+1] else "" for i in range(len(l)-1)]
print(l)

# lar=sorted(l)
# print(lar[-1])

