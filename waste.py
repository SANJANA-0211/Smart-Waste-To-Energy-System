# Waste to Energy Simulator 🌱⚡

# Taking input from user
waste_kg = float(input("Enter amount of organic waste (in kg): "))

# Biogas calculation (approx)
biogas = waste_kg * 0.1   # 1kg ≈ 0.08–0.12 m³ → taking avg 0.1

# Energy calculation
energy = biogas * 2       # 1 m³ biogas ≈ 2 kWh

# Output results
print("\n--- Energy Report ---")
print(f"Waste processed: {waste_kg} kg")
print(f"Biogas produced: {biogas:.2f} m³")
print(f"Energy generated: {energy:.2f} kWh")

# Extra insight
if energy > 8:
    print("This can power Wi-Fi + street lights! 🌐💡")
else:
    print("Energy generated is small, but still useful 🌱")