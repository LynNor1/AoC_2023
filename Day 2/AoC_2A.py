import os

max_red = 12
max_green = 13
max_blue = 14

filename = "input_data.txt"

# Using readlines()
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, filename), 'r')
Lines = file1.readlines()

sum = 0
for line in Lines:

    # get the game #
    game_tokens = line.split(':')
    game_num_tokens = game_tokens[0].split()
    game_num = int(game_num_tokens[1])

    # get the bag draws
    bag_draws = game_tokens[1].split(';')

    # analyze each bag draw
    can_match = True
    for bag_draw in bag_draws:
        # get the cubes drawn
        cubes_drawn = bag_draw.split(',')
        # analyze the cube draws
        for cube_draw in cubes_drawn:
            # get the # and color
            item_tokens = cube_draw.split()
            # get the # of cubes
            num_cubes = int(item_tokens[0].strip())
            # get the color
            color = item_tokens[1].strip()
            if color == "red" and num_cubes > max_red:
                can_match = False
            elif color == "green" and num_cubes > max_green:
                can_match = False
            elif color == "blue" and num_cubes > max_blue:
                can_match = False

    if can_match:
        sum += game_num

print (sum)