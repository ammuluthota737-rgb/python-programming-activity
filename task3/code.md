# Hospital Billing and Patient Classification – Python Program

## 1. Problem Statement

Develop a Python program to calculate hospital bills using consultation, diagnostic, and treatment charges. Apply concessions based on patient category, validate billing constraints, and classify patients according to the payment policy.

## 2. Algorithm

1. Start.
2. Read patient name and patient category.
3. Input consultation, diagnostic, and treatment charges.
4. Validate that all charges are non-negative.
5. Calculate the total bill.
6. Apply a concession based on the patient category.
7. Calculate the final bill.
8. Classify the payment status.
9. Display the bill details.
10. Stop.

## 3. Flowchart

Start

Input patient details and charges

Are charges non-negative?

Yes

Calculate total bill

Apply concession

Calculate final bill

Classify payment status

Display bill

Stop

No

Display invalid charges

Stop

## 4. Python Source Code

```
name = input("Enter patient name: ")consultation = float(input("Consultation charge: "))diagnostic = float(input("Diagnostic charge: "))treatment = float(input("Treatment charge: "))category = input("Patient category (senior/regular): ").lower()paid = input("Payment completed? (yes/no): ").lower()if consultation < 0 or diagnostic < 0 or treatment < 0:    print("Invalid charges")elif category not in ["senior", "regular"]:    print("Invalid patient category")elif paid not in ["yes", "no"]:    print("Invalid payment status")else:    total = consultation + diagnostic + treatment    if category == "senior":        concession = total * 0.10    else:        concession = 0    final_bill = total - concession    if paid == "yes":        status = "Paid"    else:        status = "Payment Pending"    print("\n--- HOSPITAL BILL ---")    print("Patient Name:", name)    print("Patient Category:", category)    print("Total Charges: Rs.", round(total, 2))    print("Concession: Rs.", round(concession, 2))    print("Final Bill: Rs.", round(final_bill, 2))    print("Payment Status:", status)
```

## 5. Sample Input

```
Enter patient name: Ravi
Consultation charge: 500
Diagnostic charge: 1000
Treatment charge: 2500
Patient category (senior/regular): senior
Payment completed? (yes/no): no
```

## 6. Sample Output

```
--- HOSPITAL BILL ---
Patient Name: Ravi
Patient Category: senior
Total Charges: Rs. 4000.0
Concession: Rs. 400.0
Final Bill: Rs. 3600.0
Payment Status: Payment Pending
```

## 7. Result

The program calculates the hospital bill, applies a 10% concession for senior patients, validates the inputs, and displays the patient's final bill and payment status.

Note: The concession and classification rules are sample policies and can be changed according to the policy provided by your college.
