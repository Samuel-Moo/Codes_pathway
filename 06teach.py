first_age = int(input('What is the age of the first person? '))
first_height = float(input('What is the height of the first person(in inches)? '))
second_rider = input('Is there a second rider (Yes/No)? ')

if second_rider.capitalize() == 'Yes':
    second_age = int(input('What is the age of the second rider? '))
    second_height = int(input('What is the height of the second rider(in inches)? '))
    #implement the rules
    if first_height < 36 or second_height < 36:
        can_ride = False
    else:
        if first_age >= 18 or second_age >= 18:
         can_ride = True
        else:
         can_ride = False

else:
    if first_age >= 18 and first_height >= 62:
      can_ride = True
    else:
        can_ride = False

if can_ride == False:
    if first_height > 52 and second_height > 52 and first_age >= 12 and second_age >= 12:
        can_ride = True

    


if can_ride:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you may not ride.')