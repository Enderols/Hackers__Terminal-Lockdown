Battle Royale Hacker Game

A multiplayer battle royale game where players compete to hack control points and eliminate opponents. Built with Python, supporting 1 to N players on the same network.


📌 Features:

✔ Multiplayer Support – Play with friends over LAN.
✔ Hack Control Points – Capture "hackpoints" to earn points.
✔ Combat System – Shoot enemies to eliminate them.
✔ Dynamic Map – Explore and strategize in a changing arena.
✔ Real-Time Networking – Smooth gameplay using a custom server-client model.

🕹️ Controls:
Action - Key:
    Move - WASD
    Aim - Mouse
    Shoot - Space
    Hack Terminal - E

📜 Rules & Scoring
    Terminal Hacks: gain 30 health temporarly and get more amo
    Winning: Last player standing wins the round
    Health: Starts at 100, can be temporarily boosted to 130 via hacks

🌐 LAN Multiplayer Setup
1. Server Setup (Host Machine)
Run:
python server.py
    The server will automatically start on port 5555
   
    To change IP/port: Edit these files:
        network.py (Line 4): self.server = "192.168.178.1" → Your server's local IP
        server.py (Line 6): server = "192.168.178.1" → Match above IP
   
3. Client Setup (Player Machines)

Run the executable:
HackersTerminalLockdownV1_1.exe

Choose a username in the pop-up window and conect

When all clents are conectet press Start on the server!
