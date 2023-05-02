# https://www.codegrepper.com/profile/cute-copperhead-yqsmpcburmyp
import threading
import socket
import time
import json
import numpy


class Client:

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self._host = host
        self._port = port

        self.sock.connect((self._host, self._port))
        
        self.exiting = False

        # receiver_thread = threading.Thread(target=self.receive)
        # receiver_thread.start()

    def receive(self):
        while not self.exiting:
            try:
                message = self.sock.recv(1024).decode()
                print(message)
            except:
                self.stop()

    def write(self, data):
        message = json.dumps(data).encode()
        
        self.sock.send(message)
        # self.sock.send('.q'.encode())

    def stop(self):
        self.sock.send('.q'.encode())
        self.exiting = True
        self.sock.close()

  
if __name__ == '__main__':
  # HOST = '172.25.43.197'
  HOST = 'localhost'
  PORT = 8585
  client = Client(HOST, PORT)
  time.sleep(2)
  
#   client.write({'x': 0, 'y': 0, 'color': (255, 255, 0, 255)})
  client.write({'x': 5, 'y': 3, 'color': (50, 120, 0, 255)})
  client.stop()

