import os
import json
import sys

repo = sys.argv[1]

if repo == 'dev':
    print('\x1b[36mDev branch detected, no checks needed.\x1b[0m')
    sys.exit(0)

with open('update.json', 'r') as file:
    data = json.load(file)

exit_code = os.system('git clone --branch ' + data['version'] + ' https://github.com/UnifierHQ/unifier unifier')
if exit_code != 0:
    print(f'\x1b[31mCould not pull Unifier {data["version"]}. It may not exist.\x1b[0m')
    sys.exit(1)

with open('unifier/plugins/system.json', 'r') as file:
    unifier_data = json.load(file)

if unifier_data['release'] < data['release']:
    print('\x1b[36mupdate.json release number is higher than the Unifier release number.\x1b[0m')
    print(f'\x1b[36mExpected: {unifier_data["release"]}, got: {data["release"]}\x1b[0m')
    sys.exit(1)

print('\x1b[36mChecks passed, update.json is valid.\x1b[0m')
print(f'\x1b[36mupdate.json is on {data["version"]} (rel{data["release"]})\x1b[0m')
print(f'\x1b[36mUnifier is on {unifier_data["version"]} (rel{unifier_data["release"]})\x1b[0m')
