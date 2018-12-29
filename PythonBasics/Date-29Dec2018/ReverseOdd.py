s="Python high level language"
words=s.split()
s1=""
#print(s[::-1])
for i in range(len(words)):

    if i%2==0:
        s1+=" "
        s1+=words[i]
    else:
        s1+=" "
        s1+=words[i][::-1]
print(s1)


