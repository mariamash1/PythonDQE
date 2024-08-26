import random
import string

#part1
# generate random number of dicts from 2 to 10
dict_num = random.randint(2, 10)

# create empty list of dicts to add here dict
list_of_dicts = []

# loop to create each dict
for i in range(dict_num):
    # generate a random number of keys for each dict
    key_num = random.randint(1, len(string.ascii_lowercase))

    # select letters for keys randomly
    keys = random.sample(string.ascii_lowercase, key_num)

    # select  value for each key randomly and add to the dictionary
    dict = {key: random.randint(0, 100) for key in keys}

    # add the dict to the list
    list_of_dicts.append(dict)

# print
print(list_of_dicts)

#part2
new_dict = {}
for idx, dict_item in enumerate(list_of_dicts):
    for key, value in dict_item.items():
        # create a new key with the index
        new_key = f"{key}_{idx}"
        if key in new_dict:
            # Compare and update the value if the current value is greater
            if value > new_dict[key][0]:
                new_dict[key] = (value, idx)
        else:
            # add the new key-value pair with index
            new_dict[key] = (value, idx)

# formatting the keys with the dictionary index
change_dict = {f"{key}_{val[1]}": val[0] for key, val in new_dict.items()}

print(change_dict)

