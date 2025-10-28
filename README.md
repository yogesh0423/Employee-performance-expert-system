# 🧠 Employee Performance Evaluation Expert System

A simple **Expert System** built in Python with **Tkinter GUI** and **SQLite3** database to automate employee performance evaluation based on attendance, task completion, and teamwork.

---

## 🚀 Features
- GUI-based interface for easy data entry
- Rule-based evaluation system
- Add, View, and Delete employee records
- SQLite database integration
- Real-time performance result display

---

## 🧰 Tech Stack
- **Language:** Python 3.x  
- **Libraries:** Tkinter, SQLite3  
- **Database:** employee.db  

---

## 🧠 Evaluation Logic
```python
if attendance >= 90 and tasks_completed >= 80 and teamwork == "excellent":
    performance = "Outstanding"
elif attendance >= 75 and tasks_completed >= 70:
    performance = "Good"
elif attendance >= 60 and tasks_completed >= 50:
    performance = "Average"
else:
    performance = "Needs Improvement"
