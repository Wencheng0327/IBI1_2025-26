# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Basic model parameters: N for total number of people, S for susceptible, I for infected, R for recovered
N = 10000
S = N - 1
I = 1
R = 0

beta = 0.3
gamma = 0.05
time_points = 1000

# Lists to track values over time
S_values = [S]
I_values = [I]
R_values = [R]

# Pseudocode:
# for each time step:
#     calculate infection probability = beta * I / N
#     randomly decide which susceptible people become infected
#     randomly decide which infected people will be recovered
#     update S, I, R
#     store the new values

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

    S_values.append(S)
    I_values.append(I)
    R_values.append(R)

plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_values, label="susceptible")
plt.plot(I_values, label="infected")
plt.plot(R_values, label="recovered")
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend()
plt.grid( axis='y', linestyle='--', alpha=0.7 )
plt.tight_layout()
#plt.savefig( "<filename>",type="png" )
plt.show()
