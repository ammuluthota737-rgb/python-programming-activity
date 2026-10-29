
n = int(input("Enter number of products: "))

items = []
subtotal = 0
total_tax = 0

for i in range(n):
    print("\nProduct", i + 1)
    name = input("Product name: ")
    category = input("Category (food/clothing/electronics): ").lower()
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    amount = price * quantity

    if category == "food":
        tax_rate = 0.05
    elif category == "clothing":
        tax_rate = 0.05
    elif category == "electronics":
        tax_rate = 0.18
    else:
        tax_rate = 0.10

    tax = amount * tax_rate
    subtotal += amount
    total_tax += tax

    items.append((name, quantity, amount, tax))

# Threshold discount with maximum concession
if subtotal >= 5000:
    discount = min(subtotal * 0.10, 1000)
elif subtotal >= 2000:
    discount = min(subtotal * 0.05, 500)
else:
    discount = 0

final_total = subtotal + total_tax - discount

print("\n========== ITEMIZED INVOICE ==========")
print(f"{'Product':15}{'Qty':>5}{'Amount':>12}{'Tax':>10}")

for name, qty, amount, tax in items:
    print(f"{name:15}{qty:>5}{amount:>12.2f}{tax:>10.2f}")

print("--------------------------------------")
print(f"Subtotal       : Rs. {subtotal:.2f}")
print(f"Total Tax      : Rs. {total_tax:.2f}")
print(f"Discount       : Rs. {discount:.2f}")
print(f"Final Bill     : Rs. {final_total:.2f}")
