word = "lunch"
counter = 0 
guess = ""
correct_position = False
correct_letter = False


print("Welcome to the word guessing game! ")

while guess.lower() != word:
    guess = input("\nWhat is your guess? ")
    counter = counter + 1
    if len(guess) == len(word):
        for position, letter in enumerate(guess):
            
            if letter.lower() == word[i]:
                correct_position = True
                if correct_position == True:
                    letter = letter.capitalize()
            elif letter.lower() in word:
                correct_letter = True
                if correct_letter == True:
                    letter = letter.lower()
            else:
                letter = "-"
            
            print(letter, end="")
            
            
    else:
        print("The number of letters doesn't match, the word has " + str(len(word)) + " letters")    

print("\nCongratulations you guessed it! ")
print(f"It took you {counter} times" )