my_tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        task = input("Enter the task: ")
        my_tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(my_tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(my_tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")