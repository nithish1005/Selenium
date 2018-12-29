f=open("file1.txt",'r')
for line in f.readlines():
    s=line.split(" ")
    for i in s:
        print(i.capitalize(),end=" ")