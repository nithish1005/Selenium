# num=int(input("enter the range"))
#
# l=[i for i in range(num) if i%2!=0 if i%3!=0 if i%5!=0]
# print(l)

# for i in range(num):
#     if i%2!=0:
#         if i%3!=0:
#             if i%5!=0:
#                 print(i)

for i in range(10):
    if i%2==0:
        continue
    elif i%3==0:
        continue
    elif i%5==0:
        continue
    else :
        print(i)

# num = 10
# l=[]
# for i in range(num):
#     for j in range(2,6):
#         if (i % j) == 0:
#             print("It's a not a prime",i)
#             break
#         else:
#             if i not in l:
#                 l.append(i)
# print(l)