# ***************************************************************************
#
# Author: Paul Littrell & Robyn Washburn
# Lab:    CIS-133Y Lab4
# Date:   October 13, 2026
# Desc:   Main driver program for the Road Trip Planner. Displays a menu,
#         validates user input to prevent crashes, and imports modular
#         functions from separate partner files to calculate fuel costs and
#         hotel expenses.
#
# Input:  Menu choices, driving distance, vehicle MPG, gas price per gallon,
#         nightly room rate, number of nights, and hotel tax rate percentage.
# Output: Estimated total road trip fuel cost and total hotel expenses
#         including local taxes.
# Source: Module 4 Lab 4
# GitHub: https://github.com/plittrell-pcc/CIS-133Y-Lab4
#
# ***************************************************************************

# **********
# Sample Run
# **********

# ===========================================================
#                WELCOME TO THE ROAD TRIP PLANNER
# ===========================================================
# This program helps you calculate your total road trip fuel
# costs and estimate your hotel and lodging expenses.
#
# Please follow the prompts below to get started!
#
# -----------------------------------------------------------
#
# --- MAIN MENU ---
#
# 1. Calculate Road Trip Fuel Cost
# 2. Calculate Hotel & Lodging Expense
# 3. Quit Program
# Enter your choice (1-3): 1
#
# --- Road Trip Fuel Cost Calculator ---
# Enter total driving distance in miles: 350
# Enter your vehicle's fuel efficiency (MPG): 26
# Enter current price per gallon of gas ($): 4.79
#
# -> Estimated Total Fuel Cost: $64.48
#
# --- MAIN MENU ---
#
# 1. Calculate Road Trip Fuel Cost
# 2. Calculate Hotel & Lodging Expense
# 3. Quit Program
# Enter your choice (1-3): 2
#
# --- Hotel and Lodging Cost Calculator ---
# Enter the room rate: 89.99
# Enter the number of nights: 4
# Enter tax (ex. 7.5%) or zero if none: 8.9
# -> Room Subtotal: $359.96
# -> Total Lodging Tax: $32.04
# -> Estimated Total Hotel Cost: $392.00
#
# --- MAIN MENU ---
#
# 1. Calculate Road Trip Fuel Cost
# 2. Calculate Hotel & Lodging Expense
# 3. Quit Program
# Enter your choice (1-3): 3
#
# Thank you for using the Road Trip Planner. Safe travels!


import fuel_module as f   # PL: Added module
import hotel_module as h  # RW: Added module


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


def get_menu_choice():
    while True:
        choice_input = input("Enter your choice (1-3): ")
        try:
            choice = int(choice_input)
            if choice in (1, 2, 3):
                return choice
            print("Error: Please enter 1, 2, or 3.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")


def display_fuel_results(total_cost):
    print(f"\n-> Estimated Total Fuel Cost: ${total_cost:.2f}\n")


def display_hotel_results(subtotal, tax, total_hotel):
    print(f"-> Room Subtotal: ${subtotal:.2f}")
    print(f"-> Total Lodging Tax: ${tax:.2f}")
    print(f"-> Estimated Total Hotel Cost: ${total_hotel:.2f}\n")


def main():
    print_welcome_message()

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            # PL: Call fuel module input and calculation functions
            distance, mpg, price = f.get_fuel_inputs()
            total_cost = f.calculate_fuel_cost(distance, mpg, price)
            display_fuel_results(total_cost)

        elif choice == 2:
            # RW: Call hotel module input and calculation functions
            room_price, nights, tax_rate = h.get_hotel_inputs()
            subtotal, tax, total_hotel = h.calculate_hotel_cost(
                room_price, nights, tax_rate
            )
            display_hotel_results(subtotal, tax, total_hotel)

        elif choice == 3:
            print("\nThank you for using the Road Trip Planner. Safe travels!")
            break


if __name__ == "__main__":
    main()
