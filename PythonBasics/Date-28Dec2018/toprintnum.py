f=open("file.txt",'r')
for line in f.readlines():
    s=line.split()
    for i in range(len(s)):
        if s[i].isdigit():
            print(s[i])
