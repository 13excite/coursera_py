import functools

def to_json(func):
    @functools.wraps(func)
    def json_decode(*args, **kwargs):
        result = func(*args, **kwargs)




def get_data():
  return {
    'data': 42
  }

print(type(get_data()))
