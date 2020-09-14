from random import randint
import re
from time import sleep
from faker import Faker
from tabulate import tabulate
import dndutils

faker = Faker()

while True:

    coins = {"cp": 0, "sp": 0, "ep": 0, "gp": 0, "pp": 0}

    print("\n****************** DnD Tools v0.7.1 ******************")
    print("|  Press '1' to access the Coin Converter.           |")
    print("|  Press '2' to access the Coin Splitter.            |")
    print("|  Press '3' to access the Dice Roller.              |")
    print("|  Press '4' to access the Random Name Generator.    |")
    print("|  Press '5' to access the Leveling Chart.           |")
    print("|  Press 'Q' to quit.                                |")
    print("******************************************************\n")
    select = input("What is your selection? ")

    if select == "Q" or select == 'q':
        quit()

    elif int(select) == 1:  # COIN CONVERTER

        for key in coins:  # gathering amounts of each coin
            while True:  # input validation
                try:
                    coins[key] = int(input(f"How much {key}? "))
                    if coins[key] < 0:
                        print("You must enter only positive numbers.")
                        continue
                    break
                except ValueError:
                    print("You must enter a valid number.")

        while True:  # validating user input to find out if gold should be converted
            do_all = input("Do you want to convert your gold? (Y/N) ").lower()

            if do_all != "y" or do_all != "n":
                break
            else:
                continue

        calc = dndutils.Coinage(coins['cp'], coins['sp'], coins['ep'],
                                coins['gp'], coins['pp'])

        if do_all == "y":
            print(calc.convert(do_all))

        else:
            print(calc.convert())

        sleep(3)

    elif int(select) == 2:  # COIN SPLITTER
        while True:
            try:
                party = int(input("How big is your party? "))
                if party < 0:
                    print("You must enter only positive numbers.")
                    continue
                break
            except ValueError:
                print("You must enter a valid number.")

        for key in coins:  # gathering amounts of each coin
            while True:  # input validation
                try:
                    coins[key] = int(input(f"How much {key}? "))
                    if coins[key] < 0:
                        print("You must enter only positive numbers.")
                        continue
                    break
                except ValueError:
                    print("You must enter a valid number.")

        calc = dndutils.Coinage(coins['cp'], coins['sp'], coins['ep'],
                                coins['gp'], coins['pp'])

        coin_split = calc._downconvert()  # converting all coin to copper

        leftovers = coin_split % party  # calculating remainder
        split = coin_split // party  # calculating each players portion

        split_calc = dndutils.Coinage(
            split)  # upconverting from copper to prepare results for printing

        print(split_calc.calc_party())
        if leftovers > 0:  # displaying leftovers if applicable
            print(f"There is an additional {leftovers} copper left over.")

        sleep(3)

    elif int(select) == 3:  # DICE ROLLER

        print("How to use the Dice Roller...")
        print("You will input whatever you'd like to roll, plus modifiers.")
        print("ex: 4d6, 3d20, 6d20+1, etc. will all work.\n")

        while True:  # input validation
            dice_input = input(
                "What kind of die do you want to roll? (4d6, etc.) ")
            # checking for dice input follows format #d# or #d#+# or #d#-#
            valid_input = re.search(
                r"^[1-9][0-9]{0,2}[dD][1-9][0-9]{0,2}$|^[1-9][0-9]{0,2}[dD][1-9][0-9]{0,2} ?[\+\-][0-9]+$",
                dice_input)

            if valid_input != None:
                break

            else:
                print("\nPlease enter a valid input.")
                continue

        # splitting off die for calculations -- dice[0] == total dice, dice[1] == sided die, dice[2] == modifier
        dice = re.split(r"[dD\+\-]", dice_input)

        # determining what modifiers to use (if any)
        dice_mod = re.findall(r"[\+\-]", dice_input)

        if "+" in dice_mod:
            roll = [randint(1, int(dice[1])) for val in range(int(dice[0]))]
            roll_total = sum(roll) + int(dice[2])

        elif "-" in dice_mod:
            roll = [randint(1, int(dice[1])) for val in range(int(dice[0]))]
            roll_total = sum(roll) - int(dice[2])

        else:
            roll = [randint(1, int(dice[1])) for val in range(int(dice[0]))]
            roll_total = sum(roll)
            dice.append(0)  # for printing purposes
            dice_mod.append("+")  # for printing purposes

        print(f"{roll} {dice_mod[0]}{dice[2]} -- TOTAL: {roll_total}")

        sleep(2)

    elif int(select) == 4:  # NAME GENERATOR

        print("Press '1' to get first names only.")
        print("Press '2' to get full names.")

        while True:
            select = input("What kind of names would you like? ")

            if int(select) == 1:
                print("Press '1' for male.")
                print("Press '2' for female.")
                print("Press '3' to get 5 random names.")  # male and female

                while True:
                    select = input("What would you like? ")

                    if int(select) == 1:
                        print(faker.first_name_male())

                    elif int(select) == 2:
                        print(faker.first_name_female())

                    elif int(select) == 3:
                        for i in range(5):
                            print(faker.first_name())

                    else:
                        print("Please pick a valid option.")
                        continue

                    break

            elif int(select) == 2:
                print("Press '1' for male.")
                print("Press '2' for female.")
                print("Press '3' to get 5 random names.")  # male and female

                while True:
                    select = input("What would you like? ")

                    if int(select) == 1:
                        print(faker.name_male())

                    elif int(select) == 2:
                        print(faker.name_female())

                    elif int(select) == 3:
                        for i in range(5):
                            print(faker.name())

                    else:
                        print("Please pick a valid option.")
                        continue

                    break

            else:
                print("Please pick a valid option.")
                continue

            break

        sleep(3)

    elif int(select) == 5:  # LEVEL CHART

        headers = ["Experience", "Level",
                   "Prof. Bonus"]  # headers for leveling table
        table = [
            ["0", "1", "+2"], # table contents
            ["300", "2", "+2"],
            ["900", "3", "+2"],  
            ["2,700", "4", "+2"],
            ["6,500", "5", "+3"],
            ["14,000", "6", "+3"],
            ["23,000", "7", "+3"],
            ["34,000", "8", "+3"],
            ["48,000", "9", "+4"],
            ["64,000", "10", "+4"],
            ["85,000", "11", "+4"],
            ["100,000", "12", "+4"],
            ["120,000", "13", "+5"],
            ["140,000", "14", "+5"],
            ["165,000", "15", "+5"],
            ["195,000", "16", "+5"],
            ["225,000", "17", "+6"],
            ["265,000", "18", "+6"],
            ["305,000", "19", "+6"],
            ["355,000", "20", "+6"]
        ]

        print()
        print(tabulate(table, headers, tablefmt="fancy_grid"))
        select = input("Press any key to return to the main menu. ")
        if select:
            continue

    else:
        print("Please pick a valid menu option.")
        continue