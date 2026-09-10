tasks = [] #Empty lists to store tasks

#Function to display the menu options
def show_menu():
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

#Function to add a task to the list
def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" added.')

#Function to view the tasks in the list
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
        return
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['task']}")

#Function to mark a task as completed
def mark_completed():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

#Function to remove a task from the list
def remove_task():      
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            print(f'Task "{removed_task["task"]}" removed.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

#Main function to run the To-Do List application
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exiting the To-Do List application.")
        break
    else:
        print("Invalid choice. Please select a valid option.")