# https://www.codegrepper.com/profile/cute-copperhead-yqsmpcburmyp
import threading
import socket
import time
import json
import numpy as np
from PIL import Image


class Client:

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self._host = host
        self._port = port

        self.sock.connect((self._host, self._port))
        
        print(f'[CONN] Connected on port {self._port}')
        
        self.exiting = False

        receiver_thread = threading.Thread(target=self.receive)
        receiver_thread.start()

    def receive(self):
        while not self.exiting:
            try:
                message = self.sock.recv(10240)
                print(len(message))
                message = message.decode()
                # print(message)
                json_data = json.loads(message)
                
                print('MSG] Received image data')
                
                self.update_image(json_data)
                
            except ConnectionAbortedError:
                self.stop()
                break
            
            except json.JSONDecodeError:
                print('json error :()')
                pass

    def write(self, data):
        message = json.dumps(data).encode()
        
        self.sock.send(message)

    def update_image(self, json_data):
        image_flat = np.array(json_data['arr'], dtype=np.uint8)
        image_data = image_flat.reshape(json_data['shape'])
        
        img = Image.fromarray(image_data)
        img.save('test.png')
        
    def stop(self):
        self.sock.send('.q'.encode())
        self.exiting = True
        self.sock.close()

  
if __name__ == '__main__':
#   HOST = socket.gethostbyname('172.25.41.213')
  HOST = 'localhost'
  PORT = 8585
  client = Client(HOST, PORT)
  time.sleep(2)
  
#   client.write({'x': 0, 'y': 0, 'color': (255, 255, 0, 255)})
  
  while True:
      m = input('> ')
      m_split = m.split()
      
      if len(m_split) == 0:
          break
      
      print(m_split)
      
      client.write({'x': int(m_split[0]), 'y': int(m_split[1]), 'color': (255, 120, 0, 255)})
  client.stop()

