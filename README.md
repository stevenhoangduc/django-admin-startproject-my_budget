# 💰 My Budget - Expense Tracking App

My Budget is a Dango-based web application that helps users manage their personal finances by tracking income, expenses, budgets, and categories.  It offers a clean interface, mobile-friendly design, and features that support financial awareness and goal setting.

The project uses authentication and CRUD operations to create, read, update and elete expenses assigned to a user.

[Live Demo]
https://my-budget-app-242e0420fc68.herokuapp.com/

## 📷 Screenshots 

![login](<screenshots/Screenshot 2025-03-17 at 9.18.00 PM.png>)
![home](<screenshots/Screenshot 2025-03-17 at 9.29.40 PM.png>)
![about](<screenshots/Screenshot 2025-03-17 at 9.30.26 PM.png>)
![pdf](<screenshots/Screenshot 2025-03-17 at 9.31.59 PM.png>)


### 🚀 Features

* User Registrations & Profile
* Track Income and Expenses
* Organize by Category and Subcategory
* Create Monthly Budgets
* View Transaction History
* Add Notes to Transactions
* Dashboard Summary (Income vs Expenses)

### 🧱 Tech Stack

* Backend: Django (Python)
* Frontend: Django Templates + HTML/CSS(Tailwind or Bootstrap suggested)
* Database: SQLite (default), can switch to PostgreSQL
* Charting: Chart.js (optional for dashboard visuals)

### ⚙️ Getting a Started

1. Clone the repo

    * git clone <your-repo-url>
    * cd my_budget

2. Create a virtual enviroment

    * python -m venv venv
    * source venv/bin/activate  # or venv\\Scripts\\activate on Windows

3. Install dependencies

    * pip install django

4. Run initial setup

    * python manage.py makemigrations
    * python manage.py migrate

5. Start the server

    * python3 manage.py runserver

6. (Optional) Create superuser

    * python3 manage.py createsuperuser

### 🧠 Future Ideas

* Monthly budget alerts
* Bank API intergrations
* Expense predictions
* Chart/graph display

### 👨‍💻 Author

Made by Steven Hoang Duc








