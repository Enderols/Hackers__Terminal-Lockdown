import socket, pickle, random
from _thread import *
from sys import *
#from player import Player
import tkinter as tk

global gameStart
gameStart = False
server = "192.168.178.1"
port = 5555

def threaded_client(conn, playerId):
    if gameStart == True:
        conn.send(pickle.dumps(None))
        return # If the game has already started, do not allow new connections

    conn.send(pickle.dumps(playerId))
    global currentPlayer
    reply = []
    while not gameStart:
        pass
    conn.send(pickle.dumps(len(players)))
    while True:
        if gameStart == False:
            print("Game Stopped")
            players[playerId] = None
            if all(p is None for p in players):
                print("All clients disconnected. Clearing players list.")
                players.clear()
                currentPlayer = 0
            break
        try:
            data = pickle.loads(conn.recv(2048))
            players[playerId] = data

           
            if not data: 
                print("Disconnected")
                break
            else:                        

                reply = players.copy()  # Send a copy of the players list to all clients
                
                #print("Received: ", data)
                #print("Sending: ", reply)
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

def reset_button_clicked():
    global gameStart
    gameStart = False

def checkForGameStart():
    # Create the main window
    strtwin = tk.Tk()
    strtwin.title("Start Game")
    # Create and pack the start button
    startButton = tk.Button(strtwin, text="Start", command=start_button_clicked)
    resetButton = tk.Button(strtwin, text="Reset", command=reset_button_clicked)
    startButton.pack(pady=20)
    resetButton.pack(pady=20)
    strtwin.mainloop()
       


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
    
except socket.error as e:
    print(str(e))

s.listen(16) #max connections
start_new_thread(checkForGameStart, ())
print("Waiting for a connection, Server Started")
global currentPlayer


#players = [Player(0,0,50,50, (255,0,0)), Player(33,33,50,50, (0,0,255))]
players = []

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    players.append(None) # Initialize with None for new player
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    
