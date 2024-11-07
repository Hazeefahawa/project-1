TODoList = [1
]

def AddTask():
    task = input("Enter task: ")
    TODoList.append({"task": task, "completed": False})
    print("Task added successfully")

def ViewTask():
    for index, task in enumerate(TODoList, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['task']} - {status}")
        print()

def MarkAsCompleted():
    ViewTask()
    try:
        index = int(input("Enter the number of task you want to mark as completed: ")) - 1
        TODoList[index]["completed"] = True
        print("Task marked as completed")
    except (ValueError, IndexError):
        print("Invalid input")

def Removetask():
    ViewTask()
    try:
        index = int(input("Enter the number of task you want to remove: ")) - 1
        removed_task = TODoList.pop(index)
        print(f"Task '{removed_task['task']}' removed successfully")
    except (ValueError, IndexError):
        print("Invalid input")  

# Main function 
while True:
    choice = input("Enter your choice: \n1 to add task \n2 to view tasks \n3 to mark task as completed \n4 to remove task \n5 to exit the app\n")
    
    if choice == "1":
        AddTask()
    elif choice == "2":
        ViewTask()
    elif choice == "3":
        MarkAsCompleted()
    elif choice == "4":
        Removetask()
    elif choice == "5":
        print("Exiting To Do List App, Goodbye.")
        break
    else:
        print("Invalid input")
