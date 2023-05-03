# https://www.codegrepper.com/profile/cute-copperhead-yqsmpcburmyp
import socket
import threading
import json
import numpy as np
from PIL import Image


class Server():
    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._host = '0.0.0.0'
        self._port = port

        
        self.sock.bind((self._host, self._port))

        self.clients = []
        
        img = Image.open('init.png', mode='r')
        self.pixels = np.array(img)

    def start(self):
        self.sock.listen(5)
        print(f'[INIT] Server listening on {self._port}')
        while True:
            client, address = self.sock.accept()
            
            print(f'[CONN] Connection accepted with {address}')
            
            self.clients.append(client)
            
            # TODO: Send starter image
            bytes_data = self.get_image_bytes()
            client.send(bytes_data)

            connection_handler = threading.Thread(target=self.connection_handler, args=(client, address,))
            connection_handler.start()
        
        
            
    def get_image_bytes(self):
        flat_arr = self.pixels.flatten()
        flat_arr = flat_arr.tolist()
        
        data = {'shape': self.pixels.shape, 'arr': flat_arr}
        
        json_data = json.dumps(data)
        bytes_data = json_data.encode()
        
        return bytes_data

    def connection_handler(self, client, address):
        while True:
            # Wait for pixel command
            try:
                raw_message = client.recv(1024).decode()

                if raw_message == '.q':
                    self.terminate(client, address)
                    break
                
                message = json.loads(raw_message)
            
                # Process pixel
                print(f'[MSG] Recieved {message} from {address}')
                self.pixels[message['y'], message['x']] = message['color']
                
                # Send updated canvas
                self.broadcast()
            
            except ConnectionAbortedError:
                self.terminate(client, address)
                break
            
            except json.JSONDecodeError:
                pass
            
    def terminate(self, client, address):
        self.clients.remove(client)
        client.close()
        print(f'[CONN] Connection closed with {address}')
        
            
    def broadcast(self):
        bytes_image = self.get_image_bytes()
        for client in self.clients:
            client.send(bytes_image)


if __name__ == '__main__':
    s = Server(8585)
    s.start()