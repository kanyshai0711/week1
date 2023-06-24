class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
    
    def update_description(self, new_description):
        self.description = new_description
    
    def __str__(self):
        return f"Task ID: {self.task_id}, Description: {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def create_task(self, task_id, description):
        task = Task(task_id, description)
        self.tasks.append(task)
    
    def read_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    
    def update_task(self, task_id, new_description):
        task = self.read_task(task_id)
        if task:
            task.update_description(new_description)
        else:
            print("Задание не найдено.")
    
    def delete_task(self, task_id):
        task = self.read_task(task_id)
        if task:
            self.tasks.remove(task)
        else:
            print("Задание не найдено.")
    
    def list_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(task)
        else:
            print("Нет заданий.")


task_manager = TaskManager()

task_manager.create_task(1, "Выучить Python")
task_manager.create_task(2, "Закончить проект")
task_manager.create_task(3, "Сходить в спортзал")

task_manager.list_tasks()

task_manager.update_task(2, "Закончить проект до конца недели")

task = task_manager.read_task(2)
print(task)

task_manager.delete_task(3)

task_manager.list_tasks()
