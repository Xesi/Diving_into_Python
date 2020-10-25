import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key",
                    help="display a square of a given number")
parser.add_argument("--value", 
                    help="increase output verbosity")
args = parser.parse_args()

key = args.key
value = args.value

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def read_json(storage_path):
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, 'r') as file:
        raw_data = file.read()
        if raw_data:
            return json.loads(raw_data)
        return {}

storage = read_json(storage_path)

if(value is None):
        if(key in storage):
            print(*storage.get(key, []), sep=', ')
        else:
             print(None)
else:
    if(key not in storage):
        storage[key] = []
    
    storage[key].append(value)
    
    with open(storage_path, 'w') as f:
        json.dump(storage, f)




