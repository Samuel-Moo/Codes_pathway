accounts = []
balances = []
account = ""
balance = 0
total = 0
average = 0

print("Enter the names and balances of bank accounts (type: quit when done)")

while account != "quit":
    account = input("What is the name of this account? ")
    if account != "quit":
        accounts.append(account)
        balance = float(input("What is the balance? "))
        balances.append(balance)


print("\nAccount information: ")

for i in range(len(accounts)):
    account = accounts[i]
    balance = balances[i]
    print(f"{account} - ${balance:.2f}")

for balance in balances: 
    total += balance

print(f"Total: ${total:.2f}")

average = total / len(balances)

print(f"Average: ${average}")