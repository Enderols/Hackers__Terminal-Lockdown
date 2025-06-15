import socket, pickle, random
from _thread import *
from sys import *
#from player import Player
<<<<<<< HEAD
import tkinter as tk

global gameStart
gameStart = False
server = "192.168.0.1"
=======


server = "10.10.208.211"
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae
port = 5555

def threaded_client(conn, playerId):
    conn.send(pickle.dumps(playerId))
    global currentPlayer
    reply = []
    while not gameStart:
        pass
    conn.send(pickle.dumps(len(players)))
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[playerId] = data

           
            
            if not data: 
                print("Disconnected")
                break
            else:
            
                if players[playerId]["givendamage"]:
                    print(players[playerId]["givendamage"])
                    for key in players[playerId]["givendamage"]:
                        players[key]["health"] = players[playerId]["givendamage"][key]
                        print(f"Player {key} health updated to {players[key]['health']}")
                        

            reply = players.copy()  # Send a copy of the players list to all clients
                
                #print("Received: ", data)
                #print("Sending: ", reply)
            print(f"health von spieler {playerId}: {reply[playerId]["health"]}")
            conn.sendall(pickle.dumps(reply))
            
        except:
            print("Error")
            players[playerId] = None
            if all(p is None for p in players):
                print("All clients disconnected. Clearing players list.")
                players.clear()
                currentPlayer = 0
            break
    print("Lost connection")
    
    conn.close()

def start_button_clicked():
    global gameStart
    gameStart = True

def checkForGameStart():
    # Create the main window
    strtwin = tk.Tk()
    strtwin.title("Start Game")
    # Create and pack the start button
    start_button = tk.Button(strtwin, text="Start", command=start_button_clicked)
    start_button.pack(pady=20)
    strtwin.mainloop()
       


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
    
except socket.error as e:
    print(str(e))

s.listen(16) #max connections
<<<<<<< HEAD
start_new_thread(checkForGameStart, ())
=======
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae
print("Waiting for a connection, Server Started")
global currentPlayer


#players = [Player(0,0,50,50, (255,0,0)), Player(33,33,50,50, (0,0,255))]
players = []
<<<<<<< HEAD
=======


def threaded_client(conn, playerId):
    conn.send(pickle.dumps(playerId))
    global currentPlayer
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
            players[playerId] = None
            if all(p is None for p in players):
                print("All clients disconnected. Clearing players list.")
                players.clear()
                currentPlayer = 0
            break
    print("Lost connection")
    
    conn.close()
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae

currentPlayer = 0
while True:
    
    conn, addr = s.accept()
    print("Connected to: ", addr)
    players.append(None) # Initialize with None for new player
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    
