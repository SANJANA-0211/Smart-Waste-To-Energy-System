# Smart Waste to Energy Simulator 🌱⚡

print("Welcome to Smart Waste System\n")

# Taking multiple inputs
food_waste = float(input("Enter food waste (kg): "))
plant_waste = float(input("Enter plant waste (kg): "))

# Total waste
total_waste = food_waste + plant_waste

# Biogas calculation
biogas = total_waste * 0.1

# Energy calculation
energy = biogas * 2

# Output
print("\n--- Smart Report ---")
print(f"Total Waste: {total_waste} kg")
print(f"Biogas: {biogas:.2f} m³")
print(f"Energy: {energy:.2f} kWh")

# Smart suggestion
if total_waste > 30:
    print("High waste detected! Add more bins in this area 🚮")
else:
    print("Waste level normal ✅")

# Usage estimate
print("\n--- Usage ---")
print(f"Wi-Fi: {energy*4:.0f} hours")
print(f"Street Lights: {energy/2:.0f} lights (5 hrs)")
