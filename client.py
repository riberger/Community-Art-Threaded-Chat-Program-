# https://www.codegrepper.com/profile/cute-copperhead-yqsmpcburmyp
import threading
import socket
import time
import json
import numpy as np
from PIL import Image
from gui import GUI
from tkinter.colorchooser import askcolor


class Client(GUI):

    def __init__(self, host, port):
        # Initialize TCP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self._host = host
        self._port = port

        # Initialize conneciton
        self.sock.connect((self._host, self._port))
        print(f'[CONN] Connected on port {self._port}')
        
        self.exiting = False  # handles graceful exit

        # Spin up receiver
        receiver_thread = threading.Thread(target=self.receive)
        receiver_thread.start()
        
        # Spin up GUI
        super().__init__()
        
        self.stop()

    def receive(self):
        time.sleep(2)
        
        # Keep receiving
        while not self.exiting:
            try:
                # Convert message to JSON
                message = self.sock.recv(10240)
                message = message.decode()
                json_data = json.loads(message)
                
                print('[MSG] Received image data')
                
                # Get updated image
                self.update_image(json_data)
                self.change_img()
                
            except ConnectionAbortedError:
                self.stop(open=False)
                break
            except OSError:
                self.stop(open=False)
                break
            except json.JSONDecodeError:  # if buffer receives blank line
                pass
    
    '''
    Writes to socket a JSON object containing 
    which pixel to update.
    
    @params
        data (JSON): pixel position and color to change
    '''
    def write(self, data):
        message = json.dumps(data).encode()
        
        self.sock.send(message)
    
    '''
    Extract inputted data and write to server
    '''
    def submit(self):
        # Obtain designated color
        colors = askcolor(title="Color Chooser")
        color = colors[0]
        
        # Extract input data
        x, y = self.send_bits()  
        
        if x != -1 and y != -1:
            color = list(color)
            color.append(255)  # append opacity
            
            data = {'x': x, 'y': y, 'color': color}
            
            self.write(data)
        
    def update_image(self, json_data):
        image_flat = np.array(json_data['arr'], dtype=np.uint8)
        image_data = image_flat.reshape(json_data['shape'])
        
        img = Image.fromarray(image_data)
        img.save('test.png')
        
    def stop(self, open=True):
        if open:
            self.sock.send('.q'.encode())
        self.exiting = True
        self.sock.close()

  
if __name__ == '__main__':
#   HOST = socket.gethostbyname('172.25.41.213')
  HOST = 'localhost'
  PORT = 8585
  client = Client(HOST, PORT)

