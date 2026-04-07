import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Spriya@1995",
    database = "expense_db",
    
)

cursor = conn.cursor()
print("Connected to DB successfully")


#  Abstract Class

from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_details(self):
        pass
    
# 1. User Creation

class User(Person):
    def __init__(self,name):
        self._name = name
        
    def add_user(self):
        query = "Insert into users (name) values (%s)"
        cursor.execute(query, (self._name,))
        conn.commit()
        print("User Addes")
    
    def get_details(self):
        return f"User: {self.__name}"

# 2. Expense Class (Inheritance)

class Expense(User):
    def __init__(self, name, user_id, amount, category, desc, date):
        super().__init__(name)  
        self.user_id = user_id
        self.amount = amount
        self.category = category
        self.desc = desc
        self.date = date

    def add_expense(self):
        query = """
        INSERT INTO expenses (user_id, amount, category, description, date)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (self.user_id, self.amount,
                               self.category, self.desc, self.date))
        conn.commit()
        print("✅ Expense Added")

    def get_details(self): 
        return f"{self.category} - {self.amount}"
    
# 3. View Expenses(Join)
    
def view_expenses():
        query = """
        SELECT u.name, e.amount, e.category, e.date
        FROM users u
        JOIN expenses e ON u.user_id = e.user_id
        """
        cursor.execute(query)

        for row in cursor.fetchall():
         print(row)
         
# 4: Filter Expenses

def filter_by_category(category):
    cursor.execute("SELECT amount, category FROM expenses")
    data = cursor.fetchall()

    result = list(filter(lambda x: x[1] == category, data))
    print(result)


def filter_by_date(date):
    cursor.execute("SELECT amount, date FROM expenses")
    data = cursor.fetchall()

    result = [x for x in data if str(x[1]) == date]
    print(result)

    
    # 5. Total Expense Calculation(map,reduce)
    
from functools import reduce

def total_expense():
      cursor.execute("SELECT amount FROM expenses")
      data = cursor.fetchall()

      amounts = list(map(lambda x: x[0], data))

      total = reduce(lambda x, y: x + y, amounts, 0)
      print("Total Expense:", total)
      

# 6. Category-wise Spending

def category_wise():
    cursor.execute("SELECT category, amount FROM expenses")
    data = cursor.fetchall()

    result = {}
    for cat, amt in data:
        result[cat] = result.get(cat, 0) + amt

    print(result)
    
    #  7. Delete / Update Expense
    
    def update_expense(exp_id, new_amount):
     query = "UPDATE expenses SET amount=%s WHERE exp_id=%s"
     cursor.execute(query, (new_amount, exp_id))
     conn.commit()
     print("✅ Updated")


    def delete_expense(exp_id):
     query = "DELETE FROM expenses WHERE exp_id=%s"
     cursor.execute(query, (exp_id,))
     conn.commit()
     print("✅ Deleted")
        
        # Advanced Logic (Main Evaluation)
    
    # 1. Monthly Report
    
    def monthly_report():
     query = """
    SELECT MONTH(date), SUM(amount)
    FROM expenses
    GROUP BY MONTH(date)
    """
     cursor.execute(query)

    for row in cursor.fetchall():
        print(f"Month {row[0]}: {row[1]}")
        
    # 2. Highest Expense
    
    from functools import reduce
    
    def highest_expense():
     cursor.execute("SELECT amount FROM expenses")
     data = cursor.fetchall()

     amounts = [x[0] for x in data]
     high = reduce(lambda a, b: a if a > b else b, amounts)
     print("Highest Expense:", high)
     
    #  3. Smart Insight
    
def smart_insight():
    cursor.execute("SELECT category, amount FROM expenses")
    data = cursor.fetchall()

    result = {}
    for cat, amt in data:
        result[cat] = result.get(cat, 0) + amt

    if not result:
        print("No data")
        return

    max_cat = max(result, key=result.get)

    print(f"⚠️ You are spending too much on {max_cat}")
    
    
    # Final System
    
    # Final System

while True:
    print("\n1.Add User\n2.Add Expense\n3.View\n4.Total\n5.Smart Insight\n6.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        User(name).add_user()

    elif choice == "2":
        user_id = int(input("User ID: "))
        amt = float(input("Amount: "))
        cat = input("Category: ")
        desc = input("Description: ")
        date = input("Date (YYYY-MM-DD): ")

        Expense("", user_id, amt, cat, desc, date).add_expense()

    elif choice == "3":
        view_expenses()

    elif choice == "4":
        total_expense()

    elif choice == "5":
        smart_insight()

    elif choice == "6":
      break