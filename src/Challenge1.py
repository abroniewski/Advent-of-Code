# Day 1 Challenge
# https://adventofcode.com/2021/day/1

# Part 1 - How many measurements are larger than the previous measurement?
with open('../data/raw/AdventCode-1.txt', 'r') as f:
    reader = f.readlines()
    depth = list(reader)

count = 0
# Why don't I get an overflow error with this range in the for index?
#   it seems like I am going from 1 -> 2000, but my index should only
#   allow to go from 0 -> 1999?
for index in range(1,len(depth)):
    last_value = int(depth[index-1].strip())
    current_value = int(depth[index].strip())
    if current_value > last_value:
        count += 1
print(f"The number of measurements larger than the previous is {count}")

# -----------------
# Part 2 - Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

# dropping count number by 1 as the first triple will increase the count by 1 even though there is no true
count = -1
last_sum = 0
for index in range(2,len(depth)):
    two_before = int(depth[index-2].strip())
    one_before = int(depth[index-1].strip())
    current = int(depth[index].strip())
    current_sum = sum([two_before, one_before, current])
    if current_sum > last_sum:
        count += 1
    last_sum = current_sum
print(f"The number of three-measurement sums larger than the previous is {count}")
