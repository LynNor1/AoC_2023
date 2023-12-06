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

# convert seeds list to list of ranges that
# need to be converted to the next element
seed_ranges = list()
for idx in range(0, len(seeds), 2):
    seed_ranges.append([seeds[idx], seeds[idx+1]])

def sort_list_of_lists(lst, index):
    return sorted(lst, key=lambda x: x[index])

# sort all seed ranges by 1st index
new_seed_ranges = sort_list_of_lists (seed_ranges, 0)
seed_ranges = new_seed_ranges
 
# sort all mappings by 2nd index
new_mappings = list()
for mapping_list in mappings:
    new_mapping_list = sort_list_of_lists(mapping_list, 1)
    new_mappings.append(new_mapping_list)
mappings = new_mappings

# for each seed, find the location 
# where it can be planted
start_tag = "seed"
from_tag = start_tag
final_tag = "location"
start_ranges = seed_ranges
location_found = False

while not location_found:

    print (f"Searching for idx of mapping from {from_tag}")

    for map_index in map_indices:
        if map_index[0] == from_tag:
            to_tag = map_index[1]
            map_idx = map_index[2]        
            print (f"  Found index for mapping from {from_tag} to {to_tag}")

            mymappings = mappings[map_idx]

            processed_ranges = list()
            unprocessed_ranges = start_ranges

            # loop over all the unmapped ranges
            while len(unprocessed_ranges) > 0:

                # grab 1st range
                myrange = unprocessed_ranges[0]
                # remove it from the list!
                del unprocessed_ranges[0]

                print (f"    Processing range: {myrange[0]} to {myrange[0]+myrange[1]-1}")

                did_process = False

                # loop over all the mappings
                for mymapping in mymappings:
                    diff = mymapping[1]-mymapping[0]                    
                    print (f"      Looking at mapping: {mymapping[1]} to {mymapping[1]+mymapping[2]-1} CONV {diff}")
                    # find overlap between myrange (e.g. seed range) and mymapping (e.g. soil range), if any
                    start_myrange = myrange[0]
                    end_myrange = myrange[0]+myrange[1]-1
                    start_mymap = mymapping[1]
                    end_mymap = mymapping[1]+mymapping[2]-1
                    overlap_start = max([start_myrange, start_mymap])
                    overlap_end = min([end_myrange, end_mymap])
                    if overlap_start <= overlap_end:
                        overlap = [overlap_start-diff, overlap_end-overlap_start+1]
                        processed_ranges.append(overlap)
                        print (f"        Found overlap from {overlap_start} to {overlap_end} CONV {diff}")     
                        did_process = True                   
                        # any unmapped range *before* the overlap is not going
                        # to be mapped to a new range (because I've sorted the
                        # initial seeds and all the mappings))
                        if overlap_start > start_myrange:
                            processed_ranges.append([start_myrange, overlap_start-start_myrange])
                            did_process = True
                            print (f"        Start overlap has no map {start_myrange} to {overlap_start-1}")
                        # any unmapped range *after* the overlap COULD be
                        # mapped by a subsequent mapping so we need to keep it
                        # in our list of unprocessed ranges
                        if end_myrange > overlap_end:
                            unprocessed_ranges.append([overlap_end+1,end_myrange-overlap_end])
                            print (f"        End range could be processed in later mapping from {overlap_end+1} to {end_myrange}")
                        break
                    else:
                        # no overlap
                        print (f"        No overlap so try next mapping")
                
                # if we're out of mappings to search over, then the
                # current unprocessed range is converted as-is
                if not did_process:
                    processed_ranges.append(myrange)

            break

    # update for next iteration
    from_tag = to_tag

    # sort the new processed ranges by starting index
    new_processed_ranges = sort_list_of_lists (processed_ranges, 0)
    start_ranges = new_processed_ranges

    if from_tag == "location":
        location_found = True
        # smallest location should be the very first # in the firs trange
        print (start_ranges[0][0])


 