import argparse
# Load our functional saving and loading file routines
from utils.storage_manager import load_data, save_data
from models.user import User

# Import components from the 'rich' package to display clean terminal visualization layouts
from rich.console import Console
from rich.table import Table

# Initialize the screen writing wrapper engine object from the rich framework
console = Console()

def main():
    # Read our saved system objects from the local JSON storage folder right at the start
    users = load_data()

    # Configure the primary command line input text parser layout engine
    parser = argparse.ArgumentParser(description="DevPulse: Command-Line Sprint & Agile Team Task Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Command Setup: add-user
    user_parser = subparsers.add_parser("add-user", help="Register a brand new team developer profile")
    user_parser.add_argument("--name", required=True, help="The official identifier name of the teammate")

    # Command Setup: add-project
    proj_parser = subparsers.add_parser("add-project", help="Create and map a project to a specific developer profile")
    proj_parser.add_argument("--user", required=True, help="The target developer owner name")
    proj_parser.add_argument("--title", required=True, help="The naming title of the new repository project")

    # Command Setup: add-task
    task_parser = subparsers.add_parser("add-task", help="Inject a sprint feature action task item inside a project")
    task_parser.add_argument("--project", required=True, help="The naming title of the parent project")
    task_parser.add_argument("--title", required=True, help="The description summary of the task")

    # Command Setup: complete-task
    comp_parser = subparsers.add_parser("complete-task", help="Resolve and check off a task item to status finished")
    comp_parser.add_argument("--project", required=True, help="The parent project title container")
    comp_parser.add_argument("--title", required=True, help="The target task description being completed")

    # Command Setup: list
    subparsers.add_parser("list", help="Print a structural grid view display of all system operational history logs")

    # Read and breakdown instructions coming straight from execution console arguments
    args = parser.parse_args()

    # --- CLI LOGIC ROUTINES ---

    if args.command == "add-user":
        # Scan system lists defensively to avoid double duplicate record creation items
        if any(u.name.lower() == args.name.lower() for u in users):
            console.print(f"[bold red]Error:[/bold red] The team developer name '{args.name}' already exists.")
            return
        
        # Instantiate and append user object profiles
        users.append(User(args.name))
        save_data(users)
        console.print(f"[bold green]Success:[/bold green] Created developer profile records for '{args.name}'.")

    elif args.command == "add-project":
        # Search for the developer owner profile matching input conditions
        user = next((u for u in users if u.name.lower() == args.user.lower()), None)
        if not user:
            console.print(f"[bold red]Error:[/bold red] Profile user entity matching '{args.user}' was not found.")
            return
        
        # Create a new project inside the selected user object container layout
        user.add_project(args.title)
        save_data(users)
        console.print(f"[bold green]Success:[/bold green] Associated project tracker '{args.title}' to user account '{user.name}'.")

    elif args.command == "add-task":
        # Find the targeted tracking project across all existing developer profiles
        project = None
        for user_obj in users:
            project = next((p for p in user_obj.projects if p.title.lower() == args.project.lower()), None)
            if project:
                break
        
        if not project:
            console.print(f"[bold red]Error:[/bold red] Target container project title '{args.project}' was not found anywhere.")
            return
        
        # Inject task objects directly inside our found project tracker properties
        project.add_task(args.title)
        save_data(users)
        console.print(f"[bold green]Success:[/bold green] Injected sprint task item '{args.title}' inside project layout framework '{project.title}'.")

    elif args.command == "complete-task":
        # Search the database layout to acquire references to the requested project module
        project = None
        for user_obj in users:
            project = next((p for p in user_obj.projects if p.title.lower() == args.project.lower()), None)
            if project:
                break
            
        if not project:
            console.print(f"[bold red]Error:[/bold red] Target container project title '{args.project}' was not found.")
            return
            
        # Target matching task strings within the assigned active project stack scope
        task = next((t for t in project.tasks if t.title.lower() == args.title.lower()), None)
        if not task:
            console.print(f"[bold red]Error:[/bold red] Task context target description '{args.title}' was not found inside that project scope.")
            return
            
        # Update flag states to declare completion success metrics
        task.mark_complete()
        save_data(users)
        console.print(f"[bold green]Success:[/bold green] Marked assignment status task item '{args.title}' as finished.")

    elif args.command == "list":
        if not users:
            console.print("[yellow]System notification: Local data registers are currently empty.[/yellow]")
            return
            
        # Configure a Rich layout grid component object block for elegant console reading
        table = Table(title="DevPulse Management Sprint Board Database Matrix")
        table.add_column("Assigned Dev Profile", style="cyan", justify="left")
        table.add_column("Active Project Tracks", style="magenta")
        table.add_column("Task Milestone Objectives & Verification Status", style="green")

        # Iterate user arrays loops to paint rows into our screen layout grid
        for user_obj in users:
            if not user_obj.projects:
                table.add_row(user_obj.name, "[dim]No active projects managed[/dim]", "[dim]-[/dim]")
            for proj_obj in user_obj.projects:
                task_accumulation_string = ""
                for task_obj in proj_obj.tasks:
                    # Append status checks next to task entries
                    completion_check_mark = "[bold green]✓ Done[/bold green]" if task_obj.is_complete else "[bold red]✗ Pending[/bold red]"
                    task_accumulation_string += f"• {task_obj.title} ({completion_check_mark})\n"
                
                table.add_row(
                    user_obj.name, 
                    proj_obj.title, 
                    task_accumulation_string.strip() if task_accumulation_string else "[dim]No sprint tasks scheduled[/dim]"
                )
        
        # Output the formatted canvas table component grid structure to the terminal screen layout
        console.print(table)

if __name__ == "__main__":
    main()