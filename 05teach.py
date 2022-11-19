score = float(input('What is your grade percentage? '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
elif score < 60:
    grade = 'F'

remainder = score % 10 

if remainder >= 7:
    sign = "+"
elif remainder <= 3:
    sign = "-"
else: sign = ""

if score >= 93:
    sign = ''
elif grade == 'F':
    sign = ''   

print(f"{grade}{sign}")

if score <= 69:
    print("Keep trying.")
else:
    print('Good job! Keep going!.')



