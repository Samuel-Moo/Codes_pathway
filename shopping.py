print("Welcome to the Shopping Cart program!")

decision = 0
cart = [] 
prices = []
total = 0

while decision != 5: 
    print("""\nPlease select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit""")
    decision = int(input("Please enter an action: "))
    if decision == 1:
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))
        print(f"'{item}' has been added to the cart.")
        cart.append(item)
        prices.append(price)
    
    if decision == 2:
        print("The items in the list are: ")
        for i, k in enumerate(range(len(cart))):
            print(f"{k + 1}. {cart[i]} - ${prices[i]}")
                

    if decision == 3:
        remove = int(input("Which item would you like to remove? "))
        remove += -1
        if remove > (len(cart)):
            print("Sorry, that is not a valid number")
        else:
            cart.pop(remove)
            prices.pop(remove)
            print("Item removed")

    
    if decision == 4:
        for x in prices:
            total += x
        print(f"The total price of the items is ${total:.2f}")

print("Thank you. Goodbye. ")