# 🧠 Employee Performance Evaluation Expert System

This is a **Command-Line Expert System** built in Python using a **rule-based approach** to evaluate employee performance.  
The system uses parameters such as **attendance**, **tasks completed**, and **teamwork** to categorize employees into performance levels.

---

## 🚀 Features

- Command-line interface (CLI) for ease of use  
- Rule-based reasoning to determine employee performance  
- Local data storage using **SQLite**  
- Add, view, update, and delete employee records  
- Simple and lightweight system — ideal for learning Expert Systems in AI  

---

## 🧰 Tech Stack

- **Language:** Python 3.x  
- **Database:** SQLite3 (built-in)  
- **Libraries:** Standard Python libraries (no external dependencies)

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
