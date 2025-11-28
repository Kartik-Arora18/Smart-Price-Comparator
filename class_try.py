import tkinter as tk
from tkinter import ttk, messagebox
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime

class ExpenseTrackerApp(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Expense Tracker")
        self.geometry("600x400")
        self.expenses = defaultdict(list)  # Dictionary to store expenses by month
        self.categories = [
            "Food",
            "Travel",
            "Utilities",
            "Entertainment",
            "Other",
        ]
        self.category_var = tk.StringVar(self)
        self.category_var.set(self.categories[0])
        self.load_expenses()  # Load existing expenses data
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(
            self, text="Expense Tracker", font=("Helvetica", 20, "bold")
        )
        self.label.pack(pady=10)
        self.frame_input = tk.Frame(self)
        self.frame_input.pack(pady=10)
        self.expense_label = tk.Label(
            self.frame_input, text="Expense Amount:", font=("Helvetica", 12)
        )
        self.expense_label.grid(row=0, column=0, padx=5)
        self.expense_entry = tk.Entry(
            self.frame_input, font=("Helvetica", 12), width=15
        )
        self.expense_entry.grid(row=0, column=1, padx=5)
        self.category_label = tk.Label(
            self.frame_input, text="Category:", font=("Helvetica", 12)
        )
        self.category_label.grid(row=0, column=2, padx=5)
        self.category_dropdown = ttk.Combobox(
            self.frame_input,
            textvariable=self.category_var,
            values=self.categories,
            font=("Helvetica", 12),
            width=15,
        )
        self.category_dropdown.grid(row=0, column=3, padx=5)
        self.date_label = tk.Label(
            self.frame_input, text="Date:", font=("Helvetica", 12)
        )
        self.date_label.grid(row=0, column=4, padx=5)
        self.month_var = tk.StringVar(self)
        self.month_var.set(datetime.now().strftime("%B"))  # Set current month as default
        self.month_dropdown = ttk.Combobox(
            self.frame_input,
            textvariable=self.month_var,
            values=[
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ],
            font=("Helvetica", 12),
            width=10,
        )
        self.month_dropdown.grid(row=0, column=5, padx=5)
        self.year_var = tk.StringVar(self)
        self.year_var.set(datetime.now().year)  # Set current year as default
        self.year_dropdown = ttk.Combobox(
            self.frame_input,
            textvariable=self.year_var,
            values=[year for year in range(2020, 2031)],  # Assume years from 2020 to 2030
            font=("Helvetica", 12),
            width=7,
        )
        self.year_dropdown.grid(row=0, column=6, padx=5)
        self.add_button = tk.Button(self, text="Add Expense", command=self.add_expense)
        self.add_button.pack(pady=5)
        self.frame_list = tk.Frame(self)
        self.frame_list.pack(pady=10)
        self.scrollbar = tk.Scrollbar(self.frame_list)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.expense_listbox = tk.Listbox(
            self.frame_list,
            font=("Helvetica", 12),
            width=40,
            yscrollcommand=self.scrollbar.set,
        )
        self.expense_listbox.pack(pady=5)
        self.scrollbar.config(command=self.expense_listbox.yview)
        self.delete_button = tk.Button(
            self, text="Delete Expense", command=self.delete_expense
        )
        self.delete_button.pack(pady=5)
        self.show_chart_button = tk.Button(
            self, text="Show Expenses Chart", command=self.show_expenses_chart
        )
        self.show_chart_button.pack(pady=5)

    def add_expense(self):
        expense = self.expense_entry.get()
        category = self.category_var.get()
        month = self.month_var.get()
        year = self.year_var.get()
        if expense:
            date = f"{year}-{datetime.strptime(month, '%B').month:02d}"
            self.expenses[date].append((float(expense), category))
            self.expense_listbox.insert(tk.END, f"{expense} - {category} ({date})")
            self.expense_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Expense amount cannot be empty.")

    def delete_expense(self):
        selected_index = self.expense_listbox.curselection()
        if selected_index:
            selected_item = self.expense_listbox.get(selected_index)
            expense_info = selected_item.split(" - ")
            expense = float(expense_info[0])
            category_date = expense_info[1].split(" (")
            category = category_date[0]
            date = category_date[1].split(")")[0]
            self.expenses[date].remove((expense, category))
            self.expense_listbox.delete(selected_index)
        else:
            messagebox.showwarning("Warning", "No expense selected to delete.")

    def show_expenses_chart(self):
        month_expenses = defaultdict(float)
        for month, month_data in self.expenses.items():
            for expense, _ in month_data:
                month_expenses[month] += expense
        months = list(month_expenses.keys())
        expenses = list(month_expenses.values())
        plt.figure(figsize=(8, 6))
        plt.bar(months, expenses, color='skyblue')
        plt.xlabel('Month')
        plt.ylabel('Total Expenses')
        plt.title(f"Monthly Expenses")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def load_expenses(self):
        try:
            with open("expenses.txt", "r") as file:
                for line in file:
                    date, expense, category = line.strip().split(",")
                    self.expenses[date].append((float(expense), category))
        except FileNotFoundError:
            pass

    def save_expenses(self):
        with open("expenses.txt", "w") as file:
            for date, expenses in self.expenses.items():
                for expense, category in expenses:
                    file.write(f"{date},{expense},{category}\n")

    def on_closing(self):
        self.save_expenses()
        self.destroy()

if __name__ == "__main__":

    app = ExpenseTrackerApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)  # Bind on_closing method to window close event
    app.mainloop()