str="Selenium Automation Tool"
words=str.split()
count=0
for word in words:
    print(word.upper())
    count+=1
    if count>1:
        break
