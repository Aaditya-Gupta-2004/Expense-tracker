💰 Expense Tracker (Django)
A simple yet powerful Expense Tracker web application built using Django. This app allows users to record daily expenses, dynamically manage categories, and view insightful reports to track their spending habits over time.

🚀 Features
📋 Add, edit, and delete expenses

🏷️ Dynamic category management (create, update, delete)

📅 Filter expenses by date, category, and amount

📊 View total expense summary

🔒 User authentication (Login/Logout)

🧼 Clean and responsive UI (Optional: Bootstrap/Tailwind)

🛠 Tech Stack
Backend: Django (Python)

Database: SQLite (default) — easily switchable to PostgreSQL/MySQL

Frontend: HTML, CSS (Bootstrap optional)

Templating: Django Templates

📦 Installation
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/django-expense-tracker.git
cd django-expense-tracker
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5. Start the development server
bash
Copy
Edit
python manage.py runserver
6. Access the app
Open your browser and go to:
http://127.0.0.1:8000/

🔐 Admin Access
To access the Django admin panel:

bash
Copy
Edit
python manage.py createsuperuser
Then visit:
http://127.0.0.1:8000/admin/

