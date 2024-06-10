# Task Manager
A simple task management application that allows users to log in, register new users, add tasks, view tasks, and generate reports. The application is implemented in Python and stores user credentials and tasks in text files.

## Features
  * User login and registration
  * Add tasks
  * View all tasks
  * View tasks assigned to the logged-in user
  * Generate task and user reports
  * Admin-specific options for generating reports and displaying statistics

## Requirements
Python version  3.2 or higher

## Installation
 Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/task-manager.git
Navigate to the project directory:

bash
Copy code
cd task-manager
Ensure you have Python 3.2 or higher installed on your system.

## Usage
Run the script:

bash
Copy code
python task_manager.py
Follow the on-screen prompts to log in, register new users, add tasks, and generate reports.

## File Structure
  *  task_manager.py: The main script for the task manager application.
  *  user.txt: Stores user credentials in the format username, password.
  *  tasks.txt: Stores tasks in the format username, title, description, due_date, date_assigned, completed.
  *  task_overview.txt: Generated report containing an overview of all tasks.
  *  user_overview.txt: Generated report containing an overview of all users and their tasks.
  *  Code Overview
  *  Functions
  *  user_login(file_name)
  *  Reads user credentials from the specified file and returns them as a dictionary.

## login(users)
Prompts the user to log in using a username and password.

## reg_user()
Registers a new user by appending their credentials to the user.txt file.

## add_task()
Adds a new task to the tasks.txt file.

## view_all()
Displays all tasks from the tasks.txt file.

## view_mine(username)
Displays tasks assigned to the logged-in user.

## generate_reports()
Generates reports on tasks and users and saves them to task_overview.txt and user_overview.txt.

## Main Menu
The main menu provides different options based on whether the logged-in user is an admin or a regular user.

# admin login in:
 * user : admin
 * password : adm1n
## Admin options:

  * Register a user
  * Add a task
  * View all tasks
  * View my tasks
  * Generate reports
  * Display statistics
  * Exit
# admin login in: admin passw: adm1n
## Regular user options:

* Add a task
* View all tasks
* View my tasks
* Exit
