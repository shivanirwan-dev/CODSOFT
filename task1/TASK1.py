# TO-DO LIST
Tasks=[]
while True:
    print("---- TO DO LIST-----")
    print("1. Add Task")
    print("2.View Task")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        task = input("Enter your task:")
        Tasks.append(task)
    elif choice == 2:
        if len(Tasks) == 0:
            print("You have no tasks")
        else:
            print(" Your tasks are ")
            for i in range(len(Tasks)):
                print(i+1,"-->",Tasks[i])
    elif choice == 3:
        if len(Tasks)==0:
            print("You have no tasks to remove")
        else:
            for i in range(len[Tasks]):
                print(i+1,"-->",Tasks[i])
            num = int(input("Enter the number of the task to remove: "))  # take the number of task to remove
            if 1<= num <= len[Tasks]:
                Tasks.pop(num-1)
                print("Your task removed sucessfully")
            else:
                print("Invalid task number!")
    elif choice == 4:
        print("Existing the program")
        break
    else:
        print("Invalid choice. Try again Please")



