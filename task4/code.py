
name = input("Enter employee name: ")
basic = float(input("Enter basic pay: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))

gross = basic + allowances + overtime + incentives

if gross <= 10000:
    deduction = 0
elif gross <= 20000:
    deduction = (gross - 10000) * 0.10
else:
    deduction = 1000 + (gross - 20000) * 0.20

net = gross - deduction

print("\n===== SALARY STATEMENT =====")
print("Employee Name :", name)
print("Basic Pay     : ₹", basic)
print("Allowances    : ₹", allowances)
print("Overtime Pay  : ₹", overtime)
print("Incentives    : ₹", incentives)
print("----------------------------")
print("Gross Salary  : ₹", round(gross, 2))
print("Deductions    : ₹", round(deduction, 2))
print("Net Salary    : ₹", round(net, 2))

