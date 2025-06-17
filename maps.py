#walls of map:
def map1():
    map = []

    wall = 20
    door = 100

    # === Outer Walls ===
    map += [
        (0, 0, 4800, wall),             # Top
        (0, 3580, 4800, wall),          # Bottom
        (0, 0, wall, 3600),             # Left
        (4780, 0, wall, 3600),          # Right
    ]

    # === Room Block A (Top-Left 3x2 rooms) ===
    room_w = 500
    room_h = 400
    spacing = 100
    origin_x = 100
    origin_y = 100

    for row in range(2):
        for col in range(3):
            x = origin_x + col * (room_w + spacing)
            y = origin_y + row * (room_h + spacing)

            # Room box with bottom door
            map += [
                (x, y, room_w, wall),                            # Top
                (x, y, wall, room_h),                            # Left
                (x + room_w - wall, y, wall, room_h),            # Right
                (x, y + room_h - wall, (room_w - door) // 2, wall),      # Bottom-left
                (x + (room_w + door) // 2, y + room_h - wall, (room_w - door) // 2, wall),  # Bottom-right
            ]

    # === Central Corridor Horizontal ===
    map += [
        (700, 1200, 1200, wall),
        (700, 1220, wall, 400),
        (1900, 1220, wall, 400),
        (700, 1620, 1200, wall),
    ]

    # === Central Big Room ===
    big_x, big_y = 1500, 1800
    big_w, big_h = 1400, 800
    map += [
        (big_x, big_y, big_w, wall),
        (big_x, big_y + big_h - wall, big_w, wall),
        (big_x, big_y, wall, big_h),
        (big_x + big_w - wall, big_y, wall, big_h),
        # Doors
        (big_x + big_w//2 - door//2, big_y, door, wall),
        (big_x + big_w//2 - door//2, big_y + big_h - wall, door, wall),
        (big_x, big_y + big_h//2 - door//2, wall, door),
        (big_x + big_w - wall, big_y + big_h//2 - door//2, wall, door),
    ]

    # === Vertical Maze Corridor Right Side ===
    vx = 3000
    vy = 400
    for i in range(5):
        map.append((vx, vy + i * 300, wall, 200))
        if i % 2 == 0:
            map.append((vx, vy + i * 300 + 200, 500, wall))

    # === Lower Left Room Group ===
    for i in range(2):
        x = 200 + i * 700
        y = 2600
        map += [
            (x, y, 600, wall),
            (x, y, wall, 500),
            (x + 600 - wall, y, wall, 500),
            (x, y + 500 - wall, (600 - door) // 2, wall),
            (x + (600 + door) // 2, y + 500 - wall, (600 - door) // 2, wall),
        ]

    return map




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
    map = [
    # Outer boundaries (scaled to 2400x1800)
    (0, 0, 2400, 50),        # Top border
    (0, 0, 50, 1800),        # Left border
    (2350, 0, 50, 1800),     # Right border
    (0, 1750, 2400, 50),     # Bottom border

#Central structure (halved dimensions)
    (900, 600, 600, 400),    # Main combat zone
    (1000, 700, 100, 200),   # Central pillar
    (1300, 700, 100, 200),   # Central pillar

#North wing
    (200, 200, 400, 300),    # Northwest room
    (200, 400, 175, 50),     # NW room entrance wall
    (425, 400, 175, 50),     # NW room entrance continuation
    (600, 200, 200, 200),    # North hallway
    (700, 400, 100, 50),     # North choke point

#East wing
    (1600, 400, 500, 400),   # Eastern barracks
    (1600, 700, 200, 50),    # Barracks left entrance
    (1900, 700, 200, 50),    # Barracks right entrance
    (1800, 1000, 300, 500),  # Southeast armory
    (1900, 1000, 100, 50),   # Armory entrance

#Open areas
    (400, 900, 50, 400),     # West courtyard left
    (950, 900, 50, 400),     # West courtyard right
    (1200, 1200, 600, 50),   # Southern plaza north

#Hallways
    (800, 500, 100, 100),    # North-south choke
    (1100, 1100, 200, 50),   # East-west connector
    (1500, 800, 50, 400),    # Vertical hallway

#Cover objects (slightly smaller but proportional)
    (500, 600, 40, 40),      # Small crate
    (1400, 1400, 60, 40),    # Long crate

#Special areas
    (200, 1400, 300, 300),   # Southwest sniper nest
    (200, 1600, 100, 50),    # Sniper nest entrance
    (1900, 200, 400, 300),   # Northeast power position
    (2100, 400, 100, 50)     # Power position entrance
]
    return map

def map4():
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

        # Top right room (INACCESSIBLE: gap in bottom wall too wide for doorway)
        (1400, 100, 400, 20),       # Top wall
        (1400, 100, 20, 320),       # Left wall
        (1800, 100, 20, 320),       # Right wall
        (1420, 400, 100, 20),       # Bottom left segment
        (1720, 400, 80, 20),        # Bottom right segment (gap of 200px at 1520-1720)

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

        # --- New obstacles and partial walls in empty areas ---

        # Central bottom-left area
        (800, 1400, 120, 20),       # Horizontal obstacle
        (960, 1450, 20, 100),       # Vertical post

        # Central bottom-right area
        (1400, 1400, 200, 20),      # Horizontal barrier
        (1500, 1450, 20, 100),      # Vertical post

        # Left-middle region
        (100, 600, 100, 20),        # Small wall
        (160, 640, 20, 80),         # Post below it

        # Far right middle
        (2200, 800, 100, 20),       # Thin horizontal wall
        (2250, 820, 20, 80),        # Vertical pillar

        # Top center open field
        (1100, 200, 200, 20),       # Mid-field wall
        (1180, 220, 20, 100),       # Vertical short wall
    ]
    hackpoints = [
        (1800/2,2400/2),
        (1800/3,2400/3)
    ]
    return map, hackpoints

def map5():
    map_walls = [
    # Outer boundaries (thinner walls)
    (0, 0, 2400, 30),        # Top border
    (0, 0, 30, 1800),        # Left border
    (2370, 0, 30, 1800),     # Right border
    (0, 1770, 2400, 30),     # Bottom border

#Central structure (more open with cover)
    (900, 600, 600, 400),    # Main combat zone
    (1000, 700, 80, 200),    # Central pillar (thinner)
    (1320, 700, 80, 200),    # Central pillar (thinner)
    (1100, 800, 40, 40),     # Small cover
    (1300, 800, 40, 40),     # Small cover
    (1200, 900, 80, 40),     # Low wall cover

#North wing (more accessible)
    (200, 200, 400, 300),    # Northwest room
    (200, 400, 150, 30),     # Entrance wall (wider gap)
    (450, 400, 150, 30),     # Entrance continuation
    (600, 200, 200, 200),    # North hallway
    (700, 400, 100, 30),     # Choke point (thinner)

#East wing (more open entrances)
    (1600, 400, 500, 400),   # Eastern barracks
    (1600, 700, 220, 30),    # Wider entrance
    (1880, 700, 220, 30),    # Wider entrance
    (1800, 1000, 300, 500),  # Southeast armory
    (1850, 1000, 200, 30),   # Wider entrance

#Open areas with scattered cover
    (400, 900, 30, 400),     # West courtyard left
    (950, 900, 30, 400),     # West courtyard right
    (500, 1000, 60, 60),     # Crate cover
    (800, 1100, 60, 60),     # Crate cover
    (1200, 1200, 600, 30),   # Southern plaza north
    (1250, 1250, 40, 40),    # Barrel cover
    (1450, 1300, 80, 40),    # Low wall



#Hallways (slightly wider)
    (800, 500, 100, 100),    # North-south choke
    (1100, 1100, 200, 30),   # East-west connector
    (1500, 800, 30, 400),    # Vertical hallway (thinner)

#More cover in open zones
    (300, 1500, 60, 60),     # Crate in sniper nest area
    (400, 1600, 120, 30),    # Low wall cover
    (1900, 300, 60, 60),     # Crate in power position
    (2100, 400, 100, 30),    # Wider entrance

#Additional tactical cover
    (1400, 500, 40, 40),     # Small cover near central
    (1600, 1000, 40, 40),    # Cover near armory
    (2000, 800, 60, 30)      # Low wall in open area
    ]

    hackpoints = [
    # -- Central Open Area (High Traffic) --
    (1050, 750),  # Near central pillar (east side)
    (1250, 850),  # Low cover near south exit
    (1420, 720),  # West of right pillar
    (950, 680),   # Near left pillar (safe gap)

    # -- North Wing (Controlled Rooms) --
    (300, 300),   # NW room corner
    (500, 450),   # Near hallway entrance
    (720, 280),   # North hallway side
    (650, 500),   # Connector to courtyard

    # -- East Wing (Barracks & Armory) --
    (1700, 500),  # Barracks left side
    (1880, 620),  # Barracks right side
    (1820, 1100), # Armory entrance
    (1950, 1300), # SE armory back

    # -- West Courtyard (Scattered Cover) --
    (480, 920),   # Behind left wall
    (600, 1050),  # Near crate
    (820, 1180),  # Along low wall
    (900, 1250),  # Plaza transition

    # -- Southern Plaza (Open but Risky) --
    (1280, 1280), # Near low wall
    (1450, 1400), # Behind central obstacle
    (1600, 1500), # Far southeast
    (1750, 1350), # Near armory exit

    # -- Special Areas (High-Value) --
    (350, 1480),  # Sniper nest approach
    (2200, 420),  # Power position flank

    # -- Hallway Hotspots --
    (880, 580),   # North-south choke
    (1180, 1180), # East-west connector
    (1520, 900)   # Vertical hallway junction
]
    return map_walls, hackpoints