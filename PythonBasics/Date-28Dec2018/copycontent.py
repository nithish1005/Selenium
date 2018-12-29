with open("file.txt") as f:
    with open("file1.txt", "w") as f1:
        for line in f:
            f1.write(line)