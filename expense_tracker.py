import sqlite3
from datetime import datetime

class ExpenseTracker:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    amount REAL,
                    category TEXT,
                    description TEXT,
                    date TEXT
                )
            ''')

    def add_expense(self, amount, category, description):
        with self.conn:
            self.conn.execute('''
                INSERT INTO expenses (amount, category, description, date)
                VALUES (?, ?, ?, ?)
            ''', (amount, category, description, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def view_expenses(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT *
