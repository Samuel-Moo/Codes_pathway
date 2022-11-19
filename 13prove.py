def calculate_wind_chill(Temp, Velo):
    return 35.74 + (0.6215 * Temp) - (35.75 * (Velo ** 0.16)) + (0.4275 * Temp * (Velo ** 0.16))

def convert_C_to_F(Temp):
    return (Temp * (9/5)) + 32 


#35.74 + 0.6215T - 35.75(V**0.16) + 0.4275T(V**0.16)

Velo = 0 
Temp = float(input("What is the temperature? "))
f_or_c = input("Fahrenheit or Celsius? (F/C) ")

if f_or_c == "C":
        Temp = convert_C_to_F(Temp)

while Velo != 60:
    Velo += 5
    wind_chill = calculate_wind_chill(Temp, Velo)
    print(f"At temperature {Temp}F, and wind speed {Velo} mph, the windchill is: {wind_chill:.2f}F")
