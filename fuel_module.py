# ****************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-133Y Lab4
# Date:   October 13, 2026
# Desc:   Fuel module containing input validation and calculation functions
#         for road trip fuel costs.
#
# ****************************************************************************

def get_fuel_inputs():
    print("\n--- Road Trip Fuel Cost Calculator ---")

    # Validate distance
    while True:
        try:
            distance = float(input("Enter total driving distance in miles: "))
            if distance > 0:
                break
            print("Error: Value must be greater than zero.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

    # Validate MPG
    while True:
        try:
            mpg = float(input("Enter your vehicle's fuel efficiency (MPG): "))
            if mpg > 0:
                break
            print("Error: Value must be greater than zero.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

    # Validate price per gallon
    while True:
        try:
            price_per_gal = float(input("Enter current price per gallon of gas ($): "))
            if price_per_gal > 0:
                break
            print("Error: Value must be greater than zero.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

    # Return the inputs as a tuple so main.py can pass them to the calculation function
    return distance, mpg, price_per_gal


def calculate_fuel_cost(distance_miles, mpg, price_per_gallon):

    if mpg == 0:
        return 0.0

    gallons_needed = distance_miles / mpg
    total_cost = gallons_needed * price_per_gallon
    return round(total_cost, 2)