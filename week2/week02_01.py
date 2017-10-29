import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def add_value(user_key, user_value):
    pass

def get_value(user_key):
    pass

parser = argparse.ArgumentParser(description='Simple key-value store script')
parser.add_argument("--key", help="set key to adding value to storage, if --key is single argument, then return data or None")
parser.add_argument("--value", help="set value to storing to storage")
args = parser.parse_args()


data = 'parse arg'
with open(storage_path, 'w') as f:
    json.dump(data, f, ensure_ascii=False)
