import taskClass
import json

class TaskManager:
    def __init__(self):
        self.tasks = []

    def get_task_by_name(self, name):
        for task in self.tasks:
            if task.title == name:
                return task
        return None
    
    def add_task(self, task):
        self.tasks.append(task)
        print(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        print(task)

    def list_tasks(self, filter):
        for task in self.tasks:
            if filter == "a":
                print(task)
            elif filter == "o" and task.status == "false":
                print(task)
            elif filter == "c" and task.status == "true":
                print(task)
            else:
                print("Invalid choice. Please enter 'a', 'o', or 'c'.")

    def change_task_status(self, task):
        task.change_status()
        print(task)

    def save_tasks_to_file(self, filename, new):
        if not new:
            try:
                with open(filename, "a") as file:
                    json.dump([task.get_task_info() for task in self.tasks], file, default=str)
            except FileNotFoundError:
                print("File not found. Please check the filename and try again.")
        else:
            try:
                with open(filename, "x") as file:
                    json.dump([task.get_task_info() for task in self.tasks], file, default=str)
            except FileNotFoundError:
                print("File not found. Please check the filename and try again.")

    def update_file(self, filename):
        try:
            with open(filename, "w") as file:
                json.dump([task.get_task_info() for task in self.tasks], file, default=str)
        except FileNotFoundError:
            print("File not found. Please check the filename and try again.")

def main():
    task_manager = TaskManager()
    print("New Task Manager")
    menu = "Enter the following options for the corresponding action:\n(o)pen - Open an existing file\n(a)dd - Add a new task\n(r)emove - Remove a task\n(l)ist - List all tasks\n(c)hange status - Change a task's status\n(q)uit - Quit the program"
    print(menu)

    while True:
        user_input = input("Enter an option: ").strip().lower()
        if user_input == "a" or user_input == "add":
            title = input("Enter task title: ")
            priority = input("Enter task priority (Low/Medium/High): ")
            due_date = input("Enter task due date (DD/MM/YYYY): ")
            category = input("Enter task category: ")
            id = 100 + len(task_manager.tasks)
            try:
                new_task = taskClass.Task(title, priority, due_date, category, id)
                task_manager.add_task(new_task)
                user_choice = input("Do you want to save task to a new file? (y/n): ")
                if user_choice == "y":
                    filename = input("Enter new filename to save task (name.json): ")
                    task_manager.save_tasks_to_file(filename, new=True)
                else:
                    filename = input("Enter filename to save task (name.json): ")
                    task_manager.save_tasks_to_file(filename, new=False)
                print("Task added successfully.")
            except ValueError as e:
                print(e)
        elif user_input == "l" or user_input == "list":
            user_choice = input("List all/ongoing/completed tasks? (a/o/c): ")
            task_manager.list_tasks(user_choice)
        elif user_input == "c" or user_input == "change status":
            title = input("Enter the title of the task to change status: ")
            task_to_change = task_manager.get_task_by_name(title)
            if task_to_change:
                task_to_change.change_status()
                print("Task status changed successfully.")
                filename = input("Enter filename to save changes (name.json): ")
                task_manager.update_file(filename)
            else:
                print("Task not found.")
        elif user_input == "r" or user_input == "remove":
            title = input("Enter the title of the task to remove: ")
            task_to_remove = task_manager.get_task_by_name(title)
            if task_to_remove:
                task_manager.remove_task(task_to_remove)
                print("Task removed successfully.")
                filename = input("Enter filename to save changes (name.json): ")
                task_manager.update_file(filename)
            else:
                print("Task not found.")
        elif user_input == "q" or user_input == "quit":
            print("Exiting the program.")
            break


main()