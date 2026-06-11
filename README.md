# devpulse_cli
DEVPULE: COMMAND-LINE SPRINT AND AGILE TEAM TASK TRACKER
DevPulse is a simple command-line tool built for software development team leaders and managers. It helps teams organize their daily work by managing developers, creating projects, and tracking tasks.

The application is written in clean Python code using Object-Oriented Programming (OOP) principles. It saves all your information to a local file on your computer so you never lose your data.

PROJECT FEATURES (WHAT IT DOES)
This project meets all the requirements for the Module 4 Final Project:

Object-Oriented Design: Uses separate Python classes for Users, Projects, and Tasks with clean relationships.

Local Data Storage: Uses Pythons built-in json module to save and load your data automatically.

Professional CLI: Uses argparse subcommands so you can interact with the application directly from your terminal.

Beautiful Tables: Uses an external package named rich to print clean, color-coded tables in the console.

PROJECT FOLDER STRUCTURE
The project code is divided into different folders and files to keep it organized and reusable:

data/storage.json: The local database file where all information is automatically saved.

models/user.py: Contains the User class (a team member who has projects).

models/project.py: Contains the Project class (a project that has tasks).

models/task.py: Contains the Task class (an individual piece of work that can be completed).

utils/storage_manager.py: Contains the code that handles saving and loading the JSON file.

cli.py: The main script that reads your terminal commands and runs the app.

requirements.txt: Lists the external Python packages needed to run the app.

HOW TO SET UP AND RUN THE APPLICATION
Follow these steps to get the project working on your computer:

Step 1: Install the Required Packages
Open your terminal inside the project folder and run this command to install the rich library:
pip install -r requirements.txt

Step 2: Register a New Team Member (Add User)
Create a profile for a developer on your team by typing:
python cli.py add-user --name Alex

Step 3: Assign a Project to the User (Add Project)
Give that developer a specific project to work on:
python cli.py add-project --user Alex --title CLITool

Step 4: Add a Sprint Task to the Project (Add Task)
Break down the project into smaller tasks:
python cli.py add-task --project CLITool --title ImplementFileSave

Step 5: Mark a Task as Done (Complete Task)
When a developer finishes a task, mark it as complete:
python cli.py complete-task --project CLITool --title ImplementFileSave

Step 6: View the Whole Team Dashboard (List)
See a beautiful, formatted table showing all users, their projects, and their task progress:
python cli.py list

HOW THE DATA PERSISTENCE WORKS
You do not need to manually save your data. Every time you run an add or complete command, the application automatically handles everything:

It opens the data/storage.json file.

It reads any existing team records.

It applies your changes.

It safely rewrites the clean data back to the file using a clean format.
