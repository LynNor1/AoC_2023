import os

filename = "input_data.txt"

# Using readlines()
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file1 = open(os.path.join(__location__, filename), 'r')
Lines = file1.readlines()

seeds = list()
map_indices = list() # of tuples: ("seed", "soil", idx)
mappings = list() # of lists: list 0 could be: [[50 98 2] [52 50 48]]

map_idx = 0
is_mapping = False
mapping_list = list()

for line in Lines:

    clean_line = line.strip()

    # look for seeds
    if clean_line.find("seeds:") == 0:
        tokens = clean_line.split(':')
        seed_tokens = tokens[1].split()
        for seed in seed_tokens:
            seeds.append(int(seed.strip()))

    # look for start of map
    elif clean_line.find(":") > 0:
        # get name of mapping
        tokens = clean_line.split()
        mapping_tokens = tokens[0].split('-')
        to_item = mapping_tokens[0]
        from_item = mapping_tokens[2]
        map_indices.append((to_item, from_item, map_idx))
        mapping_list = list()
        is_mapping = True

    # look for element of a map
    elif len(clean_line) > 0:
        short_list = list()
        tokens = clean_line.split()
        for token in tokens:
            short_list.append(int(token.strip()))
        mapping_list.append(short_list)

    # look for end of seeds or map
    else:
        if len(mapping_list) > 0:
            mappings.append(mapping_list)
            is_mapping = False
            map_idx += 1

# clean up that last mapping
if is_mapping and len(mapping_list) > 0:
    mappings.append(mapping_list)

print ("all done with parsing")

# for each seed, find the location 
# where it can be planted
start_tag = "seed"
from_tag = start_tag
final_tag = "location"
locations_for_seeds = list()
for seed in seeds:
    from_id = seed
    from_tag = start_tag
    print (f"Searching for location of seed: {seed}")
    location_found = False
    while not location_found:
        # look for mapping index for from_tag-to-to_tag
        for map_index in map_indices:
            if map_index[0] == from_tag:
                to_tag = map_index[1]
                map_idx = map_index[2]
                print (f"  Found mapping from {from_tag} to {to_tag}")
                # now get the id of the "to" target
                to_id = -1
                mymappings = mappings[map_idx]
                for mymapping in mymappings:
                    start_to_id = mymapping[0]
                    start_from_id = mymapping[1]
                    num_ids = mymapping[2]
                    if start_from_id <= from_id < start_from_id+num_ids:
                        diff = from_id - start_from_id
                        to_id = start_to_id + diff
                if to_id == -1:
                    to_id = from_id
                print (f"  {from_id} maps to {to_id}")
                break
        if to_tag == final_tag:
            location_found = True
            locations_for_seeds.append(to_id)
            print (f"  Location id of seed {seed} is {to_id}")
        else:
            # now move to next pair of items to look for
            from_id = to_id
            from_tag = to_tag

print (f"Minimum location is {min(locations_for_seeds)}")

 