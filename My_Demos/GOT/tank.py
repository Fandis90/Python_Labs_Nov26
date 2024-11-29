#! /usr/bin/env python3
# Author: ASlunka
# Version 1.0
# Description: This module describes a class of Tank for an online game

"""
  Tank Class
"""

class Tank:
    # a Class has Attributes/Data + Behaviour/Methods
    def __init__(self, country, model):
        # Constructor
        self.country = country
        self.model = model
        self._speed = 0
        self._direction = 0
        self._location = {'x':0, 'y':0, 'z':0}
        self._shells = 20
        self._health = 100
        # No explicit return as called IMPLICTLY/auto
    
    def accel(self, increase):
        self._speed += increase
        return None
    
    def decel(self, decrease):
        self._speed -= decrease
        return None
    
    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None
    
    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None
    
    def shoot(self):
        self._shells -= 1
        return None
    
    def take_damage(self, damage):
        self._health -= damage
        return None
    
    def __del__(self):
        #Destructor
        print("Boom..Boom")
        return None
    
    # And now for SOME special methods...
    # Example of OPERATOR overloading
    def __add__(self, other):
        return self._health + other._health
    
    # Getter Method
    def get_health(self):
        return self._health
    
    # Setter Method
    def set_health(self, neahealth):
        self._health = neahealth
        return None
    
    # Wrap ONE variable name interface to the two methods! (getter is always first)
    tank_health = property(get_health, set_health)

    # Example of DUCK TYPING, our tank can now QUACK like a string
    def __str__(self):
        return f"Model = {self.model}, health={self._health}, speed={self._speed}"