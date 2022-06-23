"""""
This file's intent is to accept a user's input weight in pounds or kilograms,
and output their converted weight

by: KPM - 6.22.2022
"""

CONVERSION = 2.204623 # 1KG = 2.2 LBs
weight_value = float(input("Please enter your weight: "))
weight_unit = input("Specify unit of measure: [K]g or [L]b:").capitalize() # All checks will be in capital letters

# Catch if someone enters the wrong character
while not (weight_unit == 'K' or weight_unit == 'L'):
    weight_unit = input("Please specify the correct unit of measure: [K]g or [L]b: ").capitalize()

if(weight_unit == 'K'):
    print(f'Your Weight in Lb is: {round(weight_value*CONVERSION, 0)}')
else:
    print(f'Your Weight in Kg is: {round(weight_value/CONVERSION, 1)}')

print("Thank you for using the weight calculator")