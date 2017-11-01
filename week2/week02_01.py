import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def check_key_exsist(user_key, dict):
    if user_key in dict:
        return True
    return False

def get_dict_from_json(json_data):
    return json.loads(json_data)

def extract_dict_to_json(dictinary):
    return json.dumps(dictinary)

def add_value(user_key, user_value, json_data):
    d = get_dict_from_json(json_data)
    if check_key_exsist(user_key, d):
        d[user_key].append(user_value)
        return extract_dict_to_json(d)
    d[user_key] = [user_value]
    return extract_dict_to_json(d)


def get_value(user_key, json_data):
    d = get_dict_from_json(json_data)
    if check_key_exsist(user_key, d):
        return ", ".join(map(str, d[user_key]))
    return None

#  WORK WITH JSON!!!!!
#data = {"1":"one", "2":"two"} # python словарь
#json_data = json.dumps(data) # упаковываем
#parsed_json = json.loads(json_data) #распаковываем



parser = argparse.ArgumentParser(description='Simple key-value store script')
parser.add_argument("--key", help="set key to adding value to storage, if --key is single argument, then return data or None", required=True)
parser.add_argument("--value", help="set value to storing to storage")
args = parser.parse_args()

test_hash = {
        "one" : ["two"],
        "1" : ["test", "ddd"],
    }
if args.key and not args.value:
    print(type(args.key))
    print(get_value(args.key, extract_dict_to_json(test_hash)))
elif args.key and args.value:
    print(add_value(args.key, args.value, extract_dict_to_json(test_hash)))
