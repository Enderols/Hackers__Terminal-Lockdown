import socket, pickle
from _thread import *
from sys import *
from player import Player

server = "192.168.210.59"#"10.0.0.18"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
    
except socket.error as e:
    print(str(e))

s.listen(2) #max connections
print("Waiting for a connection, Server Started")


players = [Player(0,0,50,50, (255,0,0)), Player(0,0,50,50, (0,0,255))]



def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            
            if not data: 
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                
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
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    
