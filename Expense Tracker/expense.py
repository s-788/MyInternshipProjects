import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expense_data = []

    def get_user_input(self):
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the expense category: ")
        date_str = input("Enter the date (YYYY-MM-DD, press Enter for today): ").strip()

        if date_str == "":
            date = datetime.today().strftime('%Y-%m-%d')
        else:
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Using today's date.")
                date = datetime.today().strftime('%Y-%m-%d')

        return {"Amount": amount, "Category": category, "Date": date}

    def add_expense(self, expense):
        self.expense_data.append(expense)

    def save_data(self):
        with open("expense_data.json", "w") as file:
            json.dump(self.expense_data, file)

    def load_data(self):
        try:
            with open("expense_data.json", "r") as file:
                self.expense_data = json.load(file)
        except FileNotFoundError:
            pass

    def show_summary(self):
        # Your data analysis and summary logic here
        # For simplicity, just print the raw data for now
        print("🎯Expense Data:")
        for expense in self.expense_data:
            print(expense)

def main():
    expense_tracker = ExpenseTracker()
    expense_tracker.load_data()

    while True:
        print("\n🎯Expense Tracker Menu:")
        print("1.👉 Add Expense")
        print("2.💵 Show Summary")
        print("3.✅ Save and Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            expense = expense_tracker.get_user_input()
            expense_tracker.add_expense(expense)
            print("🎯Expense added successfully!")
        elif choice == "2":
            expense_tracker.show_summary()
        elif choice == "3":
            expense_tracker.save_data()
            print("🎯Data saved. Exiting...")
            break
        else:
            print("🎯Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
