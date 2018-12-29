str="Hello, Hi Welcome to Hi"
l=str.split(" ")
d={i:l.count(i) for i in l}
print(d)

# words="Hi This Is Python Hi Is"
# s1=words.split(" ")
# l1=list(s1)
# print(l1)
# count={}.fromkeys(l1,0)
#
# for char in l1:
#     if char in count:
#          count[char]+=1
#
# print(count)