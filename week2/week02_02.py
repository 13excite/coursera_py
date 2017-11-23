import json
import functools

def to_json(func):
    @functools.wraps(func)
    def json_decode(*args, **kwargs):
        result = func(*args, **kwargs)
        if result  != 'null' or result != None:
            json_data = json.dumps(result)
            return json_data
    return json_decode




@to_json
def get_data():
  return {
    'data': 42
  }

print(get_data())
print(get_data.__name__)

