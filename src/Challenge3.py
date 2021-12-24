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

# ----------------- Part 2 ---------

# Part 2 also requires iteration through the binary strings. Can we modify our previous code to
# complete this iteration at the same time? Maybe yes, but for simplicity, we will create
# new loops. Even in real life, the dataset is small enough that it is probably faster to use a new
# loop than find good logic to do it in one go. But we can come back later to see if we can integrate
# the two solutions together.

diagnostic = []
with open('../data/raw/AdventCode-3.txt', 'r') as file:
    diagnostic = file.read().splitlines()

# Here we define a function that uses the same logic as we had in Part 1. This time we are
# iterating through the entire list of binary numbers and comparing numbers depending on which
# position they are in. The function will take as a parameter the string_position, which defines
# which location of the binary number we want to examine. It will be called in a for loop later.
# LEARNING: without casting the type to "float", the value in the "if" would get truncated resulting
#   in an incorrect evaluation.
# LEARNING: Is it better to initialize a value before the loop and then ise "value += 1" later,
# or to use only value = value + 1?
# TODO: We should include an "else" statement to catch errors
def find_most_common_bit(bit_list: list, string_position: int) -> int:
    count_bits = 0
    number_of_values = 0
    for bit in range(len(bit_list)):
        count_bits += int(bit_list[bit][string_position])
        number_of_values += 1
    if count_bits - float(0.5 * number_of_values) > 0:
        return 1
    if count_bits - float(0.5 * number_of_values) < 0:
        return 0
    if count_bits - float(0.5 * number_of_values) == 0:
        return 1

# LEARNING: I originally tried to call the find_most_common_bit function with a "not" in front of
# it when looking to return the opposite values. This did not work because the final if check
# returns a different value for a tie.
# LEARNING: Is it better stylistically to add an extra parameter to a single function to define which
# whether it is most or least common? path to go down? Then I would have a nested if? Can we make this
# shorter?
def find_least_common_bit(bit_list: list, string_position: int) -> int:
    count_bits = 0
    number_of_values = 0
    for bit in range(len(bit_list)):
        count_bits += int(bit_list[bit][string_position])
        number_of_values += 1
    if count_bits - float(0.5 * number_of_values) < 0:
        return 1
    if count_bits - float(0.5 * number_of_values) > 0:
        return 0
    if count_bits - float(0.5 * number_of_values) == 0:
        return 0


# LEARNING:
#   [num for num in bit_list if int(num[0]) == 0]
#   this line is called "comprehension" in Python. It means the same thing as:
#   for num in bit_list:
#       if int(num[0]) == 0:
#           return num
# LEARNING: always check your data types. If there are issues it may be because you are comparing
#   integers and strings
# TODO: This function does not work when it is used with the least common bit and the subset being
#   analyzed does not have any binary numbers that inlcude the least common bit in the next position.
def return_most_common_subset(bit_list: list, most_common_bit: int, position: int) -> list:
    subset_list = [num for num in bit_list if int(num[position]) == most_common_bit]
    return subset_list


# Here we find the value for oxygen following instructions. First we initialize values.
# We do this outside the for loop so that we don't save over our "diagnostic" value.
# LEARNING: Use a break statement to leave a loop. A continue statement can let you
#   skip a value. Initially a only had a "while len(subset) > 1" statement, and assumed
#   a check was completed against the while statement everytime we went through the for loop.
#   TODO: Does a while loop iterate through a list the same as a for loop just with a condition?
#       Is this "if condition: break" syntax the right way to go?
# LEARNING: I wanted to create a recursive function that calls itself. I feel this should
# be possible, but it wasn't just out of reach for implementation.
most_common_bit = find_most_common_bit(diagnostic, 0)
subset = return_most_common_subset(diagnostic, most_common_bit, 0)

for position in range(1,len(diagnostic[0])):
    most_common_bit = find_most_common_bit(subset, position)
    subset = return_most_common_subset(subset, most_common_bit, position)
    if len(subset) == 1:
        oxygen_binary = subset
        break

# This follow the same logic as the oxygen_rating search, just using least common values.
least_common_bit = find_least_common_bit(diagnostic, 0)
subset = return_most_common_subset(diagnostic, least_common_bit, 0)

for position in range(1,len(diagnostic[0])):
    least_common_bit = find_least_common_bit(subset, position)
    subset = return_most_common_subset(subset, least_common_bit, position)
    if len(subset) == 1:
        CO2_binary = subset
        break

# Now we just convert our binary string to an integer, print the results, and we are done!
oxygen_binary_string = ''.join(map(str, oxygen_binary))
oxygen_rating = int(oxygen_binary_string, base=2)

CO2_binary_string = ''.join(map(str, CO2_binary))
CO2_scrubber_rating = int(CO2_binary_string, base=2)

life_support_rating = oxygen_rating * CO2_scrubber_rating

print(f'The oxygen rating is: {oxygen_rating}')
print(f'The CO2_scrubber rating is: {CO2_scrubber_rating}')
print(f'The life support rating is: {life_support_rating}')


