#A simple to-do list application that allows the user to add, remove, and view tasks
tasks= []
while True:
    print("What are we doing today?")
    print("1. Add a task")
    print("2. Display tasks")
    print("3. Remove a task")
    print("4. Exit")
    choice= input("Choose an option ")
    if choice== "1":
        while True:
            add_task = input("Add a new task (or 'done' to finish): ")
            if add_task.lower() == 'done':
                break
            tasks.append(add_task)
        print("Tasks added successfully!")
    elif choice== "2":
        print(tasks)
    elif choice== "3":
        remove_task= input("Remove a task: ")
        tasks.remove(remove_task)
        print(f"{remove_task} was removed")
    elif choice== "4":
        print("Exiting To-Do list")
        break