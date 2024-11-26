#!/usr/bin/python3
import math

acceleration = 9.81 #m/s
velocity = 44 
theta = 80 #elevation angle
x = 0.5 #travel distance
height = 1 #meter

theta_rad = theta * (math.pi / 180)

y = height + x*math.tan(theta_rad) - (acceleration*x**2) / (2*(velocity*math.cos(theta_rad))**2)

print ("results are:", y)
