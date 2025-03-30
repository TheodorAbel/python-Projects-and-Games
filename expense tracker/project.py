import json
import tkinter as tk
from tkinter import messagebox, ttk

def load_expenses():
    """Load expenses from JSON file."""
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    """Save expenses to JSON file."""
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    """Add a new expense."""
    category = category_entry.get()
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid amount!")
        return
    description = description_entry.get()
    
    expenses = load_expenses()
    expenses.append({"category": category, "amount": amount, "description": description})
    save_expenses(expenses)
    
    messagebox.showinfo("Success", "Expense added successfully!")
    update_expense_list()

def update_expense_list():
    """Update the displayed list of expenses."""
    expense_list.delete(*expense_list.get_children())
    expenses = load_expenses()
    for i, exp in enumerate(expenses, 1):
        expense_list.insert("", "end", values=(i, exp['category'], f"${exp['amount']}", exp['description']))

def search_expenses():
    """Search for expenses by keyword."""
    keyword = search_entry.get().lower()
    expenses = load_expenses()
    matches = [exp for exp in expenses if keyword in exp["category"].lower() or keyword in exp["description"].lower()]
    
    expense_list.delete(*expense_list.get_children())
    for i, exp in enumerate(matches, 1):
        expense_list.insert("", "end", values=(i, exp['category'], f"${exp['amount']}", exp['description']))

def edit_expense():
    """Edit the selected expense."""
    selected_item = expense_list.selection()
    if not selected_item:
        messagebox.showerror("Error", "No expense selected!")
        return

    expense = expense_list.item(selected_item, 'values')
    index = int(expense[0]) - 1  # Convert ID to index

    category = category_entry.get()
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid amount!")
        return
    description = description_entry.get()

    expenses = load_expenses()
    expenses[index] = {"category": category, "amount": amount, "description": description}
    save_expenses(expenses)
    
    messagebox.showinfo("Success", "Expense updated successfully!")
    update_expense_list()

def delete_expense():
    """Delete the selected expense."""
    selected_item = expense_list.selection()
    if not selected_item:
        messagebox.showerror("Error", "No expense selected!")
        return

    expense = expense_list.item(selected_item, 'values')
    index = int(expense[0]) - 1  # Convert ID to index

    expenses = load_expenses()
    expenses.pop(index)
    save_expenses(expenses)
    
    messagebox.showinfo("Success", "Expense deleted successfully!")
    update_expense_list()

def main():
    global category_entry, amount_entry, description_entry, search_entry, expense_list
    
    root = tk.Tk()
    root.title("Expense Tracker")
    
    tk.Label(root, text="Category:").grid(row=0, column=0)
    category_entry = tk.Entry(root)
    category_entry.grid(row=0, column=1)
    
    tk.Label(root, text="Amount:").grid(row=1, column=0)
    amount_entry = tk.Entry(root)
    amount_entry.grid(row=1, column=1)
    
    tk.Label(root, text="Description:").grid(row=2, column=0)
    description_entry = tk.Entry(root)
    description_entry.grid(row=2, column=1)
    
    tk.Button(root, text="Add Expense", command=add_expense).grid(row=3, column=0, columnspan=2)
    tk.Button(root, text="Edit Expense", command=edit_expense).grid(row=3, column=2)
    tk.Button(root, text="Delete Expense", command=delete_expense).grid(row=3, column=3)
    
    tk.Label(root, text="Search:").grid(row=4, column=0)
    search_entry = tk.Entry(root)
    search_entry.grid(row=4, column=1)
    
    tk.Button(root, text="Search", command=search_expenses).grid(row=5, column=0, columnspan=2)
    
    columns = ("ID", "Category", "Amount", "Description")
    expense_list = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        expense_list.heading(col, text=col)
    expense_list.grid(row=6, column=0, columnspan=4)
    
    update_expense_list()
    root.mainloop()

if __name__ == "__main__":
    main()
