import os
import tempfile
import argparse
import json




def check_key_exsist(user_key, dict):
    if dict != None:
        if user_key in dict and dict != None:
           return True
    return False

def get_dict_from_json(json_data):
    return json.loads(json_data)

def extract_dict_to_json(dictinary):
    return json.dumps(dictinary)

def add_value(user_key, user_value, json_data):
    if  json_data == None:
        d = dict()
    else:
        d = get_dict_from_json(json_data)
    if check_key_exsist(user_key, d):
        d[user_key].append(user_value)
        return extract_dict_to_json(d)
    d[user_key] = [user_value]
    return extract_dict_to_json(d)


def get_value(user_key, json_data):
    if json_data  != 'null':
        d = json.loads(json.loads(json_data))
        if check_key_exsist(user_key, d):
            return ", ".join(map(str, d[user_key]))
    return 'None'

def open_read_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            data = f.read()
            f.closed
            return data
    return None
def open_write_file(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)



parser = argparse.ArgumentParser(description='Simple key-value store script')
parser.add_argument("--key", help="set key to adding value to storage, if --key is single argument, then return data or None", required=True)
parser.add_argument("--value", help="set value to storing to storage")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#print(storage_path)

if args.key and not args.value:

    print(get_value(args.key, extract_dict_to_json(open_read_file(storage_path))))

elif args.key and args.value:
    open_write_file(storage_path, add_value(args.key, args.value, open_read_file(storage_path)))

