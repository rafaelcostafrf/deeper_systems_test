import numpy as np
import pandas as pd
import json

df = pd.read_json('source_file_2.json')
# columns - 'name', 'managers', 'watchers', 'priority'

# sorting by priority - lowest intergers first
df = df.sort_values('priority', ascending=True)

# initializing dictionaries
watchers_dict = {}
managers_dict = {}

# function to add keys and values to dictionary
def add_2_dict(dict, key, value):
    # if there is a key, append new value, else create key and assign value as list
    if key in dict:
        dict[key].append(value)
    else:
        dict[key] = [value]
    return dict

# run trough the json by project
for name, watchers, managers in zip(df.name, df.watchers, df.managers):
    # run each project by each manager and watcher
    for manager in managers:
        add_2_dict(managers_dict, manager, name)
    for watcher in watchers:
        add_2_dict(watchers_dict, watcher, name)

# save the json, with indentation 4 to output exactly as requested
with open('watchers.json', 'w') as outfile:
    json.dump(watchers_dict, outfile, indent=4)
with open('managers.json', 'w') as outfile:
    json.dump(managers_dict, outfile, indent=4)

