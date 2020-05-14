import json
import os

# *** RENAME to the json file name - .json ***#
name = 'Wort2'
with open(name + '.json') as f:
    data = json.load(f)
i =0
for _ in data['ObjectStates'][0]['ContainedObjects']:
    print(data['ObjectStates'][0]['ContainedObjects'][i]['Nickname'])
    i += 1


