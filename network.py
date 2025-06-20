import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.178.1"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        
    def getId(self):
        return self.id
    
    def getNumOfPlayers(self):
        try:
            return pickle.loads(self.client.recv(2048))
        except:
            return None 
        
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass
        
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
    