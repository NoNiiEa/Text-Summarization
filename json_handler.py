import json

def read_json(dir):
    with open(dir, 'r') as file:
        data = json.load(file)
    return data

def dump_json(dir, data):
    with open(dir, 'w') as file:
        json.dump(data, file, indent=4)
