import socket, pickle, random
from _thread import *
from sys import *
from player import Player


server = "10.0.0.11"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
    
except socket.error as e:
    print(str(e))

s.listen(16) #max connections
print("Waiting for a connection, Server Started")


#players = [Player(0,0,50,50, (255,0,0)), Player(33,33,50,50, (0,0,255))]
players = []


def threaded_client(conn, playerId):
    conn.send(pickle.dumps(players[playerId]))
    reply = []
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[playerId] = data
            
            if not data: 
                print("Disconnected")
                break
            else:
                reply = players.copy()  # Send a copy of the players list to all clients
                
                print("Received: ", data)
                print("Sending: ", reply)
            
            conn.sendall(pickle.dumps(reply))
            
        except:
            print("Error")
            break
    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    players.append(Player(currentPlayer, random.randint(0, 450), random.randint(0, 450), 50, 50, (random.randint(0,255), random.randint(0,255), random.randint(0,255))))
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    
