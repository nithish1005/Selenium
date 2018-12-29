f=open("file.txt",'r')
line=f.readlines()
for i in range(len(line)-1,0,-1):
    print(line[i])
