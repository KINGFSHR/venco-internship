import taskClass
import json

# Create, Reading (read 1 item, read Entire list), Updating, Deleting, CRUD

class TaskManager:
    def __init__(self, filename):
        self.tasks = []
        self.filename = filename

    def list_task(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        print("No task found with ID " + str(id) + ".")


    def add_task(self, task):
        self.tasks.append(task)

    def load_tasks_from_file(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    task_info = json.loads(line)
                    task = taskClass.Task(
                        title=task_info["Title"],
                        priority=task_info["Priority"],
                        due_date=task_info["Due Date"],
                        category=task_info["Category"],
                        id=task_info["ID"]
                    )
                    if task_info["Status"]:
                        task.change_status()
                    self.tasks.append(task)
            return self.tasks
        except FileNotFoundError:
            print("File not found. Please check the filename and try again.")
        except json.JSONDecodeError:
            print("Error decoding JSON from the file. Please check the file format.")

    def remove_task(self, id):
        task = self.list_task(id)
        if task:
            self.tasks.remove(task)
            print(task)
            print("====== Task removed ======.")


    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(task)

    def change_task_status(self, id):
        task = self.list_task(id)
        if task:
            task.change_status()
            print(task)
            print("====== Task status changed ======.")
        

    def update_file(self):
        with open(self.filename, "a") as file:
            for task in self.tasks:
                json.dump(task.get_task_info(), file, default=str, indent=4)
            

def main():
    print("\n ============ New Task Manager ============ \n")
    while True:
        filename = input("Enter name of save file (name.json): ")
        if not filename[-5:] == ".json":
            print("Invalid filename. Please ensure the filename ends with '.json'.")
        else:
            task_manager = TaskManager(filename)
            with open(filename) as file:
                if file.readline() == "":
                    print("File is empty. Starting with an empty task list.")
                else:
                    task_manager.load_tasks_from_file()
            break

    menu = "Enter the following options for the corresponding action:\n(a)dd - Add a new task\n(r)emove - Remove a task\n(l)ist - List all tasks\n(c)hange status - Change a task's status\n(t)ask - View a specific task\n(q)uit - Quit the program"
    print(menu)


    while True:
        user_input = input("|||||||||| Enter an option: ").strip().lower()
        if user_input == "a" or user_input == "add":
            title = input("Enter task title: ")
            priority = input("\n ======= Enter task priority (Low/Medium/High): ")
            due_date = input("======= Enter task due date (DD-MM-YYYY): ")
            category = input("======= Enter task category: ")
            id = 100 + len(task_manager.tasks)
            try:
                new_task = taskClass.Task(title, priority, due_date, category, id)
                task_manager.add_task(new_task)
                task_manager.update_file()
                print("Task added successfully.")
            except ValueError as e:
                print(e)
        elif user_input == "l" or user_input == "list":
            task_manager.list_all_tasks()
        elif user_input == "c" or user_input == "change status":
            task_id = input("Enter the task ID to change status: ")
            try:
                task_id = int(task_id)
                task_manager.change_task_status(task_id)
                task_manager.update_file()
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif user_input == "r" or user_input == "remove":
            task_id = input("Enter the task ID to remove: ")
            try:
                task_id = int(task_id)
                task_manager.remove_task(task_id)
                task_manager.update_file()
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif user_input == "t" or user_input == "task":
            task_id = input("Enter the task ID to view: ")
            try:
                task_id = int(task_id)
                task = task_manager.list_task(task_id)
                if task:
                    print("\n" + str(task))
            except ValueError:
                print("Invalid ID. Please enter a numeric value.")
        elif user_input == "q" or user_input == "quit":
            print("Exiting the program.")
            break


main()