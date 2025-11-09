"""
Project Management Program
Estimated time to complete: 4 hours
Actual time: 4.5 hours
"""
from project import Project
import datetime

def main():
    """Main function to run the project management program."""
    default_file = "projects.txt"
    projects = load_projects(default_file)
    print(f"Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {default_file}")

    menu = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date  
- (A)dd new project  
- (U)pdate project  
- (Q)uit"""
    print(menu)

    while True:
        choice = input(">>> ").strip().lower()

        if choice == 'l':
            filename = input("Filename to load: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Filename to save: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            # Prompt to save to default file on exit
            save_choice = input(f"Would you like to save to {default_file}? ").strip().lower()
            if save_choice in ['yes', 'y']:
                save_projects(default_file, projects)
                print(f"Saved {len(projects)} projects to {default_file}")
            else:
                print("Not saving to default file.")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")

        print(menu)

class Project:
    """Represents a project with details including name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date  # Expected to be a datetime.date object
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare projects by priority for sorting."""
        return self.priority < other.priority

    def is_completed(self):
        """Check if the project is completed (100% completion)."""
        return self.completion_percentage == 100


def load_projects(filename):
    """Load projects from a tab-delimited file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion))
    return projects


def save_projects(filename, projects):
    """Save a list of Project objects to a tab-delimited file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            date_str = project.start_date.strftime("%d/%m/%Y")
            file.write(f"{project.name}\t{date_str}\t{project.priority}\t{project.cost_estimate}\t"
                       f"{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and completed projects, each sorted by priority."""
    incomplete = [p for p in projects if not p.is_completed()]
    completed = [p for p in projects if p.is_completed()]

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects that start after a user-specified date, sorted by start date."""
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()

    filtered = [p for p in projects if p.start_date > filter_date]
    for project in sorted(filtered, key=lambda x: x.start_date):
        print(project)


def add_new_project():
    """Prompt user for new project details and return a Project object."""
    print("Let's add a new project")
    name = input("Name: ")
    date_str = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, completion)


def update_project(projects):
    """Allow user to update completion percentage and/or priority of a selected project."""
    # Display projects with indices
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = int(input("Project choice: "))
    if 0 <= choice < len(projects):
        project = projects[choice]
        print(project)

        # Update completion percentage
        new_percent = input("New Percentage: ")
        if new_percent:
            project.completion_percentage = int(new_percent)

        # Update priority
        new_priority = input("New Priority: ")
        if new_priority:
            project.priority = int(new_priority)


if __name__ == "__main__":
    main()