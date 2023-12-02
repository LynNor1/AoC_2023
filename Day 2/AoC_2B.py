import os

filename = "input_data.txt"

# Using readlines()
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, filename), 'r')
Lines = file1.readlines()

sum = 0
for line in Lines:

    min_red = 0
    min_green = 0
    min_blue = 0

    # get the game #
    game_tokens = line.split(':')
    game_num_tokens = game_tokens[0].split()
    game_num = int(game_num_tokens[1])

    # get the bag draws
    bag_draws = game_tokens[1].split(';')

    # analyze each bag draw
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
            if color == "red" and num_cubes > min_red:
                min_red = num_cubes
            elif color == "green" and num_cubes > min_green:
                min_green = num_cubes
            elif color == "blue" and num_cubes > min_blue:
                min_blue = num_cubes

    power = min_red * min_green * min_blue
    sum += power

print (sum)