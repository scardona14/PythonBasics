weight = 4.6
# Ground Shipping

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight <= 10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20

cost_ground = "{:.2f}" .format(cost_ground)
print("Ground Shipping Price: $" + str(cost_ground))

cost_premium = 125

print("Premium Shipping Price: $" + str(cost_premium))

# Drone Shipping

if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9.0
elif weight <= 10:
  cost_drone = weight * 12.0
else:
  cost_drone = weight * 14.25

cost_drone = "{:.2f}" .format(cost_drone)
print("Drone Shipping Price: $" + str(cost_drone) + "\n")

cost_ground = float(cost_ground)
cost_premium = int(cost_premium)
cost_drone = float(cost_drone)

if cost_ground < cost_premium and cost_ground < cost_drone:
  print("Ground Shipping is the cheapest option.")
elif cost_premium < cost_ground and cost_premium < cost_drone:
  print("Premium Shipping is the cheapest option.")
elif cost_drone < cost_ground and cost_drone < cost_premium:
  print("Drone Shipping is the cheapest option.")
else:
  print("It is your choice to make.")