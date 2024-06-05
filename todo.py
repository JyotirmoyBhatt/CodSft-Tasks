import itertools

class Task:
    _id_counter = itertools.count(1)

    def __init__(self, title, description):
        self.id = next(self._id_counter)
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def update(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        status = 'Complete' if self.completed else 'Incomplete'
        return f"ID: {self.id}, Title: {self.title}, Description: {self.description}, Status: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def remove_task(self, task_id):
        task = self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)

    def update_task(self, task_id, title, description):
        task = self.find_task_by_id(task_id)
        if task:
            task.update(title, description)

    def mark_task_complete(self, task_id):
        task = self.find_task_by_id(task_id)
        if task:
            task.mark_complete()

    def mark_task_incomplete(self, task_id):
        task = self.find_task_by_id(task_id)
        if task:
            task.mark_incomplete()

    def list_tasks(self):
        return [str(task) for task in self.tasks]

    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add task")
    print("2. Update task")
    print("3. Delete task")
    print("4. Mark task as complete")
    print("5. Mark task as incomplete")
    print("6. List all tasks")
    print("7. Exit")

def main():
    todo_list = ToDoList()
    
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == '2':
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new title: ")
            description = input("Enter new description: ")
            todo_list.update_task(task_id, title, description)
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.remove_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            todo_list.mark_task_complete(task_id)
        elif choice == '5':
            task_id = int(input("Enter task ID to mark as incomplete: "))
            todo_list.mark_task_incomplete(task_id)
        elif choice == '6':
            tasks = todo_list.list_tasks()
            for task in tasks:
                print(task)
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
