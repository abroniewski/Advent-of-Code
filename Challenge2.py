# Day 2 challenge
# https://adventofcode.com/2021/day/2
# Calculate the horizontal position and depth you would have after following the planned course.

# initialize a list called directions. When reading in the file, the lise will take in list of 
# length 2 that includes the direction at index [0] and the movement amount at index [1]
submarine_instructions = []
with open('AdventCode-2.txt', 'r') as file:
    for line in file:
        submarine_instructions.append(line.split())


# initialize amounts. Cycle through each pair of direction and movement amount if add to horizontal movement
# or depth as appropriate. Include error check just in case, and print the results.
# The multiplication value is the expected outcome for the challenge.
def calculate_horizontal_and_depth_movement(directions: list) -> None:
    horizontal = 0
    depth = 0
    for movement in directions:
        if movement[0] == 'forward':
            horizontal += int(movement[1])
        elif movement[0] == 'down':
            depth += int(movement[1])
        elif movement[0] == 'up':
            depth -= int(movement[1])
        else:
            print(f"Oops! {movement[0]} is a funny direction!")
    print("---Part 1---")
    print(f"The submarine moved {horizontal} m horizontally and dropped to a depth of {depth} m.")
    print(f"Challenge 1 answer of horizontal * depth is: {horizontal * depth}\n")


# -----------------
# Part 2 - Using this new interpretation of the commands, calculate the horizontal 
# position and depth you would have after following the planned course.

# Similar approach to before, but now we need to change our aim with an up or down value,
# and our depth will increase with forward movement based on which direction we are aiming.
def calculate_horizontal_and_depth_with_aim(directions: list) -> None:
    horizontal = 0
    depth = 0
    aim = 0
    for movement in directions:
        if movement[0] == 'forward':
            horizontal += int(movement[1])
            depth += aim * int(movement[1])
        elif movement[0] == 'down':
            aim += int(movement[1])
        elif movement[0] == 'up':
            aim -= int(movement[1])
        else:
            print(f"Oops! {movement[0]} is a funny direction!")

    print("---Part 2---")
    print(f"The submarine moved {horizontal} m horizontally and dropped to a depth of {depth} m.")
    print(f"Challenge 2 answer of horizontal * depth is: {horizontal * depth}")


# calling all functions to run
calculate_horizontal_and_depth_movement(submarine_instructions)
calculate_horizontal_and_depth_with_aim(submarine_instructions)
