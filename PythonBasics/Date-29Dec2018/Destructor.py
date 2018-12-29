class Calendar():
    def __init__(self):
        print("Constrcutor called")
    def __del__(self):
        print("Destructor called")

obj=Calendar()
print("program ended")