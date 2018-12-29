f=open("file.txt",'r')
count=0
for line in f.readlines():
    count+=1
    if "python" in line.lower():
        print(count)

#line no of a particular word