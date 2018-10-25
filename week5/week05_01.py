import socket
import time

# class for client obj put exception
class ClientError(socket.error):
    pass

class Client:
    def __init__(self, addr, port, timeout=None):
        self.addr = addr
        self.port = port
        try:
            self.sock = socket.create_connection((self.addr, self.port), timeout)
        except socket.error as err:
            ClientError("error create connection", err)

    def _read(self):
        data = b""

        while not data.endswith(b"\n\n"):
            try:
                data += self.sock.recv(1024)
            except socket.error as err:
                raise ClientError("error recv data", err)
        
        decoded_data = data.decode()

        status, payload = decoded_data.split("\n", 1)
        payload = payload.strip()

        if status == "error":
            raise ClientError(payload)
        
        return payload

    def put(self, metric_name, metric_val, timestamp = int(time.time())):
        try:
            self.sock.sendall("put {} {} {}\n".format(metric_name, metric_val, timestamp).encode())
        except socket.error as err:
            raise ClientError("error send data", err)
    
        self._read()
        
    def get(self, metric_name):
        try:
            self.sock.sendall("get {}\n".format(metric_name).encode())
        except socket.error as err:
            raise ClientError("error send data")
        payload = self._read()

        data = {}
        if payload == "":
            return data

        for row in payload.split("\n"):
            key, value, timestamp = row.split()
            if key not in data:
                data[key] = []
            data[key].append((int(timestamp), float(value)))
        return data
    
    def close(self):
        try:
            self.sock.close()
        except socket.error as err:
            raise ClientError("error close connection", err)



#### tests
#client = Client("127.0.0.1", 8888, timeout=15)

#client.put("palm.cpu", 0.5, timestamp=1150864247)
#client.put("palm.cpu", 2.0, timestamp=1150864248)
#client.put("palm.cpu", 0.5, timestamp=1150864248)

#client.put("eardrum.cpu", 3, timestamp=1150864250)
#client.put("eardrum.cpu", 4, timestamp=1150864251)
#client.put("eardrum.memory", 4200000)

#print(client.get("*"))
