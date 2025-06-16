#walls of map:
def map1():
    map = [
    # Outer walls (bigger rectangle)
    (0, 0, 2400, 20),           # Top outer 
    (0, 1780, 2400, 20),        # Bottom outer 
    (0, 0, 20, 1800),           # Left outer 
    (2380, 0, 20, 1800),        # Right outer 

    # Inner maze walls with bigger doors (larger gaps)

    # Horizontal walls
    (150, 150, 400, 20),
    (650, 200, 20, 350),
    (670, 550, 20, 350),
    (690, 900, 300, 20),
    (1200, 600, 20, 500),
    (1220, 1100, 600, 20),
    (1850, 400, 20, 800),
    (1500, 300, 600, 20),

    # Vertical walls
    (200, 200, 20, 400),        # vertical with big door gap below
    (400, 600, 20, 400),
    (800, 700, 400, 20),
    (1400, 1200, 20, 400),
    (1600, 1400, 400, 20),
    ]
    return map
# ...existing code...


def map2():
    # All walls are 20px thick, doorways are 60px or wider (players fit)
    map = [
        # Outer walls
        (0, 0, 2400, 20),           # Top
        (0, 1780, 2400, 20),        # Bottom
        (0, 0, 20, 1800),           # Left
        (2380, 0, 20, 1800),        # Right

        # Central corridor (horizontal, with doorways)
        (200, 400, 800, 20),        # Left corridor
        (1200, 400, 1000, 20),      # Right corridor

        # Vertical walls for rooms (with doorways)
        (200, 420, 20, 400),        # Left vertical
        (1180, 420, 20, 400),       # Right vertical

        # Top left room
        (200, 100, 400, 20),        # Top wall
        (200, 100, 20, 320),        # Left wall
        (600, 100, 20, 320),        # Right wall
        (220, 400, 180, 20),        # Bottom left (doorway at 400-460)
        (420, 400, 180, 20),        # Bottom right (doorway at 380-420)

        # Top right room
        (1400, 100, 400, 20),       # Top wall
        (1400, 100, 20, 320),       # Left wall
        (1800, 100, 20, 320),       # Right wall
        (1420, 400, 180, 20),       # Bottom left (doorway at 1600-1640)
        (1620, 400, 180, 20),       # Bottom right (doorway at 1800-1840)

        # Bottom left room
        (200, 900, 400, 20),        # Top wall
        (200, 900, 20, 320),        # Left wall
        (600, 900, 20, 320),        # Right wall
        (220, 1200, 180, 20),       # Bottom left (doorway at 400-440)
        (420, 1200, 180, 20),       # Bottom right (doorway at 380-420)

        # Bottom right room
        (1400, 900, 400, 20),       # Top wall
        (1400, 900, 20, 320),       # Left wall
        (1800, 900, 20, 320),       # Right wall
        (1420, 1200, 180, 20),      # Bottom left (doorway at 1600-1640)
        (1620, 1200, 180, 20),      # Bottom right (doorway at 1800-1840)

        # Central vertical wall with two doorways
        (1190, 600, 20, 200),       # Top segment
        (1190, 900, 20, 200),       # Bottom segment

        # Additional small rooms in the center
        (900, 700, 200, 20),        # Top wall
        (900, 700, 20, 200),        # Left wall
        (1080, 700, 20, 200),       # Right wall
        (920, 900, 180, 20),        # Bottom wall (doorway at 1000-1040)

        (1300, 700, 200, 20),       # Top wall
        (1300, 700, 20, 200),       # Left wall
        (1480, 700, 20, 200),       # Right wall
        (1320, 900, 180, 20),       # Bottom wall (doorway at 1400-1440)
    ]
    return map

def map3():
    # All walls are 20px thick, doorways are ≥100px wide
    map = [
        # Outer walls
        (0, 0, 2400, 20),
        (0, 1780, 2400, 20),
        (0, 0, 20, 1800),
        (2380, 0, 20, 1800),

        # Central vertical corridor
        (1190, 100, 20, 500),
        (1190, 700, 20, 200),
        (1190, 1000, 20, 200),
        (1190, 1300, 20, 400),

        # Central horizontal corridor (wider)
        (400, 870, 760, 40),
        (1220, 870, 780, 40),

        # Top left room
        (200, 100, 400, 20),
        (200, 100, 20, 300),
        (600, 100, 20, 300),
        (220, 400, 140, 20),     # left of doorway
        (460, 400, 140, 20),     # right of doorway

        # Top center-left room
        (700, 100, 400, 20),
        (700, 100, 20, 300),
        (1100, 100, 20, 300),
        (720, 400, 140, 20),
        (960, 400, 140, 20),

        # Top right rooms
        (1300, 100, 400, 20),
        (1300, 100, 20, 300),
        (1700, 100, 20, 300),
        (1320, 400, 140, 20),
        (1560, 400, 140, 20),

        (1800, 100, 400, 20),
        (1800, 100, 20, 300),
        (2200, 100, 20, 300),
        (1820, 400, 140, 20),
        (2060, 400, 140, 20),

        # Bottom left room
        (200, 1100, 400, 20),
        (200, 1100, 20, 300),
        (600, 1100, 20, 300),
        (220, 1400, 140, 20),
        (460, 1400, 140, 20),

        # Bottom center-left room
        (700, 1100, 400, 20),
        (700, 1100, 20, 300),
        (1100, 1100, 20, 300),
        (720, 1400, 140, 20),
        (960, 1400, 140, 20),

        # Bottom right rooms
        (1300, 1100, 400, 20),
        (1300, 1100, 20, 300),
        (1700, 1100, 20, 300),
        (1320, 1400, 140, 20),
        (1560, 1400, 140, 20),

        (1800, 1100, 400, 20),
        (1800, 1100, 20, 300),
        (2200, 1100, 20, 300),
        (1820, 1400, 140, 20),
        (2060, 1400, 140, 20),

        # Central side rooms (with 100px doorway gaps)
        (1000, 700, 180, 20),
        (1000, 700, 20, 180),
        (1160, 700, 20, 180),
        (1020, 880, 100, 20),

        (1220, 700, 180, 20),
        (1220, 700, 20, 180),
        (1380, 700, 20, 180),
        (1240, 880, 100, 20),
    ]
    return map




