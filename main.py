import tasks

def main():
    print("Welcome to the To-Do List Application")
    while True:
        print("\n1. Show all tasks")
        print("2. Add a new task ")
        print("3. Complete a task")
        print("4. Remove completed tasks")
        print("5. Exit")
        
        option = input("Enter a option: ")
        if option == "1":
            print("Showing all tasks")
            for task in tasks.tasks_list:
                print(task)

    
        elif option =="2":
            print("Add new task")
            new_task = input("Enter a new task: ")
            tasks.add_task(new_task)
            
        

        elif option == '3':
            try:
                tasks.show_tasks(tasks.tasks_list)
                task_index = int(input("Enter the number of the task that you want to complete: ")) - 1
                tasks.complete_tasks(task_index)
            except IndexError:
                print("Invalid task number, please try again")
                print("Task completed succesfully")
                


        elif option == "4":
            for task in tasks.tasks_list:
                print(task)

            print("Removing completed tests")
            tasks.remove_completed_tasks()


        elif option == "5":
            print("logging out...")
            break
        
        else:
            print("Invalid option, enter 1, 2, 3, 4 or 5")  
        
        

if __name__ == "__main__":
    main()

