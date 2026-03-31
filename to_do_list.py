Task = []
CompletedTask = []
IncompletedTask = []
length = len(Task)

def addTask(task):
    global length
    Task.append(task)
    IncompletedTask.append(task)
    length = length + 1
    print("The task is added successfully")

def displayTask():
    j = 1
    for i in Task:
        print(f"{j}. {i}")
        j = j + 1

def Num_Task():
    global length
    print(f"The number of tasks you have are {length}")

def DeleteTask(num):
    global length
    Task.pop(num - 1)
    length = length - 1

def markcom(num):
    global length
    CompletedTask.append(Task[num - 1])
    Task[num -1] == f"{Task[num-1]}(Completed)"
    IncompletedTask.pop(num-1)


def displayIncompletedTasks():
    j = 1
    for i in IncompletedTask:
        print(f"{j}. {i}")
        j = j + 1

while True:
    print("=======To DO LIST=========")
    print("==========MENU============")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Delete Task")
    print("4. Display number of tasks")
    print("5. Mark Complete")
    print("6. Display only incompleted Tasks")
    print("7. Exit")

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        task = input("Enter the task: ")
        addTask(task)
    elif choice == 2:
        displayTask()
    elif choice == 3:
        num = int(input("Enter the task number to delete (start with 1): "))
        if 1 <= num <= len(Task):
            DeleteTask(num)
        else:
            print("Task number does not exist. Please try again")
    elif choice == 4:
        Num_Task()
    elif choice == 5:
        num_completed = int(input("Enter the task number which is completed: "))
        if 1 <= num_completed <= length:
            markcom(num_completed)
        else:
            print("Task number does not exist. Please try again")
    elif choice == 6:
        displayIncompletedTasks()
    elif choice == 7:
        break
    else:
        print("Invalid choice, please try again")