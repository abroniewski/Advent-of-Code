# Day 3 challenge
# https://adventofcode.com/2021/day/3
#
# -------- Part 1 ---------
# What is the power consumption of the submarine?

# Initialize a list. When reading in the file, the list will take in list of
# length equal to the number of lines in the file.
# LEARNING: Using .splitlines(), we do not return the '/n' character in each of the list objects
diagnostic = []
with open('../data/raw/AdventCode-3.txt', 'r') as file:
    diagnostic = file.read().splitlines()


# Now we initialize a list called bit_sum. This list will sum the values in each bit position.
# LEARNING: using enumerate is a very fast way to iterate through the list (much better than itterows()?)
# LEARNING: using enumerate allows access to both the index and the value
# LEARNING: a list needs to be initiated with empty values. We could not use bit_sum = []
#   and then set bit_sum[0] = 'some number'
# LEARNING: Using debugger in PyCharm, we can set the breakpoint to the bottom of the code we are
#   testing, and all the variables will be saved in memory and show directly in the editor. This
#   gives Jupyter style functionality, but lets me easily clear the memory by exiting debug mode.
#   Jupyter was slow after a while because the variables were never flushed from memory.
# LEARNING: we can use enumerate to iterate through a string. The string has an index for each value.

bit_sum = [0,0,0,0,0,0,0,0,0,0,0,0]
for diagnostic_index, item in enumerate(diagnostic):
    for bit_index, bit in enumerate(item):
        bit_sum[bit_index] += int(bit)

# We can now determine the bit-value of gamma and epsilon.
# The logic used is to subtract half of the total length of the diagnostics list.
# For gamma, anything that is negative is primarily a '0', and anything positive is primarily a '1'.
# We use the opposite logic for epsilon.
diagnostic_length = len(diagnostic)
gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]

for bit_index, bit_sum_value in enumerate(bit_sum):
    if bit_sum_value-int(0.5 * diagnostic_length) > 0:
        gamma[bit_index] = 1
        epsilon[bit_index] = 0
    if bit_sum_value-int(0.5 * diagnostic_length) < 0:
        gamma[bit_index] = 0
        epsilon[bit_index] = 1

# Convert value from bit-index to integer. First convert to string, then pass the string into int() function with
# base=2. map() function will iterate through each value in the gamma list and modify the value type (e.g. map it).
# The '' in front of the join() function means we have no spaces between the values being joined.
gamma_string = ''.join(map(str, gamma))
gamma_rate = int(gamma_string, base=2)

epsilon_string = ''.join(map(str, epsilon))
epsilon_rate = int(epsilon_string, base=2)

power_consumption = gamma_rate * epsilon_rate

print(f'The gamma rate is: {gamma_rate}')
print(f'The epsilon rate  is: {epsilon_rate}')
print(f'The power consumption is: {power_consumption}')


