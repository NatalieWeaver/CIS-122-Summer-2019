'''
Author: Natalie Weaver
Date:   July 30, 2019

CIS 122 Challenge Set 4 Part 3
Drawing barcodes

Sources: None
'''

import argparse	# Used in main program to obtain 5-digit ZIP code from command line
import time	# Used in main program to pause program before exit
import turtle	# Used in your function to print the bar code

## Constants used by this program
SLEEP_TIME = 30	# number of seconds to sleep after drawing the barcode
ENCODINGS = [[1, 1, 0, 0, 0],	# encoding for '0'
             [0, 0, 0, 1, 1],	# encoding for '1'
             [0, 0, 1, 0, 1],   # encoding for '2'
             [0, 0, 1, 1, 0],	# encoding for '3'
             [0, 1, 0, 0, 1],	# encoding for '4'
             [0, 1, 0, 1, 0],	# encoding for '5'
             [0, 1, 1, 0, 0],	# encoding for '6'
             [1, 0, 0, 0, 1],	# encoding for '7'
             [1, 0, 0, 1, 0],	# encoding for '8'
             [1, 0, 1, 0, 0]	# encoding for '9'
            ]
SINGLE_LENGTH = 25	# length of a short bar, long bar is twice as long

def compute_check_digit(digits):
    """
    Compute the check digit for use in ZIP barcodes
    args:
        digits: list of 5 integers that make up zip code
    returns:
        check digit as an integer
    """
    sum = 0
    for i in range(len(digits)):
        sum = sum + digits[i]
    check_digit = 10 - (sum % 10)
    if (check_digit == 10):
        check_digit = 0
    return check_digit


def draw_bar(digit):
    '''
    (? , int) -> None
    In Turtle, draws a single bar of the barcode, with length SINGLE_LENGTH if the digit
    is 0, and length twice SINGLE_LENGTH if the digit is 1. Returns None.
    '''
    turtle.left(90)
    if digit == 0:
        length = SINGLE_LENGTH
    else:
        length = 2 * SINGLE_LENGTH
    turtle.forward(length)
    turtle.up()
    turtle.backward(length)
    turtle.right(90)
    turtle.forward(10)
    turtle.down()

    return None


def draw_zip(my_turtle, zip):
    '''
    () -> None
    Using Turtle, draws the barcode associated to the zip code + check digit.
    '''

    digit5 = zip % 10
    digit4 = (zip % 100 - digit5) // 10
    digit3 = (zip % 1000 - (digit4 * 10 + digit5)) // 100
    digit2 = (zip % 10000 - (digit3 * 100 + digit4 * 10 + digit5)) // 1000
    digit1 = (zip - (digit2 * 1000 + digit3 * 100 + digit4 * 10 + digit5)) // 10000
    check_digit = compute_check_digit([digit1, digit2, digit3, digit4, digit5])

    bar_digits = [1] + ENCODINGS[digit1] + ENCODINGS[digit2] + ENCODINGS[digit3] + ENCODINGS[digit4] + ENCODINGS[digit5] + ENCODINGS[check_digit] + [1]

    for digit in bar_digits:
        turtle.tracer(0, 0)
        draw_bar(digit)
        turtle.update()

    return None

# What's up with all this my_turtle stuff? and how does the main function work?

##def main():
##    parser = argparse.ArgumentParser()
##    parser.add_argument("ZIP", type=int)
##    args = parser.parse_args()
##    zip = args.ZIP
##    if zip <= 0 or zip > 99999:
##        print("zip must be > 0 and < 100000; you provided", zip)
##    else:
##        my_turtle = turtle.Turtle()
##        draw_zip(my_turtle, zip)
##        time.sleep(SLEEP_TIME)
##
##if __name__ == "__main__":
##    main()
