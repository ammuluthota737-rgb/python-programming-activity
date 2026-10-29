

name = input("Enter patient name: ")

consultation = float(input("Consultation charge: "))
diagnostic = float(input("Diagnostic charge: "))
treatment = float(input("Treatment charge: "))

category = input("Patient category (senior/regular): ").lower()
paid = input("Payment completed? (yes/no): ").lower()

if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges")
elif category not in ["senior", "regular"]:
    print("Invalid patient category")
elif paid not in ["yes", "no"]:
    print("Invalid payment status")
else:
    total = consultation + diagnostic + treatment

    if category == "senior":
        concession = total * 0.10
    else:
        concession = 0

    final_bill = total - concession

    if paid == "yes":
        status = "Paid"
    else:
        status = "Payment Pending"

    print("\n--- HOSPITAL BILL ---")
    print("Patient Name:", name)
    print("Patient Category:", category)
    print("Total Charges: Rs.", round(total, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Final Bill: Rs.", round(final_bill, 2))
    print("Payment Status:", status)
