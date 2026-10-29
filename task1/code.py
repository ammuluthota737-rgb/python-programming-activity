
# University Scholarship Allocation System

def is_eligible(aggregate, marks, attendance, income):
    return (
        aggregate >= 60
        and all(m >= 50 for m in marks)
        and attendance >= 75
        and income <= 500000
    )

n = int(input("Enter number of applicants: "))
eligible = []

for i in range(n):
    print("\nApplicant", i + 1)

    name = input("Enter name: ")
    marks = []

    for j in range(1, 6):
        m = float(input(f"Marks in subject {j}: "))
        marks.append(m)

    attendance = float(input("Attendance percentage: "))
    income = float(input("Annual family income: "))

    aggregate = sum(marks) / len(marks)

    if is_eligible(aggregate, marks, attendance, income):
        eligible.append([
            name, aggregate, marks[0], attendance, income
        ])
        print("Eligible for scholarship")
    else:
        print("Not eligible for scholarship")

# Tie-breaking rules:
# 1. Higher aggregate
# 2. Higher Subject 1 marks
# 3. Higher attendance
# 4. Lower family income

eligible.sort(
    key=lambda x: (-x[1], -x[2], -x[3], x[4])
)

print("\n--- RANKED SCHOLARSHIP LIST ---")

if not eligible:
    print("No eligible applicants.")
else:
    for rank, student in enumerate(eligible, start=1):
        print(
            rank, student[0],
            "- Aggregate:", round(student[1], 2)
        )

