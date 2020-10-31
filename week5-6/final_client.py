import socket
import time


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        try:
            self.sock = socket.create_connection((self.host, self.port),
                                                 self.timeout)
        except socket.error as err:
            raise ClientError(err)

    def put(self, metric, value, timestamp=None):
        timestamp = str(timestamp or int(time.time()))
        request = f'put {metric} {value} {timestamp}\n'.encode('utf8')
        try:
            self.sock.sendall(request)
            response = self.sock.recv(1024)
            if b'ok\n' not in response:
                raise ClientError
        except Exception:
            raise ClientError

    def get(self, key):
        metric_dict = {}
        request = f'get {key}\n'.encode('utf8')

        try:
            self.sock.sendall(request)
            response = self.sock.recv(1024)
            if b'ok' not in response:
                raise ClientError

            response = str(response).strip('\n').split('\\n')

            for m in response:
                metrics = m.split(' ')
                if len(metrics) == 3:
                    metric_key = metrics[0]
                    metric_value = float(metrics[1])
                    metric_timestamp = int(metrics[2])
                    metric_list = metric_dict.get(metric_key, [])
                    metric_list.append((metric_timestamp, metric_value))
                    metric_dict.update({metric_key: sorted(metric_list)})
                elif metrics not in [["b'ok"], [""], ["'"]]:
                    raise ClientError

            return metric_dict

        except Exception as err:
            raise ClientError(err)


if __name__ == "__main__":
    client = Client("127.0.0.1", 8888, timeout=15)
    # client.put("palm.cpu", 0.5, timestamp=1150864247)
    print(client.get('*'))
