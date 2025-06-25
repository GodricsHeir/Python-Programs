def addTask(taskNo, taskDescription):
    with open('tasks.txt', 'a') as file:
        #check if the task number already exists
        tasks = getTasks()
        for task in tasks:
            if task.startswith(f"{taskNo}:"):
                print(f"Task number {taskNo} already exists. Please use a different number.")
                return
        file.write(f"{taskNo}: {taskDescription}\n")

def getTasks():
    tasks = []
    try:
        with open('tasks.txt', 'r') as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # If the file doesn't exist, return an empty list
    return tasks

def deleteTask(taskNo):
    tasks = getTasks()
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            if not task.startswith(f"{taskNo}:"):
                file.write(task + "\n")

def updateTask(taskNo, newDescription):
    tasks = getTasks()
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            if task.startswith(f"{taskNo}:"):
                file.write(f"{taskNo}: {newDescription}\n")
            else:
                file.write(task + "\n")

def clearTasks():
    with open('tasks.txt', 'w') as file:
        file.write("")  # Clear the file by writing an empty string

def menu():
    print("Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Clear Tasks")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice

choice=menu()
if choice == '1':
    taskNo = input("Enter task number: ")
    taskDescription = input("Enter task description: ")
    addTask(taskNo, taskDescription)
elif choice == '2':
    tasks = getTasks()
    print("Tasks:")
    for task in tasks:
        print(task)
elif choice == '3':
    taskNo = input("Enter task number to delete: ")
    deleteTask(taskNo)
elif choice == '4':
    taskNo = input("Enter task number to update: ")
    newDescription = input("Enter new task description: ")
    updateTask(taskNo, newDescription)
elif choice == '5':
    clearTasks()
elif choice == '6':
    print("Exiting the Task Manager. Goodbye!")
    exit()
else:
    print("Invalid choice. Please try again.")