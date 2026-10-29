
usage = float(input("Enter required data (GB): "))
calls = int(input("Enter required call minutes: "))
days = int(input("Enter required validity (days): "))
budget = float(input("Enter budget (Rs): "))

n = int(input("Enter number of plans: "))
best_plan = ""
best_cost = float("inf")

for i in range(n):
    print("\nPlan", i + 1)
    name = input("Plan name: ")
    price = float(input("Plan price: "))
    data = float(input("Data limit (GB): "))
    call_limit = int(input("Call limit (minutes): "))
    validity = int(input("Validity (days): "))
    extra_data_rate = float(input("Extra cost per GB: "))
    extra_call_rate = float(input("Extra cost per minute: "))

    extra_data = max(0, usage - data)
    extra_calls = max(0, calls - call_limit)

    cost = price + extra_data * extra_data_rate
    cost += extra_calls * extra_call_rate

    print("Total cost: Rs.", round(cost, 2))

    if (data >= usage and call_limit >= calls
            and validity >= days and cost <= budget):
        if cost < best_cost:
            best_cost = cost
            best_plan = name

print("\n===== RESULT =====")
if best_plan:
    print("Most economical plan:", best_plan)
    print("Total cost: Rs.", round(best_cost, 2))
else:
    print("No eligible plan found within the budget.")

