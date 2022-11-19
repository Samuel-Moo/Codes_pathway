#v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
import math

print("Welcome to the velocity calculator. Please enter the following: ")
mass = float(input("\nMass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
csa = float(input("Cross sectional area (in m^2): "))
drag = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

drag_2 = (1/2) * density * csa * drag
velocity = (math.sqrt(mass * gravity / drag_2)) * (1 - math.exp((- math.sqrt(mass * gravity * drag_2) / mass ) * time))

print(f"\nThe inner value of c is: {drag_2:.3f}")
print(f"The velocity after {time} seconds is: {velocity:.3f} m/s ")