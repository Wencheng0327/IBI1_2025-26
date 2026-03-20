#3

import matplotlib.pyplot as plt
import numpy as np

# Population data
population_2020 = {
    "UK": 66.7,
    "China": 1426,
    "Italy": 59.4,
    "Brazil": 208.6,
    "USA": 331.6
}
population_2024 = {
    "UK": 69.2,
    "China": 1410,
    "Italy": 58.9,
    "Brazil": 212.0,
    "USA": 340.1
}

# Calculate population growth rate
growth_rate = {}
for country in population_2020:
    rate = ((population_2024[country] - population_2020[country]) / population_2020[country]) * 100
    growth_rate[country] = rate

# Sort from largest increase to largest decrease
sorted_growth = sorted( growth_rate.items(), key = lambda x: x[1], reverse = True )
print("\nSorted population growth rates:")
for country, rate in sorted_growth:
    print( f"{country}: {rate:.2f}%" )

# Find largest increase and decrease
largest_increase = max(growth_rate, key=growth_rate.get)
largest_decrease = min(growth_rate, key=growth_rate.get)

print(f"\nLargest increase: {largest_increase}")
print(f"Largest decrease: {largest_decrease}")

# Prepare data for bar chart
countries = [country for country, rate in sorted_growth]
rates = [rate for country, rate in sorted_growth]
bars = plt.bar(countries, rates)

plt.title("Population Growth Rate (2020-2024)")
plt.xlabel("Countries")
plt.ylabel("Growth Rate (%)")
plt.yticks(np.arange(-2, 5, 1))
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.axhline(0, color='black', linewidth=0.8)

# Show values on top of bars
for bar in bars:
    height = bar.get_height()
    if height >= 0:
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.2f}%",
            ha='center',
            va='bottom'
        )
    else:
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.2f}%",
            ha='center',
            va='top'
        )

plt.show()