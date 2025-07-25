class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Pending"  # Default status is Pending
    def mark_as_completed(self):
        self.status = "Completed"
    def __str__(self):
        return f"Task: {self.title}, Description: {self.description}, Due Date: {self.due_date}, Status: {self.status}"


class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                return f"Task '{title}' marked as completed."
        return f"Task '{title}' not found."
    def list_all_tasks(self):
        return [str(task) for task in self.tasks]
    def display_incomplete_tasks(self):
        return [str(task) for task in self.tasks if task.status == "Pending"]


def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. List All Tasks")
        print("4. Display Incomplete Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date: ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)
            print(f"Task '{title}' added successfully.")
        elif choice == '2':
            title = input("Enter the title of the task to mark as completed: ")
            result = todo_list.mark_task_completed(title)
            print(result)
        elif choice == '3':
            tasks = todo_list.list_all_tasks()
            if tasks:
                print("\nAll Tasks:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks available.")
        elif choice == '4':
            incomplete_tasks = todo_list.display_incomplete_tasks()
            if incomplete_tasks:
                print("\nIncomplete Tasks:")
                for task in incomplete_tasks:
                    print(task)
            else:
                print("No incomplete tasks available.")
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()


Define Post Class:
Create a Post class with attributes like title, content, and author.
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}\nContent: {self.content}"
