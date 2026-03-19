#2

import matplotlib.pyplot as plt

heart_rates = [ 72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64 ]
num_patients = len ( heart_rates )
#calculate sum 
#sum = 0
#for i in heart_rate:
#   sum += i
mean_hr = sum ( heart_rates ) / num_patients
print(f"Number of patients: {num_patients}")
print(f"Mean heart rate: {mean_hr:.2f} bpm")

# Categorize heart rates and Find largest category
low = 0
normal = 0
high = 0
for hr in heart_rates:
    if hr < 60:
        low += 1
    elif 60 <= hr <= 120:
        normal += 1
    else:
        high += 1
print(f"Low (<60): {low}")
print(f"Normal (60–120): {normal}")
print(f"High (>120): {high}")
categories = {
    "Low": low,
    "Normal": normal,
    "High": high
}
largest = max(categories, key = categories.get )
print(f"Largest category: {largest}")

# Pie chart
colors = ['#66c2a5', '#fc8d62', '#8da0cb']
labels = categories.keys()
sizes = categories.values()
plt.pie( sizes, labels = labels, autopct = '%1.1f%%', startangle = 90, explode = [0, 0.1, 0], shadow = True, colors = colors ) 
plt.title("Heart Rate Categories")
plt.axis( 'equal' )

plt.show()