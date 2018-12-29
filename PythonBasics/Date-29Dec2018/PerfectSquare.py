import math
ran=int(input("enter the range"))

for i in range(ran):
    n = int(math.sqrt(i))
    if(i == n*n):
        print(i,"perfect Square")
    else:
        print(i,"Not Perfect Square")



#pgm to check for perfect square