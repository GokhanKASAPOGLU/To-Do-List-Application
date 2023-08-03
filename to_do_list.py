import os

# Create an empty To-Do list
to_do_list = []

# Function to load existing data from a file
def load_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            for line in file:
                task = line.strip()
                to_do_list.append(task)
        print("Existing data loaded successfully.")
    except FileNotFoundError:
        print("\nNo existing to_do_list.txt file found. Creating a new one.")

# Function to add user input tasks to the list
def add_task(to_do_list):
    task = input("Enter the task to be done: ")
    to_do_list.append(task)
    print("Task successfully added.")

# Function to show tasks in the list
def show_tasks(to_do_list):
    print("To-Do Tasks:")
    for task in to_do_list:
        print("- " + task)

# Function to delete a task from the list
def delete_task(to_do_list):
    task = input("Enter the task you want to delete: ")
    if task in to_do_list:
        to_do_list.remove(task)
        print("Task successfully deleted.")
    else:
        print("Task not found.")

# Function to save the To-Do list to a file
def save_to_file(to_do_list, file_path):
    with open(file_path, "w") as file:
        for task in to_do_list:
            file.write(task + "\n")

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "to_do_list.txt")

# Load existing data from the file
load_from_file(file_path)

# Main loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Save To-Do List")
    print("5. Exit")
    choice = input("Your choice (1/2/3/4/5): ")
    
    if choice == "1":
        add_task(to_do_list)
    elif choice == "2":
        show_tasks(to_do_list)
    elif choice == "3":
        delete_task(to_do_list)
    elif choice == "4":
        save_to_file(to_do_list, file_path)
        print("To-Do List successfully saved to the file.")
    elif choice == "5":
        print("Exiting the application...")
        break
    else:
        print("Invalid choice. Please try again.")
