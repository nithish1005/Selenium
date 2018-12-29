s="Python Is High Level Language"
vowels=set("aeiouAEIOU")
count=0
for char in s:
    if char in vowels:
        count+=1
print("Vowels Count ",count)