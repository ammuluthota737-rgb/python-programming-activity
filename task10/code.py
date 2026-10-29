
venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
catering = float(input("Enter catering cost per person: Rs. "))
transport = float(input("Enter transport cost: Rs. "))
certificates = float(input("Enter certificate cost per person: Rs. "))

participants = int(input("Enter expected participants: "))
sponsorship = float(input("Enter sponsorship amount: Rs. "))
fee = float(input("Enter registration fee per person: Rs. "))

if participants < 0 or sponsorship < 0 or fee < 0:
    print("Invalid input")
else:
    fixed_cost = venue + equipment + transport
    variable_cost = participants * (catering + certificates)
    total_cost = fixed_cost + variable_cost

    registration_income = participants * fee
    total_funds = sponsorship + registration_income
    shortfall = max(0, total_cost - total_funds)

    contribution = max(0, total_cost - sponsorship) / participants \
        if participants > 0 else 0

    # Break-even registration count
    per_person_margin = fee - catering - certificates

    if total_cost <= sponsorship:
        break_even = 0
    elif per_person_margin > 0:
        break_even = max(
            0,
            int((fixed_cost - sponsorship) / per_person_margin) + 1
        )
        # Correct exact-integer break-even
        import math
        break_even = max(
            0, math.ceil((fixed_cost - sponsorship) / per_person_margin)
        )
    else:
        break_even = None

    print("\n===== EVENT FINANCIAL REPORT =====")
    print(f"Fixed Costs       : Rs. {fixed_cost:.2f}")
    print(f"Variable Costs    : Rs. {variable_cost:.2f}")
    print(f"Total Event Cost  : Rs. {total_cost:.2f}")
    print(f"Sponsorship       : Rs. {sponsorship:.2f}")
    print(f"Registration Income: Rs. {registration_income:.2f}")
    print(f"Participant Contribution Needed: Rs. {contribution:.2f}")
    print(f"Sponsorship Shortfall: Rs. {shortfall:.2f}")

    if break_even is not None:
        print("Minimum Break-even Registrations:", break_even)
    else:
        print("Break-even cannot be achieved with this registration fee.")

