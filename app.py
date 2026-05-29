import tkinter as tk
from tkinter import messagebox
from datetime import datetime

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "done": False, "completed_at": None})
        print("Tasks: ", tasks)

        entry.delete(0, tk.END)
        update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task['done'] else "❌"
        completed_at = f" - {task['completed_at']}" if task["completed_at"] else ""
        listbox.insert(tk.END, f"{task['task']} - {status} - {completed_at}")


def show_tasks():
    if tasks:
        for task in tasks:
            update_listbox()
    else:
        messagebox.showwarning("Warning!", "No tasks added yet")        

def on_select(event):
    try:
        task_index = listbox.curselection()[0]
        print(f"Selected task index: {task_index}")
    except IndexError:
        pass

def complete_task():
    try:
        task_index = listbox.curselection()[0]
        print(f"Selected task index: {task_index}")  
        tasks[task_index]["done"] = True
        tasks[task_index]["completed_at"] = datetime.now()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to complete")

def remove_task():
    try:
        task_index = listbox.curselection()[0]
        tasks.pop(task_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove")




root = tk.Tk()
root.title("To-do List Application")
root.geometry("700x700")

label = tk.Label(root, text="Please add your tasks", font=("Arial", 20))
label.pack(pady=20)

entry = tk.Entry(root, width=20, font=("Arial", 20))
entry.pack(pady=20)

add_button = tk.Button(root, text="Add task", command=add_task)
add_button.pack(pady=20)


complete_button = tk.Button(root, text="Complete task", command=complete_task)
complete_button.pack(pady=20)

remove_button = tk.Button(root, text="Remove task", command=remove_task)
remove_button.pack(pady=20)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=20)

root.mainloop()








