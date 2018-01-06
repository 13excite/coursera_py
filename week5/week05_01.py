import socket
import time
import collections as cllns

# class for client obj put exception
class ClientError(socket.error):
    pass

class Client:

    def __init__(self, host, port, timeout=None):
        self._host = host
        self._port = port
        self._timeout = timeout

    def put(self, name, value, timestamp=None):
        timestamp = timestamp or int(time.time())
        with socket.create_connection((self._host, self._port), self._timeout) as s:
            data = 'put %s %f %d\n' % (name, value, timestamp)
            try:
                s.send(data.encode('utf-8'))
            except socket.error:
                raise ClientError

    def get(self, key_metric):
        data_dict = cllns.defaultdict(list)
        with socket.create_connection((self._host, self._port), self._timeout) as s:
            msg = 'get %s\n' % key_metric
            try:
                s.send(msg.encode('utf-8'))
            except socket.error:
                raise ClientError
            data = s.recv(1024).decode('utf-8')
            data = [i.split() for i in data.split('\n')[1:] if len(i) > 1]
            [data_dict[i[0]].append((int(i[2]), float(i[1]))) for i in data]
        if key_metric == '*':
            return data
        else:
            data = {key_metric: data.get(key_metric)}
            return data



#### tests
client = Client("127.0.0.1", 8888, timeout=15)

client.put("palm.cpu", 0.5, timestamp=1150864247)
#client.put("palm.cpu", 2.0, timestamp=1150864248)
#client.put("palm.cpu", 0.5, timestamp=1150864248)

#client.put("eardrum.cpu", 3, timestamp=1150864250)
#client.put("eardrum.cpu", 4, timestamp=1150864251)
#client.put("eardrum.memory", 4200000)

#print(client.get("*"))
