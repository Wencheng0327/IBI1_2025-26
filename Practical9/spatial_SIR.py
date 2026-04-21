# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Model parameters
beta = 0.3
gamma = 0.05
time_points = 100

# 0 = susceptible, 1 = infected, 2 = recovered
population = np.zeros((100, 100), dtype=int)

# Randomly choose one infected individual
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# Pseudocode:
# start with a 100 x 100 grid of susceptible people
# choose one random cell to be infected
# for each time step:
#     find all infected cells
#     for each infected cell:
#         check all 8 neighbours
#         if a neighbour is susceptible, infect with probability beta
#         recover the infected cell with probability gamma
#     update the grid
#     save snapshots for plotting

snapshots = {0: population.copy()}

for t in range(1, time_points + 1):
    new_population = population.copy()

    infected_positions = np.where(population == 1)
    infected_cells = list(zip(infected_positions[0], infected_positions[1]))

    for x, y in infected_cells:
        # Check all 8 neighbours
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = x + dx
                ny = y + dy
                # Check boundary conditions
                if 0 <= nx < 100 and 0 <= ny < 100:
                    # Only susceptible neighbours can be infected
                    if population[nx, ny] == 0:
                        if np.random.random() < beta:
                            new_population[nx, ny] = 1
        # Recovery step
        if np.random.random() < gamma:
            new_population[x, y] = 2

    population = new_population

    if t in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        snapshots[t] = population.copy()

# Plot a series of snapshots
times_to_plot = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

fig, axes = plt.subplots(3, 4, figsize=(10, 8), dpi=150)
axes = axes.flatten()

for i, time in enumerate(times_to_plot):
    ax = axes[i]
    ax.imshow(snapshots[time], cmap="viridis", interpolation="nearest")
    ax.set_title(f"time {time}")

# Hide the last empty subplot
for j in range(len(times_to_plot), len(axes)):
    axes[j].axis("off")

sus_patch = mpatches.Patch(color='purple', label='Susceptible (0)')
inf_patch = mpatches.Patch(color='green', label='Infected (1)')
rec_patch = mpatches.Patch(color='yellow', label='Recovered (2)')
plt.legend(handles=[sus_patch, inf_patch, rec_patch])

plt.suptitle("Spatial SIR model")
plt.tight_layout()
plt.show()

