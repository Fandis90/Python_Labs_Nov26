fuel_per_lap = 2.25 #kg
lap_count = 45
min_requirement = fuel_per_lap * lap_count
contingency = min_requirement * 0.5
total_fuel = min_requirement + contingency
print(min_requirement, contingency, total_fuel)
