# https://www.codegrepper.com/profile/cute-copperhead-yqsmpcburmyp
import socket
import threading
import json
import numpy as np
from PIL import Image


class Server():
    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._port = port

        self.sock.bind(('127.0.0.1', self._port))
        self.sock.listen()

        self.clients = []
        
        img = Image.open('init.png', mode='r')
        self.pixels = np.array(img)

        
        # self.pixels = np.zeros([16, 16, 3], dtype=np.uint8)

    def start(self):
        while True:
            client, address = self.sock.accept()
            
            self.clients.append(client)

            connection_handler = threading.Thread(target=self.connection_handler, args=(client, address,))
            connection_handler.start()

    def connection_handler(self, client, address):
        while True:
            # Wait for pixel command
            # ...
            try:
                raw_message = client.recv(1024).decode()
                
                if raw_message == '.q':
                    self.clients.remove(client)
                    client.close()
                    break
                
                message = json.loads(raw_message)
            
                # Process pixel
                # ...
                print(message)
                self.pixels[message['y'], message['x']] = message['color']
                
                img = Image.fromarray(self.pixels)
                img.save('test.png')
                
                # Send updated canvas
                # self.broadcast()
            
            except ConnectionAbortedError:
                break
            
            except json.JSONDecodeError:
                pass
            # except:
            #     print('Error')
            #     client.close()
            #     break
            
    def broadcast(self):
        for client in self.clients:
            client.send('BROADCAST'.encode())


if __name__ == '__main__':
    s = Server(8080)
    s.start()