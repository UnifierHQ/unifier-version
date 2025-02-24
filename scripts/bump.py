import json

with open('unifier/plugins/system.json', 'r') as file:
    unifier_data = json.load(file)

release = unifier_data['release']
reboot = unifier_data['reboot']
version = unifier_data['version']

with open('update.json', 'r') as file:
    data = json.load(file)

data['release'] = int(release)
data['reboot'] = int(reboot)
data['version'] = version

with open('update.json', 'w') as file:
    # noinspection PyTypeChecker
    json.dump(data, file, indent=2)

print(json.dumps(data, indent=2))
