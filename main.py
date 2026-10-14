# ****************************************************************************
#
# Author: Paul Littrell & Robyn Washburn
# Lab:    CIS-133Y Lab4
# Date:   October 13, 2026
# Desc:   Main driver program for the Road Trip Planner. Displays a menu,
#         validates user input to prevent crashes, and imports modular functions
#         from separate partner files to calculate fuel costs and hotel expenses.
#
# Input:  Menu choices, driving distance, vehicle MPG, gas price per gallon,
#         nightly room rate, number of nights, and hotel tax rate percentage.
# Output: Estimated total road trip fuel cost and total hotel expenses
#         including local taxes.
# Source: Module 4 Lab 4
# GitHub: https://github.com/plittrell-pcc/CIS-133Y-Lab4
#
# ****************************************************************************

import fuel_module
# import hotel_module  # Partner module (coming soon)

def print_welcome_message():
    print("===========================================================")
    print("               WELCOME TO THE ROAD TRIP PLANNER            ")
    print("===========================================================")
    print("This program helps you calculate your total road trip fuel ")
    print("costs and estimate your hotel and lodging expenses.        ")
    print("                                                           ")
    print("Please follow the prompts below to get started!          \n")
    print("-----------------------------------------------------------\n")

def display_menu():
    print("--- MAIN MENU ---\n")
    print("1. Calculate Road Trip Fuel Cost")
    print("2. Calculate Hotel & Lodging Expense")
    print("3. Quit Program")

def main():
    print_welcome_message()

    while True:
        display_menu()

        # Validate menu choice
        choice_input = input("Enter your choice (1-3): ")
        try:
            choice = int(choice_input)
            if choice == 1:
                # Call fuel module input and calculation functions
                distance, mpg, price = fuel_module.get_fuel_inputs()
                total_cost = fuel_module.calculate_fuel_cost(distance, mpg, price)
                print(f"\n-> Estimated Total Fuel Cost: ${total_cost:.2f}\n")
            elif choice == 2:
                print("\n[Notice] Hotel & Lodging calculation is coming soon (Partner section).\n")
            elif choice == 3:
                print("\nThank you for using the Road Trip Planner. Safe travels!")
                break
            else:
                print("Error: Please enter 1, 2, or 3.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")

main()