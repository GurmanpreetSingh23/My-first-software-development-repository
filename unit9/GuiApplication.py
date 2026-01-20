import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    # UX Principle: "Forgiveness" & "Error Prevention"
    # We check if the input is empty to prevent bad data.
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)  # Clear the box so they can type again immediately
    else:
        messagebox.showwarning("Warning", "You must enter a task first!")

def delete_task():
    # UX Principle: Handling selection
    try:
        # Get the index of the currently selected item
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        # UX Principle: Feedback
        # If they click delete without selecting anything, tell them why it failed.
        messagebox.showwarning("Warning", "Please select a task to delete.")

# --- 1. SETUP THE MAIN WINDOW ---
root = tk.Tk()
root.title("My Daily Task Manager")
root.geometry("400x450")
root.configure(bg="#f0f0f0") # Light gray background is easier on the eyes

# --- 2. CREATE WIDGETS (The Design) ---

# Title Label
header_label = tk.Label(root, text="To-Do List", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
header_label.pack(pady=10)

# Input Field (Where user types)
task_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
task_entry.pack(pady=5)

# UX Feature: Allow pressing "Enter" key to add task (Efficiency)
task_entry.bind('<Return>', add_task)

# Add Button
add_button = tk.Button(root, text="Add Task", width=20, command=add_task, bg="#4CAF50", fg="white")
add_button.pack(pady=5)

# Listbox with Scrollbar (Essential for Usability if list gets long)
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, width=35, height=10, font=("Helvetica", 12), yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=listbox.yview)

# Delete Button
delete_button = tk.Button(root, text="Delete Selected", width=20, command=delete_task, bg="#FF5733", fg="white")
delete_button.pack(pady=10)

# --- 3. START THE APP ---
root.mainloop()