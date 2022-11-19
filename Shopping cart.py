print("Welcome to the Shopping Cart program!")

decision = 0
cart = [] 

while decision != 5: 
    print("""Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit""")
    decision = int(input("Please enter an action: "))
    if decision == 1:
        item = input("What item would you like to add? ")
        print(f"'{item}' has been added to the cart.")
        cart.append(item)
    
    if decision == 2:
        for individual_item in cart: 
            print(individual_item)

print("Thank you. Goodbye. ")