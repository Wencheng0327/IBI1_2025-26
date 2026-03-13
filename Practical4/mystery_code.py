# What does this piece of code do?
# Answer:the code is to randomly selcet an integer from 1 to 10 11 times, calculating their sum and output the sum

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0
progress=0
while progress<=10:	#Perform a loop with 11 iterations.
	progress+=1
	n = randint(1,10)	#Randomly select an integer from 1 to 10
	total_rand+=n	#calculate the sum of chosen randomised integer

print(total_rand)

