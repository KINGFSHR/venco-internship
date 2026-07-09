import datetime

class Task:
    def __init__(self, title, priority, due_date, category, id):
        try:
            duedate = datetime.date(int(due_date.split("-")[2]), int(due_date.split("-")[1]), int(due_date.split("-")[0]))
        except ValueError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY.")
        except IndexError:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY.")
        if priority not in ["Low", "Medium", "High"]:
            raise ValueError("Invalid priority. Please use 'Low', 'Medium', or 'High'.")
        self.title = title
        self.priority = priority
        self.due_date = duedate
        self.category = category
        self.status = False
        self.id = id

    def change_status(self):
        if self.status == False:
            self.status = True
        else:
            self.status = False

    def get_task_info(self):
        return {
            "ID": self.id,
            "Title": self.title,
            "Priority": self.priority,
            "Due Date": self.due_date,
            "Category": self.category,
            "Status": self.status
        }

    def __str__(self):
        output = "ID: " + str(self.id) + "\n"
        output += "Title: " + self.title + "\n"
        output += "Priority: " + self.priority + "\n"
        output += "Due Date: " + str(self.due_date) + "\n"
        output += "Category: " + self.category + "\n"
        if self.status:
            output += "Status: Completed\n"
        else:
            output += "Status: Ongoing\n"
        return output