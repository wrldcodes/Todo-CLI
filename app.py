tasks = []

def add_task():
    task = input("Enter task:  ")
    tasks.append(task)


def view_task():
    if tasks == 0:
        print("no todo yet my ni$$a")
    else:
        for task in tasks:
            print(task)  



def delete_task():
    print(f"{tasks}")
    index = int(input("Enter your task number ski: ")) - 1
    remove_task = input("Delete task: ")
    for task in tasks:
        if task.upper() == remove_task().upper:
            tasks.remove(task)
            found = True
            print("Deleted successfully")
            break
    
    if not found: 
            print("todo not found in list of todos")    


def update_task():
    index = int(input("Enter your task number ski: ")) - 1
    edit_task = input("Edit your task chief: ")
    tasks[index] = edit_task



def exit():
    tasks.clear()
    print("Exited successfully")



def show_menu():
    print("\n=========== TODO LIST =========")
    print ("1. Add Task")
    print ("2. View Task")
    print ("3. Edit Task")
    print ("4. Delete Task")

#infinite loop for the app to keep running
def main_app():
    while True:
        show_menu()

        choice = input("Choose from option what you wanna do my nigga: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            update_task()    
        elif choice == "4":
            delete_task()

        else:
            print("invalid option naa you no dey see the option well")


main_app()