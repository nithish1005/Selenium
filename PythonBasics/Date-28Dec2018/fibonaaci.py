# n=int(input("Enter the Number"))
# a,b=0,1
# while n>0:
#       print(a)
#       a,b=b,a+b
#       n-=1

import re
m = re.findall(r'\d', '99Guru1025')
print(m)