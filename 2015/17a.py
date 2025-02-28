# Advent of Code 2015, day 17, part 1

from itertools import combinations

with open("data/17.txt") as file:
    my_list = [int(line.strip()) for line in file.readlines()]

all_combinations = []
for i in range(1, len(my_list) + 1):
    all_combinations.extend(combinations(my_list, i))

count = 0
number_of_containers = []
for combi in all_combinations:
    if sum(combi) == 150:
        count += 1
        number_of_containers.append(len(combi))

print(f"Combinations: {count}")