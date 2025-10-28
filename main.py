
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Connect or create SQLite database
conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS employee_performance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    attendance INTEGER,
    tasks_completed INTEGER,
    teamwork TEXT,
    performance TEXT
)
""")
conn.commit()

# --- Rule-Based Evaluation Logic ---
def evaluate_performance(attendance, tasks_completed, teamwork):
    teamwork = teamwork.lower()
    if attendance >= 90 and tasks_completed >= 80 and teamwork == "excellent":
        return "Outstanding"
    elif attendance >= 75 and tasks_completed >= 70:
        return "Good"
    elif attendance >= 60 and tasks_completed >= 50:
        return "Average"
    else:
        return "Needs Improvement"

# --- GUI Functions ---
def add_employee():
    name = name_var.get()
    attendance = int(attendance_var.get())
    tasks = int(tasks_var.get())
    teamwork = teamwork_var.get()

    performance = evaluate_performance(attendance, tasks, teamwork)
    cursor.execute("""
        INSERT INTO employee_performance (name, attendance, tasks_completed, teamwork, performance)
        VALUES (?, ?, ?, ?, ?)
    """, (name, attendance, tasks, teamwork, performance))
    conn.commit()

    messagebox.showinfo("Result", f"Performance for {name}: {performance}")
    clear_fields()
    show_records()

def show_records():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM employee_performance")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)

def delete_record():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select", "Please select a record to delete.")
        return
    record = tree.item(selected)["values"][0]
    cursor.execute("DELETE FROM employee_performance WHERE id=?", (record,))
    conn.commit()
    show_records()

def clear_fields():
    name_var.set("")
    attendance_var.set("")
    tasks_var.set("")
    teamwork_var.set("")

# --- GUI Design ---
root = tk.Tk()
root.title("Employee Performance Expert System")
root.geometry("800x600")

tk.Label(root, text="Employee Performance Evaluation System", font=("Arial", 16, "bold")).pack(pady=10)

form_frame = tk.Frame(root)
form_frame.pack(pady=10)

name_var = tk.StringVar()
attendance_var = tk.StringVar()
tasks_var = tk.StringVar()
teamwork_var = tk.StringVar()

tk.Label(form_frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(form_frame, textvariable=name_var).grid(row=0, column=1)

tk.Label(form_frame, text="Attendance (%)").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(form_frame, textvariable=attendance_var).grid(row=1, column=1)

tk.Label(form_frame, text="Tasks Completed (%)").grid(row=2, column=0, padx=5, pady=5)
tk.Entry(form_frame, textvariable=tasks_var).grid(row=2, column=1)

tk.Label(form_frame, text="Teamwork (Excellent/Good/Average/Poor)").grid(row=3, column=0, padx=5, pady=5)
tk.Entry(form_frame, textvariable=teamwork_var).grid(row=3, column=1)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Record", command=add_employee, bg="lightgreen").grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Delete Record", command=delete_record, bg="lightcoral").grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="View Records", command=show_records, bg="lightblue").grid(row=0, column=2, padx=10)
tk.Button(button_frame, text="Clear Fields", command=clear_fields, bg="lightgray").grid(row=0, column=3, padx=10)

# Table
tree = ttk.Treeview(root, columns=("ID", "Name", "Attendance", "Tasks", "Teamwork", "Performance"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Attendance", text="Attendance")
tree.heading("Tasks", text="Tasks")
tree.heading("Teamwork", text="Teamwork")
tree.heading("Performance", text="Performance")
tree.pack(fill="both", expand=True, pady=10)

show_records()
root.mainloop()

# Close database on exit
conn.close()
