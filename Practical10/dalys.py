# import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir( "C:/cygwin64/home/Lenovo/IBI1_2025-26/Practical10" )
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Show the third and fourth columns (Year and DALYs)
# for the first 10 rows (inclusive, total 10 rows)
first_10_year_dalys = dalys_data.iloc[0:10, 2:4]
print("\nThird and fourth columns for the first 10 rows:")
print(first_10_year_dalys)

max_index_first10 = first_10_year_dalys["DALYs"].idxmax()

print("\nMaximum DALYs in the first 10 rows:")
print("Year:", first_10_year_dalys.loc[max_index_first10, "Year"])
print("DALYs:", first_10_year_dalys.loc[max_index_first10, "DALYs"])
# COMMENT: The year with the maximum DALYs across the first 10 years for which DALYs were recorded in Afghanistan is 1998 (DALYs: 86656.29)

# Show all years for which DALYs were recorded in Zimbabwe
zimbabwe_years = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]
print("\nAll years recorded for Zimbabwe:")
print(zimbabwe_years)

first_year_zimbabwe = zimbabwe_years.min()
last_year_zimbabwe = zimbabwe_years.max()
print("\nZimbabwe first and last recorded year:")
print("First year:", first_year_zimbabwe)
print("Last year:", last_year_zimbabwe)
# COMMENT: DALYs were recorded in Zimbabwe from 1990 to 2019 (first year: 1990, last: 2019)

# Countries with maximum and minimum DALYs in 2019
recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

max_row_2019 = recent_data.loc[recent_data["DALYs"].idxmax()]
min_row_2019 = recent_data.loc[recent_data["DALYs"].idxmin()]

print("\nCountry with maximum DALYs in 2019:")
print(max_row_2019)
print("\nCountry with minimum DALYs in 2019:")
print(min_row_2019)
# COMMENT: 
# The country with the maximum DALYs in 2019 is: Lesotho (DALYs: 90771.64)
# The country with the minimum DALYs in 2019 is: Singapore (DALYs: 15045.11)

# Plot DALYs over time for one of those countries: Lesotho
chosen_country = "Lesotho"
country_data = dalys_data.loc[dalys_data["Entity"] == chosen_country, ["Year", "DALYs"]]

plt.figure(figsize=(7, 4), dpi=150)
plt.plot(country_data["Year"], country_data["DALYs"], "bo--")
plt.xticks(country_data["Year"], rotation=-90)
plt.xlabel("Years")
plt.ylabel("DALYs")
plt.title(f"DALYs over time in {chosen_country}")
plt.tight_layout()
plt.show()

# Question: What was the distribution of DALYs across all countries in 2019?
question_data = dalys_data.loc[dalys_data["Year"] == 2019, "DALYs"]

plt.figure(figsize=(7, 4), dpi=150)
plt.hist(question_data, bins=30, edgecolor="black")
plt.xlabel("DALYs")
plt.ylabel("Number of countries")
plt.title("Distribution of DALYs across all countries in 2019")
plt.tight_layout()
plt.show()

print("\nSummary statistics for DALYs in 2019:")
print(question_data.describe())