from datetime import datetime
#  This is where we will be seperating  and splitting the dict/list and remove the newlines

def user_login(file_name):
    with open(file_name,"r") as file:
        lines = file.readlines()
        users = {}
        for line in lines:
            part = line.strip().split(":",1)

            # Split item in part with ", "
            splitted = part[0].split(", ")
            if len(splitted) == 2:
                username, password = splitted
                users[username] = password
        return users
# This is where the user will be able to login
def login(users):
    while True:
        global username
        username = input("Enter username:")
        password = input("Enter password:")
        if username in users.keys() and users[username] == password:
            print("Login succesfull")
            break
        else:
            print("Invalid username or password, try again")
file_name = "user.txt"
users = user_login(file_name)
login(users)        

def reg_user():
    with open("user.txt","a") as file:  
        user_name = input("Enter a new username:")
        with open("user.txt","r") as file_check:
            if any(user_name in line for line in file_check):
                print("username already exists.enter another username.")
                return
            user_password = input("Enter a new password:")
            password_confirm = input("Please confirm password:")
            if user_password != password_confirm:
                print("Password do not match,please make sure that the password is the same:")
                exit()
            file.write(f"\n{user_name}, {user_password}")
            print("user login successfully")

def add_task():
    with open("tasks.txt","a") as file:
            task_user = input("Enter username of the person whom the task is assigned to: ")
            title_task = input("Title of the task: ")
            discr_task = input("The description of the task: ")
            due_date = input("When is this task due(example 06/05/2013)")
            date_assinged = (input("When is this task assigned "))
            file.write(f"\n{task_user}, {title_task}, {discr_task}, {due_date}, {date_assinged}, no")


def view_all():
    with open("tasks.txt","r") as file:
            lines = file.readlines()
            
    print("All tasks:")
    for index, line in enumerate(lines, start=1):
        task = line.strip().split(", ")
            # The code uses sequence unpacking to unpack the first six elements of task into separate variables
        if len(task) >= 6:
            user, title, description, task_assinged, due_date, completed = task[:6]
        print(f"Task {index}:")
        print(f"Username:\t\t{user}")
        print(f"Title:\t\t\t{title}")
        print(f"Description:\t\t{description}")
        print(f"Date Assigned:\t\t{task_assinged}")
        print(f"Due Date:\t\t{due_date}")
        print(f"Completed:\t\t{'yes' if completed == 'yes' else  'no'}")
        print()

def view_mine(username):
    with open("tasks.txt", "r") as file:
        lines = file.readlines()

        tasks_to_display = []
        for idx, line in enumerate(lines, 1):
            task = line.strip().split(", ")
            if task[0] == username:
                tasks_to_display.append((idx, task))

        if not tasks_to_display:
            print("No tasks found for this user.")
        else:
            for idx, task in tasks_to_display:
                print(f"Task Number: {idx}")
                print(f"Username:    {task[0]}")
                print(f"Title:       {task[1]}")
                print(f"Description: {task[2]}")
                print(f"Date Assigned: {task[3]}")
                print(f"Due Date:    {task[4]}")
                print(f"Completed:   {'yes' if task[5] == 'yes' else 'no'}")
                print()

            while True:
                choice = input("Enter task number to mark as complete or edit, or -1 to return to the main menu:")
                if choice == "-1":
                    break
                task_number = int(choice)
                if 1 <= task_number <= len(tasks_to_display):
                    task_idx, task = tasks_to_display[task_number - 1]
                    edit_choice = input("Enter 'c' to mark complete, 'e' to edit: ")
                    if edit_choice.lower() == 'c' and task[5] != "yes":
                        task[5] = "yes"
                        lines[task_idx] = ", ".join(task) + "\n"
                        with open("tasks.txt", "w") as file:
                            file.writelines(lines)
                        print("Task is completely marked and cannot be edited.")
                    elif edit_choice.lower() == 'e':
                        new_user = input("Enter new username: ")
                        new_date = input("Enter new due date (example 06/05/2013):")
                        if new_user:
                            task[0] = new_user
                        if new_date:
                            task[4] = new_date
                        lines[task_idx] = ", ".join(task) + "\n"
                        with open("tasks.txt", "w") as file:
                            file.writelines(lines)
                        print("Task edited.")
                    else:
                        print("Invalid choice.")
                else:
                    print("Invalid task number.")

def generate_reports():
    with open ("tasks.txt","r") as file:
        tasks = file.readlines()

    with open ("user.txt","r") as file:
        users_1 = file.readlines()
    task_total = len(tasks)
    completed_task = sum(1 for task in tasks if task.strip().split(", ")[-1] == "yes")
    uncompleted_task = task_total - completed_task

    today = datetime.now().date()# get the date time to get todays date                                   # (%Y)means 4 numbers to enter the others or for 2 numbers only
    task_overdue = sum(1 for task in tasks if task.strip().split(", ")[-1] == "no" and datetime.strptime(task.strip().split(", ")[4], "%m/%d/%Y").date() < today)

    user_total = len(users_1)
    # creating a new txt file to get an overview of the task
    with open("task_overview.txt","w") as file:
        file.write("Task overview\n")
        file.write(f"total tasks assigned: {task_total}\n")
        file.write(f"Completed task: {completed_task}\n")
        file.write(f"Uncompleted task: {uncompleted_task}\n")
        file.write(f"Overdue task: {task_overdue}") #the number will be rounded to two decimal places and displayed with two digits after the decimal point.
        file.write(f"percentage of incomplete tasks: {(uncompleted_task / task_total) * 100:.2f}%")
        file.write(f"percentage of overdue tasks: {(task_overdue / task_total) * 100:.2f}%")

    with open("user_overview.txt","w") as file:
        file.write("user overview\n")
        file.write(f"total users: {user_total}\n")
        file.write(f"total tasks: {task_total}\n")

        for user in users_1:
            user_task = [task for task in tasks if task.strip().split(", ")[0] == user.strip()]
            total_user_tasks = len(user_task)
            completed_user_tasks = sum(1 for task in user_task if task.strip().split(", ")[-1] == "yes")
            uncompleted_user_task = total_user_tasks - completed_user_tasks
            overdue_user_task =sum(1 for task in user_task if task.strip().split(", ")[-1] == "no" and datetime.striptime(task.strip().split(", ")[4], "%m/%d/%Y")<today)
            # the code at the bottom is to make sure not to get 0 cause you cant divide by zero
            if total_user_tasks != 0:
                completed_percentage = (completed_user_tasks / total_user_tasks) * 100
            else:
                completed_percentage = 0
            if total_user_tasks != 0:
                uncompleted_percent = (uncompleted_user_task / total_user_tasks) * 100
            else:
                uncompleted_percent = 0
            if total_user_tasks != 0:
                overdue_percent = (overdue_user_task / total_user_tasks) * 100
            else:
                overdue_percent = 0
            file.write(f"user: {user.strip()}\n")
            file.write(f"total tasks assigned: {total_user_tasks}\n")
            file.write(f"percentage of total tasks: {(total_user_tasks/ task_total)* 100:.2f}%\n")
            file.write(f"percentage of completed task: {(completed_percentage)* 100:.2f}%\n")
            file.write(f"percentage of task to be complete: {(uncompleted_percent) * 100:.2f}%")
            file.write(f"percentage of overdue tasks: {(overdue_percent) * 100:.2f}%")
    print("reports generated")


# This is where the user wil have option to choose. 
while True:
    #admin menu
    if username == 'admin':
        menu = input ('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    gn - generate reports
    ds - display statistics                                                 
    e - exit
    : ''').lower()
    else:         
        menu = input('''Select one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks                                 
    e - exit
    : ''').lower()    
# If user chooses 'r' this will then let the user register a new name and password. 
    if menu == 'r' and username == "admin":
        reg_user()


# If user chooses 'a' it will let the user add a task to the file(tasks.txt). 
    elif menu == 'a':
        add_task()
        

    # If user chooses 'va' it will then view all task. 
    elif menu == 'va':
        view_all()
    # If user choose vm it will then only view my task for the user.
    elif menu == 'vm':
        view_mine(username)

    elif menu == 'gn'and username == "admin":
        generate_reports()


    elif menu == 'ds'and username == "admin":  
        # Creating an empty list and append.      
        with open("user.txt", "r") as file:
            count = 0
            for line in file:
                count += 1
        print(f"The number of users is: {count}")
        with open("tasks.txt", "r") as file:
            line_count = 0
            for line in file:
                line_count += 1
        print(f"The number of tasks in the file is: {line_count}")

    #If user choose e it just exits the program.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have entered an invalid input. Please try again")