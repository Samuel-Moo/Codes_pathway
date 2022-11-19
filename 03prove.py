child_meal = float(input("What is the price of a chid's meal? "))
adult_meal = float(input("what is the price of an adult's meal? "))
number_children = int(input("How many children are there? "))
number_adults = int(input("How many adults are there? "))
tax_percentage = float(input("What is the percentage of sales taxes? "))
tip = float(input("What percentage do you wish to leave as tip? "))

subtotal = (child_meal * number_children) + (adult_meal * number_adults)
print(f"\nSubtotal: ${subtotal:.2f}")

total_tip = subtotal * tip / 100 
print(f"Tip: ${total_tip:.2f}")

taxes = subtotal * tax_percentage / 100
print(f"Taxes: ${taxes:.2f}")

total = subtotal + taxes + total_tip
print(f"Total: ${total:.2f}")

payment = float(input("\nWhat is the payment amount? "))
change = payment - total
print(f"Change: ${change:.2f}")