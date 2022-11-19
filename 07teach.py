import random

play_again = "yes"

while play_again.lower() == "yes":
    
    magic = random.randint(1,100)

    guess = -1

    times_guessed = 0 
    
    
    while guess != magic:
        guess = int(input("What is your guess? "))
        times_guessed = times_guessed + 1

        if guess < magic:
            print("Higher")
        elif guess > magic:
            print("Lower")       
        else: 
            print("You guessed it!")

    print(f"You guessed {times_guessed} times.")

    play_again = input("Do you want to play again? (yes/no) ")

print("Thank you for playing goodbye.")
