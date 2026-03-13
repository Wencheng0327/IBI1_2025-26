#5
#pseudocode:
#define variables for the number of initial infected students, total students and growth rate
#print initial infection status
#loop until all students are infected (notes: the infected students can't be more than total)
#update infection count and check if curren-infected is bigger than total
#print total days required

# initialize variables
initial_infected = 5
growth_rate = 0.4
total_students = 91
current_infected = initial_infected
days = 0

# output initial state 
print("Day", days, ":", current_infected, "infected")

# Loop until all 91 students are infected.
while current_infected < total_students:
    current_infected = current_infected * (1 + growth_rate)
    days += 1   #Add one day in each cycle.
    #if the number of "infected" students is bigger than the number of total students, it means all students are infected
    if current_infected <= 91:
        print("Day", days, ":", current_infected, "infected","(around",round(current_infected),"infected)")
    else:
        print("Day", days, ":", 91, "infected")
        break

# output total days that all students are infected
print("It took", days, "days to infect all students.")