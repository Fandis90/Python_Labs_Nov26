#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This module

"""
  Docstring
"""
import sys
import tank

def main():
    #Create/Instantiate 3 new Tank Objects..
    tom_tank = tank.Tank("german", "tiher")
    chri_tank = tank.Tank("america", "sherman")
    naoki_tank = tank.Tank("british","churchil")

    # And the game begins
    tom_tank.accel(64)
    chri_tank.accel(31)

    naoki_tank.rotate_left(289)
    naoki_tank.accel(27)
    naoki_tank.shoot()

    # ..and sucess.
    tom_tank.take_damage(59)
    chri_tank.take_damage(39)

    # And now some game visuals
    # print(f"Heath of Thomas the tank is {tom_tank._health}") # POOR CODE!

    # This is an example of operator overloading
    print(f"the health of Thomas and Chris's Tanks = {tom_tank + chri_tank}")

    # Thomas has received a health boost
    # tom_tank._health = 100 # DO NOT ACCESS PRIVATE Variables
    #print(f"New health of Thomas's tank is {tom_tank._health}")

    # Better to use SETTER AND GETTER methods
    tom_tank.set_health(101)
    print(f"new health of Thomas tank is {tom_tank.get_health()}")

    tom_tank.tank_health = 102
    print(f"new health of Thomas tank is {tom_tank.tank_health}")

    print(f"Status of Thomas tank = {tom_tank}")

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)