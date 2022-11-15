#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Nov. 10, 2022
# a program that calculates the the square of
# all the numbers proceeding and including a given number


def main():
    # variables
    user_num_string = input("Please enter a whole number: ")

    # exception handling
    try:
        user_num_int = int(user_num_string)

    # input wasn't an integer
    except Exception:
        print("Input invalid! Please enter a WHOLE number!")

    # input is valid
    else:
        # checks if num is negative
        if user_num_int < 0:
            print("Input invalid! Please enter a WHOLE number!")

        # squares all numbers up to and including user num
        for counter in range(0, user_num_int + 1):
            num_squared = counter**2
            print(f"{user_num_int}^2 = {num_squared}")

    # final message regardless of input
    finally:
        print("Thank you for using this program!")


if __name__ == "__main__":
    main()
