# 🎓 Student Management System

A Student Management System built using **Python, Flask, PostgreSQL, HTML, CSS, and Jinja2**.

## Features

- ➕ Add Student
- 📋 View Students
- ✏️ Edit Student
- ❌ Delete Student

## Technologies Used

- Python
- Flask
- PostgreSQL
- psycopg2
- HTML
- CSS
- Jinja2

## Project Structure

```
Student-Management-System/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── students.html
│   ├── edit.html
│   ├── about.html
│   └── contact.html
│
├── static/
│   └── style.css
│
├── .gitignore
└── README.md
```

## How to Run

1. Clone the repository

```
git clone <repository-url>
```

2. Install dependencies

```
pip install flask psycopg2
```

3. Create a PostgreSQL database named `students_db`.

4. Create the `students` table.

5. Run

```
python app.py
```

Open:

```
http://127.0.0.1:5000
```
