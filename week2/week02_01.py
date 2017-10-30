import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def check_key_exsist(user_key, json_data):
    dic_data = json.loads(json_data)
    for element in dic_data:
        if user_key in element:
            return True
    return False


def add_value(user_key, user_value, json_data):
    d = {}
    d[user_key] = user_key

    pass

def get_value(user_key, json_data):
    if check_key_exsist(user_key, json_data):
        ##  get values
    return None

#  WORK WITH JSON!!!!!
#data = {"1":"one", "2":"two"} # python словарь
#json_data = json.dumps(data) # упаковываем
#parsed_json = json.loads(json_data) #распаковываем
#print data == parsed_json


parser = argparse.ArgumentParser(description='Simple key-value store script')
parser.add_argument("--key", help="set key to adding value to storage, if --key is single argument, then return data or None")
parser.add_argument("--value", help="set value to storing to storage")
args = parser.parse_args()
if args.key:
    test_hash = {
        "one" : "two",
        "1" : "test",
    }
    print(test_hash[args.key])


with open(storage_path, 'w') as f:
    d = json.loads(f)
