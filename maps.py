from game import Wall
#walls of map:
def map1():
    m1 = [
    # Outer walls (bigger rectangle)
    Wall(0, 0, 2400, 20),           # Top outer wall
    Wall(0, 1780, 2400, 20),        # Bottom outer wall
    Wall(0, 0, 20, 1800),           # Left outer wall
    Wall(2380, 0, 20, 1800),        # Right outer wall
    ]
    return m1