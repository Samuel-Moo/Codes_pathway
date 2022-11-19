while inner_loop < 6:

    attempt = input()

    # Game logic
    output = ""
    for i in range(secret.__len__()):
        if guess[i] == secret[i]:
            output = output + Back.RED + attempt[i] + Back.RESET
        elif attempt[i] in word:
            output = output + Back.YELLOW + attempt[i] + Back.RESET
        else:
            output = output + attempt[i] + Back.RESET
    print(output)
    if word == attempt:
        print("Congrats")
        inner_loop = inner_loop + 6 # Reset game

    inner_loop = inner_loop + 1

def comparison(self):
    correct_position = 0
    correct_letter = 0

    for i,l in enumerate(self.guess):
        if l==self.word[i]:
            correct_position+=1
        elif l in self.word:
            correct_letter+=1

    print(
        f"{correct_position} letters in correct position, {correct_letter} correct letters in wrong position.")


word = "lunch"
counter = 0 
guess = ""
correct_position = False
correct_letter = False


while guess != word:
    guess = input("\nWhat is your guess? ")
    counter = counter + 1
    for position, letter in enumerate(guess):
        if letter == word[position]:
            correct_position = True
            if correct_position == True:
                letter = letter.capitalize()
        elif letter in word:
            correct_letter = True
            if correct_letter == True:
                letter = letter.lower()
        else:
            letter = "-"

        print(letter, end="")

print("\nCongratulations you guessed it! ")
print(f"It took you {counter} times" )