# Advent of Code 2015, day 1, part 1

with open("data/1.txt") as file:
    content = file.read()

floor_up = content.count("(")
floor_down = content.count(")")

floor = floor_up - floor_down

print(f"Floor: {floor}")