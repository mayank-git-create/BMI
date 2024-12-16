#!/usr/bin/env python3.6

# Function to gather user input
def gather_info():
    height = float(input("What is your height? (inches or meters) "))
    weight = float(input("What is your weight? (pounds or kilograms) "))
    system = input("Are your measurements in metric or imperial systems? ").lower().strip()
    return (height, weight, system)

# Function to calculate BMI based on the system (metric or imperial)
def calculate_bmi(weight, height, system='metric'):
    if system == 'metric':
        # BMI = weight (kg) / height (m^2)
        bmi = weight / (height ** 2)
    else:
        # BMI = 703 * weight (lb) / height (inches^2)
        bmi = 703 * (weight / (height ** 2))
    return bmi

# Main code to continuously ask for input until a valid system is provided
while True:
    height, weight, system = gather_info()
    
    if system.startswith('i'):
        # If the system is imperial
        bmi = calculate_bmi(weight, height, system='imperial')
        print(f"Your BMI is {bmi:.2f}")
        break  # Exit the loop after calculating BMI in imperial system
    elif system.startswith('m'):
        # If the system is metric
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi:.2f}")
        break  # Exit the loop after calculating BMI in metric system
    else:
        print("Invalid input! Please enter 'metric' or 'imperial' for the system.")
