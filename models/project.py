# Import the Task class from the same directory
from models.task import Task

# Represents a project which can contain multiple tasks (One-to-Many Relationship)
class Project:
    def __init__(self, title, tasks=None):
        # Set the name of the project
        self.title = title
        # If no tasks are provided, initialize an empty list to store them
        self.tasks = tasks if tasks is not None else []

    def add_task(self, task_title):
        # Construct a new instance of a Task object
        new_task = Task(task_title)
        # Append the new task object into the project's task list
        self.tasks.append(new_task)
        return new_task

    def to_dict(self):
        # Converts the project details and all its nested tasks into a dictionary mapping
        return {
            "title": self.title,
            "tasks": [task.to_dict() for task in self.tasks]
        }

    @classmethod
    def from_dict(cls, data):
        # Rebuilds a Project object from structural JSON text dictionary maps
        project = cls(data["title"])
        # Loop through and reconstruct every individual task inside the data package
        project.tasks = [Task.from_dict(t) for t in data["tasks"]]
        return project