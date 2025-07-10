import json

with open('unifier/plugins/system.json', 'r') as file:
    unifier_data = json.load(file)

release = unifier_data['release']
reboot = unifier_data['reboot']
b_reboot = unifier_data['b_reboot']
version = unifier_data['version']

with open('update.json', 'r') as file:
    data = json.load(file)

data['release'] = int(release)
data['reboot'] = int(reboot)
data['b_reboot'] = int(b_reboot)
data['version'] = version

with open('update.json', 'w') as file:
    # noinspection PyTypeChecker
    json.dump(data, file, indent=2)

print(json.dumps(data, indent=2))
