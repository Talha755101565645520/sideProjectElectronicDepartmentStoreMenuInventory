# Talha Hussain
# Side Project: Electronic Department Store Inventory Program Project in Python

import string
import math

def main():

    print("\t\tWelcome to Battery and Light Electronics Department Store\n")
    print("\t\tTalha Hussain, Owner\n")

    # Constants for menu choices.
    rechargeable_batteries_choice = 1
    regularbatteries_choice = 2
    lcd_light_bulbs_choice = 3
    halogen_light_bulbs_choice = 4
    exit_choice = 5

    # Variables for menu choice, item amount, subtotal price for the item, input coupon code, discount,
    # and grand total. 
    choice = 0
    item_amount = 0
    lcd_light_bulbs_one_or_two = 0
    number_of_lcd_light_bulbs = 0
    number_of_halogen_light_bulbs = 0
    coupon_code = ""
    recharge_battery_subtotal = 0.0
    regular_battery_subtotal = 0.0
    lcd_subtotal = 0.0
    halogen_subtotal = 0.0
    running_total_halogen = 0
    number_of_rechargeable_batteries = 0
    grand_total = 0.0

    rechargeable_batteries = 7.75
    regular_batteries_six_pack = 2.25
    regular_batteries_for_battery_one_code_six_pack = 1.50
    lcd_light_bulbs_one_pack = 4.00
    lcd_light_bulbs_two_pack = 5.50
    halogen_light_bulbs_one_to_five_pack = 5.99
    halogen_light_bulbs_six_to_ten_pack = 5.49
    halogen_light_bulbs_eleven_or_more_pack = 4.99

    while choice != exit_choice:
        while True:
            try:
                # Display the menu.
                print("Our Inventory: ")
                print("1. Rechargeable Batteries")
                print("2. Regular Batteries")
                print("3. LCD Light Bulbs")
                print("4. Halogen Light Bulbs")
                print("5. Exit\n")

                # Get User's Choice.
                choice = int(input("Please make a selection: "))

                # Validate the menu selection.
                if 1 <= choice <= 5:
                    break
                else:
                    print("Please enter a valid menu choice between 1 and 5.\n")
            except ValueError:
                print("You entered an Invalid Number or Character or Letter. Please enter a choice from 1-5: ")

        if choice == rechargeable_batteries_choice:
            while True:
                try:
                    item_amount = int(input("How many rechargeable batteries would you like to buy?: "))
                    if item_amount >= 0:
                        break
                    else:
                        print("Sorry, you have entered an Invalid Input, please enter positive whole number amounts only.\n")
                except ValueError:
                    print("You have entered an Invalid Number or Character or Letter.\n")
        
            number_of_rechargeable_batteries = item_amount + number_of_rechargeable_batteries
            recharge_battery_subtotal = item_amount * rechargeable_batteries
            print(f"\tThe subtotal for the Rechargeable Batteries is $: {recharge_battery_subtotal:.2f}\n") # Before ":.2f

        elif choice == regularbatteries_choice:
            while coupon_code != "battery1" and coupon_code != "NONE":
                coupon_code = input("Please type in a coupon code or NONE: ")

            while True:
                try:
                    item_amount = int(input("How many rechargeable batteries would you like to buy? "))
                    if item_amount >= 0:
                        break
                    else:
                        print("Sorry, you have entered an Invalid Input, please enter positive whole number amounts only.\n")
                except ValueError:
                    print("You entered an Invalid Number or Character or Letter.\n")
                    print("Please enter the number of regular batteries that you would like to buy: ")

            if coupon_code == "battery1":
                regular_battery_subtotal = item_amount * regular_batteries_for_battery_one_code_six_pack
                print(f"\tThe subtotal for the Rechargeable Regular Batteries is $: {regular_battery_subtotal:.2f}\n\n")
            elif coupon_code == "NONE":
                regular_battery_subtotal = item_amount * regular_batteries_six_pack
                print(f"\tThe subtotal for the Regular Batteries is $: {regular_battery_subtotal:.2f}\n\n")
            else:
                print("\tInvalid Input, please enter the coupon code battery1 or NONE.")

            # Display the Subtotal.
            print(f"\tThe subtotal for the Regular Batteries is $: {regular_battery_subtotal:.2f}\n\n")
        
        elif choice == lcd_light_bulbs_choice:
            # Reset the variable "lcd_light_bulbs_one_or_two"  for the while loop to iterate again and prompt the user to select the "lcd_light_bulbs_choice" for a second time.
            lcd_light_bulbs_one_or_two = 0
            while lcd_light_bulbs_one_or_two != 1 and lcd_light_bulbs_one_or_two !=2:
                while True:
                    try:
                        lcd_light_bulbs_one_or_two = int(input("Would you like to buy LCD Light Bulbs one at a time or two at a time (1 or 2)?"))
                        if lcd_light_bulbs_one_or_two == 1 or lcd_light_bulbs_one_or_two == 2:
                            break
                        else:
                            print("Invalid Input. Please say 1 or 2 for the number of times you would like to buy an LCD Light Bulb.\n")
                    except ValueError:
                        print("You have entered an Invalid Number or Character or Letter.\n")
                if lcd_light_bulbs_one_or_two == 1:
                    while True:
                        try:
                            number_of_lcd_light_bulbs = int(input("How many one packs of LCD Light Bulbs would you like to buy?: "))
                            if number_of_lcd_light_bulbs >= 0:
                                break
                            else:
                                print("Invalid Input. Sorry, you have an entered an Invalid Input. Please enter positive whole number values only.\n")
                        except ValueError:
                            print("You have entered an Invalid Number or Character or Letter.\n")
                    lcd_subtotal = number_of_lcd_light_bulbs * lcd_light_bulbs_one_pack
                    print(f"\tThe subtotal for LCD Light Bulbs is $: {lcd_subtotal:.2f}\n\n")
            
                elif lcd_light_bulbs_one_or_two == 2:
                    while True:
                        try:
                            number_of_lcd_light_bulbs = int(input("How many two packs of LCD Light Bulbs would you like to buy?: "))
                            if number_of_lcd_light_bulbs >= 0:
                                break
                            else:
                                print("Invalid Input. Sorry, you have entered an Invalid Input. Please enter positive whole number values only.\n")
                        except ValueError:
                            print("You have entered an Invalid Number or Character or Letter.\n")
                    lcd_subtotal = number_of_lcd_light_bulbs * lcd_light_bulbs_two_pack
                    print(f"\tThe subtotal for LCD Light Bulbs is $: {lcd_subtotal:.2f}\n\n")
                else:
                    print("\tInvalid Input.")
            
        elif choice == halogen_light_bulbs_choice:
            # Ask for the order quantity, calculate the total for the order, display the individual item price and the order total. Validate the number of Halogen
            # Lightbulbs that the customer will buy.
            while number_of_halogen_light_bulbs < 1:
                while True:
                    try:
                        number_of_halogen_light_bulbs = int(input("\tHow many halogen light bulbs would you like to buy?"))
                        if number_of_halogen_light_bulbs >= 1:
                            break
                        else:
                            print("Invalid Input. Sorry, you have entered an invalid input. Please enter whole positive numbers only.\n")
                    except ValueError:
                        print("You have entered an Invalid Number or Character or Letter.\n")

                running_total_halogen += number_of_halogen_light_bulbs
                print(f"Your running total is: {running_total_halogen:.2f}")

                if running_total_halogen >= 1 and running_total_halogen <= 5:
                    halogen_subtotal = running_total_halogen * halogen_light_bulbs_one_to_five_pack
                    print(f"\tThe subtotal for Halogen Light Bulbs is $: {halogen_subtotal}\n\n")
                elif running_total_halogen >= 6 and running_total_halogen <= 10:
                    halogen_subtotal = running_total_halogen * halogen_light_bulbs_six_to_ten_pack
                    print(f"\tThe subtotal for Halogen Light Bulbs is $: {halogen_subtotal}\n\n")
                elif running_total_halogen >= 11:
                    halogen_subtotal = running_total_halogen * halogen_light_bulbs_eleven_or_more_pack
                    print(f"\tThe subtotal for Halogen Light Bulbs is $: {halogen_subtotal}\n\n")
                else:
                    print("\tInvalid Input.")
                
        elif choice == exit_choice:
            print("\tThank you for ordering from Battery and Light.\n\n")

        else:
            print("\tSorry, we do not sell that item.\n\n")
            print("\tPlease make another selection.")

        if number_of_rechargeable_batteries >= 2:
            lcd_subtotal = lcd_subtotal / 2
        
        # Calculate the grand total.
        grand_total = recharge_battery_subtotal + regular_battery_subtotal + lcd_subtotal + halogen_subtotal
        
        # Display the total discount and grand total.
        print(f"Your total discount is $: {lcd_subtotal:.2f}\n")
        print(f"Your grand total is $: {grand_total:.2f}\n")

if __name__ == "__main__":
    main()



