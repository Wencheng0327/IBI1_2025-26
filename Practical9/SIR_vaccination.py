# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Basic model parameters: N for total number of people, S for susceptible, I for infected, R for recovered
N = 10000
beta = 0.3
gamma = 0.05
time_points = 1000

# Vaccination percentages
vaccination_rates = range(0, 101, 10)

plt.figure(figsize=(6, 4), dpi=150)

# Pseudocode:
# for each vaccination rate:
#     define number of vaccinated people (V)
#     set total population = 10000
#     start with 1 infected person if possible
#     calculate susceptible people as S = N - V - I
#     loop through time points
#         calculate infection probability
#         randomly decide new infections
#         randomly decide new recoveries
#         update S, I, R
#         record infected values
#     plot infected curve for this vaccination rate

for vacc_percent in vaccination_rates:
    V = int(N * vacc_percent / 100)

    # keep total population at 10000
    I = 1
    S = N - V - I
    R = 0

    # if everyone is vaccinated, there is no susceptible person left
    if S <= 0:
        S = 0
        I = 0

    I_values = [I]
    for t in range(time_points):
        infection_probability = beta * (I / N)

        if S > 0:
            new_infections = np.sum( np.random.choice( range(2), size=S, p=[1 - infection_probability, infection_probability] ) )
        else:
            new_infections = 0

        if I > 0:
            new_recoveries = np.sum( np.random.choice( range(2), size=I, p=[1 - gamma, gamma] ) )
        else:
            new_recoveries = 0

        # ensure counts do not exceed possible limits
        new_infections = min(new_infections, S)
        new_recoveries = min(new_recoveries, I + new_infections)

        S = S - new_infections
        I = I + new_infections - new_recoveries
        R = R + new_recoveries

        I_values.append(I)

    plt.plot(I_values, label=f"{vacc_percent}%")

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()