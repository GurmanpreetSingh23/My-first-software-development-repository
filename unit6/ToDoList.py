"""
Project: Modular To-Do List Manager

"""

def display_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Exit")

def add_task(todo_list):
    """
    Asks for a task. Checks if user wants to go back.
    """
    print("\n(Type '0' to go back to the menu)")
    print("Or")
    task_name = input("Enter the task description: ")
    
    # --- check user request if he want to go back to menu ---
    if task_name == '0':
        print("Going back to menu...")
        return # This exits the function immediately
    # ---------------------------------------

    task = {"name": task_name, "completed": False}
    todo_list.append(task)
    print(f"Task '{task_name}' added successfully.")

def view_tasks(todo_list):
    print("\n--- YOUR TASKS ---")
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(todo_list):
            status = "[✓]" if task["completed"] else "[ ]"
            print(f"{i + 1}. {status} {task['name']}")

def mark_task_complete(todo_list):
    view_tasks(todo_list)
    if not todo_list:
        return 

    print("\n(Type '0' to go back to the menu)")
    print(" Or ")
    
    try:
        # We take input as a string first to check for '0' easily
        user_input = input("Enter the number of the task to mark as complete: ")
        
        # --- check user request if he want to go back to menu ---
        if user_input == '0':
            print("Going back to menu...")
            return # Exits the function immediately
        # ---------------------------------------

        task_num = int(user_input) # Convert to number for logic
        index = task_num - 1
        
        if 0 <= index < len(todo_list):
            todo_list[index]["completed"] = True
            print(f"Task '{todo_list[index]['name']}' marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")

def main():
    my_tasks = [] 
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task(my_tasks)
        elif choice == '2':
            view_tasks(my_tasks)
        elif choice == '3':
            mark_task_complete(my_tasks)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()