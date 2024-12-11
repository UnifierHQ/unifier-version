import json
import sys

version = sys.argv[1]
release = sys.argv[2]

with open('update.json', 'r') as file:
    data = json.load(file)

data['release'] = int(release)
data['version'] = version

with open('update.json', 'w') as file:
    # noinspection PyTypeChecker
    json.dump(data, file, indent=4)
