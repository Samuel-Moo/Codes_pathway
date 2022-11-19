numbers = []
new_number = -1
counter = 0

print('Enter a list of numbers, type 0 when finished.')

while new_number != 0:
    counter += 1
    new_number = int(input('Enter number: '))
    if new_number != 0:
        numbers.append(new_number)

total = 0

for new_number in numbers:
    total += new_number

print(f'The sum is: {total}')

average = total / (counter - 1)

print(f"The average is {average:.2f}")

max_numbers = max(numbers)

print(f"The largest number is {max_numbers}") 

numbers.sort()

print(numbers)