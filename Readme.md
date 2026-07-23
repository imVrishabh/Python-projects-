# Expense Tracker Using Python

A simple command-line based Expense Tracker built with Python. This project allows users to add expenses, view all recorded expenses, calculate the total amount spent, and exit the program through an interactive menu.

## Features

* Add new expenses with:

  * Date
  * Category (Food, Travel, Shopping, etc.)
  * Description
  * Amount spent
* View all saved expenses.
* Calculate the total amount spent.
* Simple menu-driven interface.
* Beginner-friendly Python project.

## Technologies Used

* Python 3

## Project Structure

```text
Expense Tracker/
│
├── expense_tracker.py
└── README.md
```

## How It Works

The program stores expenses in a list of dictionaries during runtime.

Each expense contains:

```python
{
    "date": "24-07-2026",
    "category": "Food",
    "description": "Burger",
    "amount": 150
}
```

### Menu Options

```text
==== MENU ====

1. Add Expenses
2. View All Expenses
3. View Total Kharcha
4. Exit
```

### Example

```text
Welcome to Expense Tracker : Kharcha kam kiya karo

==== MENU ====

1. Add Expenses
2. View All Expenses
3. View Total Kharcha
4. Exit

Please Enter Your Choice: 1

Date of Expense: 24-07-2026
Type of Expense: Food
Detail about Expense: Pizza
How Much You Spent: 250

Expense is added successfully.
```

## Running the Project

1. Make sure Python is installed on your system.
2. Clone the repository:

```bash
git clone <your-repository-link>
```

3. Open the project folder.

4. Run the program:

```bash
python expense_tracker.py
```

## Future Improvements

* Store expenses permanently using files or databases.
* Add expense deletion functionality.
* Filter expenses by category or date.
* Display monthly reports.
* Add graphical charts for expense analysis.
* Build a GUI using Tkinter or a web version using Flask or Django.

## Note

This project currently stores data only while the program is running. Once the program is closed, all expenses are lost. Persistent storage can be added in future versions.

## Author

**Vrishabh Deshmukh**

> "Kharcha kam kiya kar!"
