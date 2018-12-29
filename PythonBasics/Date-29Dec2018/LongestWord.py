num_of_words=int(input("Enter the number of words"))
list=[]
for i in range(num_of_words):
    s=input("Enter the word")
    list.append(s)

print(list)

length=[len(i) for i in list]

print(max(length))

#programt to print to read input from user and print the lenght of max word