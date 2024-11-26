fuel_per_lap = 2.25 #kg
lap_count = 45
min_requirement = fuel_per_lap * lap_count
contingency = min_requirement * 0.5
fuel_at_start = min_requirement + contingency

qualify_lap = 80.45
time_loss = fuel_at_start / 10 * 0.35

print("time lost at start:", time_loss)

first_lap_time = qualify_lap + time_loss
print("first lapt time:", first_lap_time)

