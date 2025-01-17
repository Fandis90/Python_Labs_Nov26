#! /usr/bin/env python3
# Author: ASlunka
# Description: This script will simulate a high street bank PIN machine

import getpass

master_pin = "0123"
pin = None #undifined but declared
attempts = 0

while pin != master_pin and attempts <3: 
    pin = getpass.getpass("Enter PIN:" )
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
        attempts += 1
else:
    # Executes only once, when while condition becomes False
    print("Too many attempts")
    print("Your card has been retained. Have a nice day")

print("Done.")