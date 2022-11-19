f_number = int(input("What is the first number? "))
s_number = int(input("What is the second number? "))

if f_number > s_number:
    print("\nThe first number is greater.")
else: 
    print("The first number is not greater.")

if f_number == s_number:
    print("The numbers are equal.")
else: 
    print("The numbers are not equal.")

if f_number < s_number:
    print("The second number is greater.")
else: 
    print("The second number is not greater.")


animal = input("\nWhat is your favorite animal? ")

if animal.lower() == "ducks":
    print("That is my favorite too!")
else:
    print("That one is not my favorite.")