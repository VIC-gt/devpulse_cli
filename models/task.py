# Represents a single work item within a project
class Task:
    def __init__(self, title, is_complete=False):
        # Store the title description of the task
        self.title = title
        # Store whether the task is done (defaults to False/Not Done)
        self.is_complete = is_complete

    def mark_complete(self):
        # Change the task status to True when completed
        self.is_complete = True

    def to_dict(self):
        # Formats the task data into a basic Python dictionary for saving to JSON
        return {
            "title": self.title,
            "is_complete": self.is_complete
        }

    @classmethod
    def from_dict(cls, data):
        # Recreates a Task object using saved dictionary data from the JSON file
        return cls(data["title"], data["is_complete"])