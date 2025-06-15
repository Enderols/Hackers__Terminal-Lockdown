import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
<<<<<<< HEAD
        self.server = "192.168.0.1"#"192.168.30.209"#"192.168.30.59"#
=======
        self.server = "10.10.208.211"#"192.168.30.209"#"192.168.30.59"#
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        
    def getId(self):
        return self.id
<<<<<<< HEAD
    
    def getNumOfPlayers(self):
        try:
            return pickle.loads(self.client.recv(2048))
        except:
            return None 
=======
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae
        
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
    