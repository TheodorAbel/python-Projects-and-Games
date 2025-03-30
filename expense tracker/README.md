# Expense Tracker Application

## 🌟 **Overview**

Welcome to the **Expense Tracker Application**! This project is built using **Python** and the **Tkinter** library, providing an intuitive and simple interface to help you manage your expenses. It allows users to:

- **Add** new expenses
- **Edit** existing ones
- **Delete** unwanted expenses
- **Search** through your list by category or description

All data is stored in a **JSON file** (`expenses.json`), and the project includes **unit tests** written in **pytest** to ensure core functionalities  are properly working.

---

## ✨ **Features**

- **Add Expense**: Easily input a new expense with a category, amount, and description.
- **Edit Expense**: Modify any existing expense details.
- **Delete Expense**: Select and remove an expense.
- **Search Expenses**: Find expenses by a keyword (either category or description).
- **Expense Display**: View your expenses in a neat, tabular format (ID, Category, Amount, Description).

---

## 📁 **Files**

### `project.py`

This file is the heart of the Expense Tracker application, and it contains the following functions:

- **`load_expenses()`**: Loads expenses from `expenses.json`.
- **`save_expenses(expenses)`**: Saves the list of expenses back into the `expenses.json` file.
- **`add_expense()`**: Adds a new expense to the list.
- **`edit_expense()`**: Allows the user to edit an existing expense.
- **`delete_expense()`**: Removes the selected expense from the list.
- **`update_expense_list()`**: Refreshes the expense display in the GUI.
- **`search_expenses()`**: Filters expenses based on a keyword search.
- **`main()`**: Initializes the GUI window with widgets (buttons, labels, input fields, expense list).

**GUI Overview**:
- **Labels**, **input fields**, and **buttons** are arranged in a user-friendly layout.
- The **Treeview widget** displays expenses in a table format.
- The app features clear, accessible buttons for each action (Add, Edit, Delete, Search).

### `test_project.py`

This file contains unit tests for the core functions of `project.py`. It uses **pytest** for testing:

- **`test_load_expenses()`**: Verifies that expenses are loaded correctly.
- **`test_save_expenses()`**: Ensures that expenses are saved accurately to the JSON file.
- **`sample_data()`**: Provides a set of sample expenses for testing.
- **`setup_test_file()`**: Sets up a temporary file for testing without modifying the actual data file.

These tests ensure the robustness of the app by verifying the functionality of the `load_expenses()` and `save_expenses()` methods.

---

## ⚙️ **Design Decisions**

### 1. **JSON Storage**
- The decision to store expenses in a simple **JSON file** makes the app lightweight and easy to use without needing a database. It also enables portability and ensures data persistence across sessions.

### 2. **Tkinter for GUI**
- **Tkinter** was chosen for its simplicity and rapid development features, allowing for quick and easy GUI creation with minimal overhead. It provides an accessible user interface without complexity.

### 3. **Modular Code**
- The application’s code is modular and neatly organized. Each function focuses on a single responsibility (adding, editing, deleting, etc.), promoting readability and ease of maintenance.

---

## 🔮 **Future Improvements**

1. **Validation Enhancements**: Add more validation, such as ensuring that amounts are positive numbers and input fields are not empty.
2. **Advanced Search**: Implement advanced filtering options, like searching by date range or filtering expenses by amount.
3. **Styling**: Refactor the interface for a more modern look, possibly using libraries like **PyQt** for a more sophisticated GUI.

---

## 🚀 **Running the Application**

To run the Expense Tracker app, follow these steps:

### 1. Install Dependencies

Ensure you have **Python** installed. Then, install **pytest** for running tests:

```bash
pip install pytest
