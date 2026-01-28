# 🏋️ Gym Registration System (Flask + SQLite)

## 📌 Project Overview
This project is a **full-stack Gym Registration Web Application** built using **Flask**, **HTML/CSS**, and **SQLite**.  
It allows users to register gym membership details through a professional web form, and securely stores the data in a local database.

The project demonstrates:
- Frontend form design
- Backend processing using Flask
- Persistent data storage using SQLite
- End-to-end full-stack integration

---

## ✨ Features
- Clean and professional registration form
- Collects detailed user information:
  - Full Name
  - Email
  - Phone Number
  - Age
  - Gender
  - Height & Weight
  - Membership Plan
  - Fitness Goal
  - Experience Level
- Data stored securely in `gym.db`
- SQLite database with proper schema
- Easy to extend and customize

---

## 🧠 Tech Stack
**Frontend**
- HTML5
- CSS3 (custom styling)

**Backend**
- Python 3
- Flask Framework

**Database**
- SQLite (`gym.db`)

---

## 📂 Project Structure
Gym_Registration/
│
├── app.py
├── gym.db
│
├── templates/
│ └── index.html
│
├── static/
│ └── style.css
│
└── README.md

---

## ▶️ How to Run the Project

### 1️⃣ Open Command Prompt in Project Folder
- Go to `C:\Gym_Registration`
- Click on the address bar
- Type `cmd`
- Press **Enter**

---

### 2️⃣ (Optional) Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install flask

4️⃣ Run the Application
python app.py

5️⃣ Open in Browser

Visit:

http://127.0.0.1:5000

🗄️ Database Details

Database file: gym.db

Table: members

Data is saved automatically when the user submits the form

SQLite auto-increments member IDs

View Database Data

You can view stored data using:

DB Browser for SQLite

Open gym.db

Click Browse Data → members

🧩 Is This a Full-Stack Project?

✅ Yes

Layer	Used
Frontend	HTML + CSS
Backend	Flask (Python)
Database	SQLite

This project covers frontend UI, backend logic, and database persistence.

⚠️ Development Notes

Flask development server is used (not for production)

SQLite is lightweight and ideal for learning/demo projects

Database locking errors may occur if gym.db is open while server is running

🚀 Future Enhancements

Admin dashboard to view members

Login & authentication

Payment integration

REST API support

Deployment using Gunicorn / Docker

✅ Status

✔ Fully functional
✔ Data successfully stored
✔ Tested end-to-end
✔ Beginner & resume friendly

📌 Final Note

This project is ideal for:

Learning Flask

Understanding full-stack flow

College submissions

Resume & GitHub portfolio

Feel free to fork, improve, or deploy 🚀
