"""
Created by: Devon
Created on: Feb 2026
This module is a Micro:bit MicroPython program that does basic math.
"""


from microbit import *


sleep(1000)
display.scroll("A rectangle has dimensions 5cm and 3cm")


display.scroll("The perimeter: 2(5+3)" + (2 * (5 + 3) ) + " cm")


display.scroll("The area: 5x3 " + 5*3 + " cm^2")
