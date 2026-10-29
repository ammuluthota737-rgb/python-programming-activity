
# Progressive Electricity Billing

months = int(input("Enter number of months: "))

month_names = []
bills = []

for i in range(months):
    name = input("\nEnter month name: ")
    units = float(input("Enter units consumed: "))

    # Calculate progressive energy charges
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed = 50
    surcharge = energy * 0.05

    if units < 100:
        rebate = energy * 0.10
    else:
        rebate = 0

    bill = energy + fixed + surcharge - rebate

    month_names.append(name)
    bills.append(bill)

    print("Energy charge: Rs.", round(energy, 2))
    print("Fixed charge: Rs.", fixed)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Final bill: Rs.", round(bill, 2))

# Compare consecutive monthly bills
print("\n--- Monthly Bill Comparison ---")

for i in range(months):
    print(month_names[i], ": Rs.", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]

        if bills[i - 1] > 0:
            percent = increase / bills[i - 1] * 100

            if percent > 30:
                print("Unusual increase:", round(percent, 2), "%")
            elif increase > 0:
                print("Normal increase:", round(percent, 2), "%")
            else:
                print("No increase in bill.")

