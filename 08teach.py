word = "Commitment"

favorite = input("What is your favorite letter? ")

for capital in word.lower():
    if capital == favorite.lower():
        capital = "_"        
    print(capital, end="")
