import socket
import time


class Client:

    def __init__(self, host, port, timeout=None):
        self._host = host
        self._port = port
        self._timeout = timeout

    def put(self, name, value, timestamp=int(time.time())):
        with socket.create_connection((self._host, self._port), self._timeout) as s:
            data = 'put %s %f %d\n' % (name, value, timestamp)
            try:
                s.send(data.encode('utf-8'))
            except socket.error:
                raise ConnectionError

    def get(self):
        pass



#### tests
client = Client("127.0.0.1", 8888, timeout=15)

client.put("palm.cpu", 0.5, timestamp=1150864247)
client.put("palm.cpu", 2.0, timestamp=1150864248)
client.put("palm.cpu", 0.5, timestamp=1150864248)

client.put("eardrum.cpu", 3, timestamp=1150864250)
client.put("eardrum.cpu", 4, timestamp=1150864251)
client.put("eardrum.memory", 4200000)

#print(client.get("*"))
