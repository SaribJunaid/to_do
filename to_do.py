class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"'{task}' has been added to your list.")

    def mark_done(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"'{task}' has been marked as completed.")
        else:
            print(f"'{task}' is not in the task list.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in your list.")
        else:
            print("Here are your tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"'{task}' has been deleted.")
        else:
            print(f"'{task}' not found.")

my_list = ToDo()

my_list.add_task("Buy groceries")
my_list.add_task("Finish assignment")

my_list.view_tasks()

my_list.mark_done("Buy groceries")
my_list.view_tasks()

my_list.delete_task("Finish assignment")
my_list.view_tasks()


