tasks = []

# To do list tasks

def add_task(new_task):
    tasks.append(new_task)
    print(f"Added task; {new_task}")

def show_tasks():
    print("\n--- Task list ---")
    if not tasks:
        print("There are no pending tasks.")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    print("------------")

def delete_task(index):
    if not tasks:
        print("There are no tasks to delete.")
        return
    else:
        real_index = index -1

        if 0 <= real_index < len(tasks):
            removed_task = tasks.pop(real_index)
            print(f"\nTask {removed_task} deleted.")
        else:
            print(f"\n Error. The index {index} is out of range.")

def update_task(index, name):
    if not tasks:
        print("There are no tasks to update.")
        return
    real_index = index -1

    if 0 <= real_index < len(tasks):
        old_task = tasks[real_index]
        tasks[real_index] = name
        print(f"\nTask '{old_task}' updated to '{name}'.")
    else:
        print(f"Error. The index {index} is out of range.")

def main():
    while True:
        print("\n--- Task Manager ---")
        print("1. View task")
        print("2. Added task")
        print("3. Delete task")
        print("4. Update task")
        print("5. Exit")
        option = input("Select an option (1-5): ")

        if option == '1':
            show_tasks()
        elif option == '2':
            new_task = input("Enter a task: ")
            add_task(new_task)
        elif option == '3':
            index = int(input("Enter index task: "))
            delete_task(index)
        elif option == '4':
            index = int(input("Enter index task: "))
            name = input("Enter a new name: ")
            update_task(index, name)
        elif option == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

main()