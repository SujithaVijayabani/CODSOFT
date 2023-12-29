class Task:
    def __init__(self, name, status="Incomplete", due_date=None):
        self.name = name
        self.status = status
        self.due_date = due_date


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task_status(self, task_name, new_status):
        for task in self.tasks:
            if task.name == task_name:
                task.status = new_status
                return True
        return False

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the To-Do List.")
        else:
            for task in self.tasks:
                print(f"{task.name} - Status: {task.status}")
        

def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Update Task Status")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            due_date = input("Enter due date (optional): ")
            new_task = Task(task_name, due_date=due_date)
            todo_list.add_task(new_task)
            print("Task added successfully!")

        elif choice == "2":
            task_name = input("Enter task name: ")
            new_status = input("Enter new status (Incomplete/Complete): ")
            if todo_list.update_task_status(task_name, new_status):
                print("Task status updated successfully!")
            else:
                print("Task not found!")

        elif choice == "3":
            todo_list.display_tasks()

        elif choice == "4":
            print("Exiting the To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
