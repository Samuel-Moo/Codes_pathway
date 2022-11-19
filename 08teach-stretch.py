word = """In coming days, it will not be possible to survive spiritually without
 the guiding, directing, comforting, and constant influence of the Holy Ghost."""

favorite = int(input("Please enter a number: "))

for i, capital in enumerate(word.lower()):
    if i % favorite == 0:
        capital = capital.upper()
    
    print(capital, end="")
