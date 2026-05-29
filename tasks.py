import pickle 
import os 
tasks_file = "tasks.pkl"
tasks_list = []

def load_tasks():
    try:
        with open(tasks_file, "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError, pickle.PickleError):
        return[]    
        
def save_tasks(tasks):
    with open(tasks_file, "wb") as file:
        pickle.dump(tasks_list, file)



def add_task(task):
    tasks_list.append({"task": task, "done": False})
    save_tasks(tasks_list)
    print(f"Task '{task}' added successfully")


def show_tasks(tasks):
    if not tasks:
        print("No tasks added yet")
        return
    for i, t in enumerate(tasks, 1):
        status = '✅' if t['done'] else '❌'
        print(f"{i}. {t['task']} - {status}")



def complete_tasks(index):
    if 0 <= index < len(tasks_list):
        tasks_list[index]["done"] = True
        print(f"Task '{tasks_list[index]['task']}' completed succesfully ✅")
    else:
        print("Invalid task number, please try again")
        save_tasks(tasks_list)

def remove_completed_tasks():
    tasks_list[:] = [t for t in tasks_list if not t["done"]]
    save_tasks(tasks_list)
    print("Completed tasks removed succesfully")


tasks_list = load_tasks()            
























