secret = ["mosiah"]
letters_secret = len(secret)
counter = 0 
guess = ""

while guess.lower() != secret:
    counter = counter + 1
    guess = input("Guess: ")

    
    letter = ""
    for i in range(secret.__len__()):
        if guess[i] == secret[i]:
            letter = guess[i].capitalize
        elif guess[i] in secret[i]:
            letter = guess[i].lower
        else:
            letter = "_"
    print(letter)
    
        
    
#else:
#    print("The number of letters doesn't match, try again")
    
        

print("Congratulations you guessed it!")
print(f"It took you {counter} guesses")


