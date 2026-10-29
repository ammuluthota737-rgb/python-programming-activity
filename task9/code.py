
budget = float(input("Enter travel budget in INR: "))
n = int(input("Enter number of expense categories: "))

expenses = []
total_spending = 0

for i in range(n):
    print("\nExpense", i + 1)
    category = input("Category: ")
    amount = float(input("Amount in foreign currency: "))
    rate = float(input("Exchange rate (INR per unit): "))
    fee_percent = float(input("Conversion fee (%): "))

    converted = amount * rate
    fee = converted * fee_percent / 100
    total = converted + fee

    expenses.append((category, converted, fee, total))
    total_spending += total

largest = max(expenses, key=lambda x: x[3])

print("\n===== TRAVEL BUDGET REPORT =====")

for category, converted, fee, total in expenses:
    print(f"\nCategory: {category}")
    print(f"Converted Amount: Rs. {converted:.2f}")
    print(f"Conversion Fee: Rs. {fee:.2f}")
    print(f"Total Expense: Rs. {total:.2f}")

print("\nTotal Spending: Rs.", round(total_spending, 2))
print("Budget: Rs.", round(budget, 2))
print("Largest Expense Category:", largest[0])

if total_spending <= budget:
    print("Status: Within Budget")
    print("Remaining: Rs.", round(budget - total_spending, 2))
else:
    print("Status: Over Budget")
    print("Exceeded By: Rs.", round(total_spending - budget, 2))

