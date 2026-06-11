# Import the Project class from the models folder
from models.project import Project

# Represents a team member who owns multiple projects (One-to-Many Relationship)
class User:
    def __init__(self, name, projects=None):
        # Assign the name identifier of the developer user
        self.name = name
        # Initialize an empty list for tracking their assigned project structures
        self.projects = projects if projects is not None else []

    def add_project(self, project_title):
        # Initialize a new Project object instance
        new_project = Project(project_title)
        # Link this new project object directly to this user's project inventory list
        self.projects.append(new_project)
        return new_project

    def to_dict(self):
        # Bundles the user instance data and all their projects into data maps
        return {
            "name": self.name,
            "projects": [project.to_dict() for project in self.projects]
        }

    @classmethod
    def from_dict(cls, data):
        # Restores user records and objects from text data properties saved on disk
        user = cls(data["name"])
        user.projects = [Project.from_dict(p) for p in data["projects"]]
        return user