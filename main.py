import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

# Create table if it doesn't exist
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

# --- Knowledge Base Rules ---
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

# --- Menu Functions ---
def add_employee():
    print("\n--- Add Employee Record ---")
    name = input("Enter employee name: ")
    attendance = int(input("Enter attendance percentage: "))
    tasks_completed = int(input("Enter task completion percentage: "))
    teamwork = input("Enter teamwork rating (Excellent/Good/Average/Poor): ")

    performance = evaluate_performance(attendance, tasks_completed, teamwork)

    cursor.execute("""
        INSERT INTO employee_performance (name, attendance, tasks_completed, teamwork, performance)
        VALUES (?, ?, ?, ?, ?)
    """, (name, attendance, tasks_completed, teamwork, performance))
    conn.commit()

    print(f"\n✅ Performance evaluation for {name}: {performance}")

def view_records():
    print("\n--- All Employee Records ---")
    cursor.execute("SELECT * FROM employee_performance")
    records = cursor.fetchall()
    if not records:
        print("No records found.")
    else:
        for row in records:
            print(f"ID: {row[0]} | Name: {row[1]} | Attendance: {row[2]} | Tasks: {row[3]} | Teamwork: {row[4]} | Performance: {row[5]}")

def delete_record():
    emp_id = int(input("Enter Employee ID to delete: "))
    cursor.execute("DELETE FROM employee_performance WHERE id=?", (emp_id,))
    conn.commit()
    print("Record deleted successfully.")

def update_record():
    emp_id = int(input("Enter Employee ID to update: "))
    attendance = int(input("Enter new attendance percentage: "))
    tasks_completed = int(input("Enter new task completion percentage: "))
    teamwork = input("Enter new teamwork rating (Excellent/Good/Average/Poor): ")

    performance = evaluate_performance(attendance, tasks_completed, teamwork)
    cursor.execute("""
        UPDATE employee_performance 
        SET attendance=?, tasks_completed=?, teamwork=?, performance=?
        WHERE id=?
    """, (attendance, tasks_completed, teamwork, performance, emp_id))
    conn.commit()
    print("✅ Record updated successfully.")

# --- Main Menu ---
while True:
    print("\n--- Employee Performance Expert System ---")
    print("1. Add Employee Record")
    print("2. View All Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_records()
    elif choice == '3':
        update_record()
    elif choice == '4':
        delete_record()
    elif choice == '5':
        print("Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")

# Close connection
conn.close()
