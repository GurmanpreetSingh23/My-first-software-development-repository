import tkinter as tk
from tkinter import ttk, messagebox

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Budget App")
        self.root.geometry("400x550")

        self.current_balance = 0.0
        
        self.setup_gui()

    def setup_gui(self):
        # 1. Top Section - Balance
        top_frame = tk.Frame(self.root, pady=10)
        top_frame.pack()

        tk.Label(top_frame, text="My Balance").pack()
        
        self.balance_label = tk.Label(top_frame, text="£0.00", font=("Arial", 24, "bold"), fg="blue")
        self.balance_label.pack()

        # 2. Middle Section - Inputs (Money)
        input_frame = tk.Frame(self.root, pady=10, padx=10)
        input_frame.pack(fill=tk.X)

        tk.Label(input_frame, text="Item Name:").pack(anchor="w")
        self.item_entry = tk.Entry(input_frame)
        self.item_entry.pack(fill=tk.X)

        tk.Label(input_frame, text="Cost/Amount (£):").pack(anchor="w")
        self.amount_entry = tk.Entry(input_frame)
        self.amount_entry.pack(fill=tk.X)

        tk.Label(input_frame, text="Type:").pack(anchor="w")
        self.type_var = tk.StringVar()
        
        # Dropdown box to choose Expense or Income
        self.type_box = ttk.Combobox(input_frame, textvariable=self.type_var, state="readonly")
        self.type_box['values'] = ("Expense", "Income")
        self.type_box.current(0)
        self.type_box.pack(fill=tk.X, pady=5)

        # Buttons
        tk.Button(input_frame, text="Add Item", bg="green", fg="white", command=self.add_item).pack(fill=tk.X, pady=5)
        tk.Button(input_frame, text="Reset", bg="orange", command=self.reset_app).pack(fill=tk.X)

        # 3. Bottom Section - List
        tk.Label(self.root, text="Transaction History", font=("Arial", 12, "bold")).pack(pady=5)
        
        # Using a simple Listbox is easier than a Table
        self.history_list = tk.Listbox(self.root, height=10)
        self.history_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def add_item(self):
        name = self.item_entry.get()
        cost = self.amount_entry.get()
        trans_type = self.type_var.get()

        # Simple check to make sure they typed something
        if name == "" or cost == "":
            messagebox.showwarning("Error", "Please fill in all boxes")
            return

        # Check if the cost is a number
        try:
            cost_value = float(cost)
        except:
            messagebox.showerror("Error", "Amount must be a number")
            return

        # Calculate new balance and add to list
        if trans_type == "Expense":
            self.current_balance -= cost_value
            # Create a string like: "Book : -£20.0 (Expense)"
            display_text = f"{name} : -£{cost_value} (Expense)"
            self.history_list.insert(0, display_text) # Add to top
            self.history_list.itemconfig(0, {'fg': 'red'}) # Color it red
        else:
            self.current_balance += cost_value
            display_text = f"{name} : +£{cost_value} (Income)"
            self.history_list.insert(0, display_text)
            self.history_list.itemconfig(0, {'fg': 'green'}) # Color it green

        # Update the big number at the top
        self.balance_label.config(text=f"£{self.current_balance:.2f}")
        
        # Clear the boxes so we can type again
        self.item_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def reset_app(self):
        # Clear everything
        self.current_balance = 0.0
        self.balance_label.config(text="£0.00")
        self.history_list.delete(0, tk.END)

# Start the program
root = tk.Tk()
app = BudgetApp(root)
root.mainloop()