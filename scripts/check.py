import os
import json
import sys

repo = sys.argv[1]

if repo == 'dev':
    print('Dev branch detected, no checks needed.')
    sys.exit(0)

with open('update.json', 'r') as file:
    data = json.load(file)

exit_code = os.system('git clone --branch ' + data['version'] + ' https://github.com/UnifierHQ/unifier unifier')
if exit_code != 0:
    print(f'Could not pull Unifier {data["version"]}. It may not exist.')
    sys.exit(1)

with open('unifier/plugins/system.json', 'r') as file:
    unifier_data = json.load(file)

if unifier_data['release'] < data['release']:
    print('update.json release number is higher than the Unifier release number.')
    print(f'Expected: {unifier_data["release"]}, got: {data["release"]}')
    sys.exit(1)
