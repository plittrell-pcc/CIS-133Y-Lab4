# ***************************************************************************
# Author: Robyn Washburn
# Lab:    CIS-133Y Lab4
# Date:   October 15, 2026
# Desc:   Hotel module for input validation and calculation of hotel costs
#
# ***************************************************************************

def get_hotel_inputs():
    print("\n--- Hotel and Lodging Cost Calculator ---")

    # Validate room price
    while True:
        try:
            room_price = float(input("Enter the room rate: "))
            if room_price > 0:
                break
            print("Error: Please enter an amount greater than 0.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

    # Validate number of nights
    while True:
        try:
            nights = int(input("Enter the number of nights: "))
            if nights > 0:
                break
            print("Error: Value must be greater than zero.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")

    # Validate tax rate
    while True:
        try:
            tax_rate = float(input("Enter tax (ex. 7.5%) or zero if none: "))
            if tax_rate >= 0:
                break
            print("Error: Value cannot be less than zero. Try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

    return room_price, nights, tax_rate


# Calculate lodging costs
def calculate_hotel_cost(room_price: float, nights: int, tax_rate: float):
    subtotal = (nights * room_price)
    tax = subtotal * (tax_rate / 100)
    total_hotel = subtotal + tax
    return round(subtotal, 2), round(tax, 2), round(total_hotel, 2)