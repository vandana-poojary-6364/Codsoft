import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks.pop(selected_task_index)
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected!")

def main():
    global task_entry, listbox

    # Create main window
    root = tk.Tk()
    root.title("To-Do List")

    # Set cool background color for the window
    root.configure(bg="#f0f4f8")  # A light, modern grayish-blue color

    # Input field and Add button
    task_entry = tk.Entry(root, width=40)
    task_entry.pack(pady=10)

    add_button = tk.Button(
        root, text="Add Task", bg="#0078D4", fg="white", font=("Helvetica", 10, "bold"), command=add_task
    )
    add_button.pack(pady=5)

    # Listbox to display tasks
    listbox = tk.Listbox(root, width=50, height=15, bg="#ffffff", fg="#333333", font=("Arial", 10))
    listbox.pack(pady=10)

    # Delete button
    delete_button = tk.Button(
        root, text="Delete Task", bg="#E81123", fg="white", font=("Helvetica", 10, "bold"), command=delete_task
    )
    delete_button.pack(pady=5)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()