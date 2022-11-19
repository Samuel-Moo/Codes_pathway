max_life = -1
max_country = ""
max_year = 0

min_life = 999
min_country = ""
min_year = 0 

year_input = int(input("Enter the year of interest: "))
sum_life_input = 0 
average_life_input = 0 
counter_input = 0
min_life_input = 999
max_life_input = -1
max_country_input = ""
min_country_input = ""

with open("life-expectancy.csv") as file:
    next(file)
    
    for words in file:
        
        words1 = words.strip()
        words2 = words1.split(",")
        
        country = words2[0]
        code = words2[1]
        year = int(words2[2])
        life_expectancy = float(words2[3])

        if life_expectancy > max_life:
            max_life = life_expectancy
            max_country = country
            max_year = year 
        
        if life_expectancy < min_life:
            min_life = life_expectancy
            min_country = country
            min_year = year
        
        if year_input == year:
            counter_input += 1
            sum_life_input += life_expectancy
            average_life_input = sum_life_input / counter_input

            if life_expectancy > max_life_input:
                max_life_input = life_expectancy
                max_country_input = country
            
            if life_expectancy < min_life_input:
                min_life_input = life_expectancy
                min_country_input = country

print(f"The overall max life expectancy is: {max_life:.2f} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life:.2f} from {min_country} in {min_year}")
print(f"For the year {year_input}: \nThe average life expectancy was: {average_life_input:.2f} ")
print(f"The max life expectancy was in {max_country_input} with {max_life_input:.2f} \nThe min life expectancy was in {min_country_input} with {min_life_input:.2f} ")



