s="Welcome to Selenium Automation"
count=0
for i in s:
    if i.islower():
        print(i,end=" ")
        count+=1
print(count)