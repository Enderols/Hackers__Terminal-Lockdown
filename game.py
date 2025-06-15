import pygame
import math
import sys
from network import Network
#from network import Network

# --- Settings ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600#
WORLD_WIDTH, WORLD_HEIGHT = 2400, 1800  #map size
ZOOM = 1.5

# --- pygame setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hackers: Terminal Lockdown")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


# --- Network setup ---
n = Network()
# --- Game objects ---
# Walls class
walls = []
class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        walls.append(self.rect)



# Hacking points
hackpoints = []
class HackingPoint:
    def __init__(self,pos):
        self.image_orig = pygame.Surface((40, 20), pygame.SRCALPHA)
        pygame.draw.rect(self.image_orig, (255, 0, 0), (0, 0, 40, 20))
        self.pos = pygame.Vector2(pos)
        self.health = 100
        self.displayed_health = 100  # For smooth animation
        self.angle = 0
        self.speed = 4
        hackpoints.append(self)

    def draw(self, surface):
        # Animate displayed_health towards actual health
        speed = 2  # Higher = faster animation
        if self.displayed_health < self.health:
            self.displayed_health = min(self.health, self.displayed_health + speed)
        elif self.displayed_health > self.health:
            self.displayed_health = max(self.health, self.displayed_health - speed)

        # Draw the hacking point itself
        image = pygame.transform.rotate(self.image_orig, -math.degrees(self.angle))
        rect = image.get_rect(center=self.pos)
        surface.blit(image, rect)
        # Only draw the loading bar if health < 100 or animation not finished
        if self.displayed_health < 100:
            bar_width = 40
            bar_height = 6
            bar_x = self.pos.x - bar_width // 2
            bar_y = self.pos.y - 25
            # Background bar (gray)
            pygame.draw.rect(surface, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height))
            # Foreground bar (green, proportional to displayed_health)
            health_ratio = max(self.displayed_health, 0) / 100
            pygame.draw.rect(surface, (0, 200, 0), (bar_x, bar_y, int(bar_width * health_ratio), bar_height))
    
# ___playersclass___
<<<<<<< HEAD

class Player:
    def __init__(self, pos, id,name="unknown"):
=======
players = []
class Player:
    def __init__(self, pos, name="unknown"):
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae
        self.image_orig = pygame.Surface((40, 20), pygame.SRCALPHA)
        pygame.draw.polygon(self.image_orig, (0, 0, 255), [(0, 0), (40, 10), (0, 20)])
        self.id = id
        self.pos = pygame.Vector2(pos)
        self.angle = 0
        self.speed = 4
        self.health = 100
<<<<<<< HEAD
        self.points = 0
        self.name = name
        self.hit_timer = 0  # Add this line
        players[self.id] = self
        self.hack_cooldown = 0
        self.hack_delay = 60  # 60 frames = 1 second at 60 FPS
        self.ammo = 200000000000

        self.damagedict = {}  # Dictionary to track damage given to other players

        
=======
        self.name = name
        self.hit_timer = 0  # Add this line
        players.append(self)
        self.hack_cooldown = 0
        self.hack_delay = 60  # 60 frames = 1 second at 60 FPS
        self.ammo = 20
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae

        self.shoot_cooldown = 0
        self.shoot_delay = 24  # 24 Frames = 0.4s bei 60 FPS

    def update(self, mouse_world_pos, keys):
        global player_dead
        if self.health <= 0 and not player_dead:
            self.health = 0
            player_dead = True
            if self in players:
                players.remove(self)
            return  # Stop further updates if dead

        forward = pygame.Vector2(math.cos(self.angle), math.sin(self.angle))
        right = pygame.Vector2(-forward.y, forward.x)
        move = pygame.Vector2(0, 0)

        # Decrease hit_timer if active
        if self.hit_timer > 0:
            self.hit_timer -= 1

    def draw(self, surface):
        # Choose color based on hit_timer
        color = (255, 0, 0) if self.hit_timer > 0 else (0, 0, 255)
        image = pygame.Surface((40, 20), pygame.SRCALPHA)
        pygame.draw.polygon(image, color, [(0, 0), (40, 10), (0, 20)])
        rotated = pygame.transform.rotate(image, -math.degrees(self.angle))
        rect = rotated.get_rect(center=self.pos)
        surface.blit(rotated, rect)
        # Draw name
        font = pygame.font.Font(None, 24)
        name_surf = font.render(self.name, True, (0, 0, 0))
        name_rect = name_surf.get_rect(center=(self.pos.x, self.pos.y - 25))
        surface.blit(name_surf, name_rect)

    def shoot(self):
        if self.ammo <= 0:
            print("Out of ammo!")
            return
        else:
            print(f"Remaining ammo: {self.ammo}")
            self.ammo -= 1
            length = 1000
            direction = pygame.Vector2(math.cos(self.angle), math.sin(self.angle))
            start = self.pos + direction * 25
            end = start + direction * length

            # Find the closest wall intersection
            min_dist = float('inf')
            hit_point = None
            for wall in walls:
                clipped = wall.clipline((start.x, start.y), (end.x, end.y))
                if clipped:
                    for pt in clipped:
                        dist = pygame.Vector2(pt).distance_to(start)
                        if dist < min_dist:
                            min_dist = dist
                            hit_point = pygame.Vector2(pt)
            if hit_point:
                end = hit_point

            # Check for player hits
<<<<<<< HEAD
            for p in players.values():  # Use a copy of the list in case we remove a player
=======
            for p in players[:]:  # Use a copy of the list in case we remove a player
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae
                if p is self:
                    continue
                player_rect = pygame.Rect(p.pos.x - 20, p.pos.y - 10, 40, 20)
                if player_rect.clipline((start.x, start.y), (end.x, end.y)):
                    p.health -= 10
<<<<<<< HEAD

                    self.damagedict[p.id] = p.health

                    p.hit_timer = 15
                    print(f"{p.name} got hit Health: {p.health}")
                    self.points += 10
=======
                    p.hit_timer = 15
                    print(f"{p.name} got hit Health: {p.health}")
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae
                    if p.health <= 0:
                        print(f"{p.name} died!")
                        p.health = 0
                        if p in players:
                            players.remove(p)
                    # Only hit one player per shot (optional: remove break if you want multi-hit)
                    break

            # Store the line coordinates for drawing
            global last_shot_coords, show_shot_line, shot_line_timer
            last_shot_coords = (start, end)
            show_shot_line = True
            shot_line_timer = 1  # Only show for 1 frame
<<<<<<< HEAD
    

class Client(Player):
    def __init__(self,pos,id):
        super().__init__(pos,id)
=======

class Client(Player):
    def __init__(self,pos):
        super().__init__(pos)
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae
        
    def update(self, mouse_world_pos, keys):
        direction = mouse_world_pos - self.pos
        self.angle = math.atan2(direction.y, direction.x)

        forward = pygame.Vector2(math.cos(self.angle), math.sin(self.angle))
        right = pygame.Vector2(-forward.y, forward.x)
        move = pygame.Vector2(0, 0)

        if keys[pygame.K_w]: move += forward
        if keys[pygame.K_a]: move -= right
        if keys[pygame.K_s]: move -= forward
        if keys[pygame.K_d]: move += right

        if self.hack_cooldown > 0:
            self.hack_cooldown -= 1

        if keys[pygame.K_h] and self.hack_cooldown == 0:
            for hackpoint in hackpoints:
                if self.pos.distance_to(hackpoint.pos) < 100:
                    hackpoint.health -= 20
                    print(f"Hacking Point Health: {hackpoint.health}")
                    self.hack_cooldown = self.hack_delay  # start cooldown

                    if hackpoint.health <= 0:
                        print("Hacking Point destroyed!")
                        self.points += 1
                        hackpoints.remove(hackpoint)
                        hackpoint.image_orig.fill((0, 0, 0, 0))
                    break  # Only hack one point at a time

        # Regenerate hackpoint health if not hacking (not pressing H or out of range)
        for hackpoint in hackpoints:
            in_range = self.pos.distance_to(hackpoint.pos) < 100
            if (not keys[pygame.K_h] or not in_range) and hackpoint.health < 100:
                hackpoint.health += 1  # Adjust speed as needed
                if hackpoint.health > 100:
                    hackpoint.health = 100

        if move.length() > 0:
            move = move.normalize() * self.speed
            self.try_move(move)

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        if keys[pygame.K_SPACE] and self.shoot_cooldown == 0:
            self.shoot()
            self.shoot_cooldown = self.shoot_delay

    def try_move(self, delta):
        new_pos = self.pos + delta
        player_rect = pygame.Rect(new_pos.x - 20, new_pos.y - 10, 40, 20)
        for wall in walls:
            if player_rect.colliderect(wall):
                return
        self.pos = new_pos

    def draw(self, surface):
        rotated = pygame.transform.rotate(self.image_orig, -math.degrees(self.angle))
        rect = rotated.get_rect(center=self.pos)
        surface.blit(rotated, rect)
<<<<<<< HEAD
    
    def send_data(self):
        data_dict = {
            "pos": self.pos,
            "angle":self.angle,
            "health": self.health,
            "id": self.id,
            "ammo": self.ammo,
            "points": self.points,
            "givendamage": self.damagedict.copy(),
            }
        if self.damagedict:
            print(self.damagedict)
        
        self.damagedict.clear()  # Clear after sending
        return data_dict.copy()
        
    
=======
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae

# Camera that follows the player
class Camera:
    def __init__(self, width, height, zoom):
        self.zoom = zoom
        self.width = width
        self.height = height

    def get_view_rect(self, target_pos):
        view_rect = pygame.Rect(0, 0, SCREEN_WIDTH / self.zoom, SCREEN_HEIGHT / self.zoom)
        view_rect.center = target_pos
        view_rect.clamp_ip(pygame.Rect(0, 0, self.width, self.height))
        return view_rect

    def apply(self, surface, view_rect):
        zoomed = pygame.transform.smoothscale(surface.subsurface(view_rect), (SCREEN_WIDTH, SCREEN_HEIGHT))
        return zoomed

last_shot_coords = None
show_shot_line = False
shot_line_timer = 0

#Update game 
def updategame():
    global player_dead
    world_surface = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))
    draw_world(world_surface)

    view_rect = camera.get_view_rect(player.pos)
    mouse_screen = pygame.Vector2(pygame.mouse.get_pos())
    mouse_world = mouse_screen / ZOOM + view_rect.topleft

    keys = pygame.key.get_pressed()
<<<<<<< HEAD
    for user in players.values():
=======
    for user in players:
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae
        user.update(mouse_world, keys)
        user.draw(world_surface)

    # Draw the main player if not dead (for local player)
    if not player_dead:
        player.draw(world_surface)

    # Draw all hacking points with loading bars
    for hackpoint in hackpoints:
        hackpoint.draw(world_surface)

    # Draw last shot line if shoot key is held
    global last_shot_coords, show_shot_line, shot_line_timer
    if show_shot_line and last_shot_coords and shot_line_timer > 0:
        start, end = last_shot_coords
        pygame.draw.line(world_surface, (255, 255, 0, 255), start, end, 10)  # Fully opaque, thicker
        shot_line_timer -= 1
    else:
        show_shot_line = False

    screen.blit(camera.apply(world_surface, view_rect), (0, 0))

    text = font.render(f"Health: {max(player.health, 0)}", True, (0, 255, 0), (0, 0, 128))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
    screen.blit(text, text_rect)

    if player.health <= 0:
        # Draw a semi-transparent grey overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((50, 50, 50, 180))  # RGBA: last value is alpha (transparency)
        screen.blit(overlay, (0, 0))

        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, game_over_rect)
        #cover the screen in transparent red
        print("Player died!")
        player.health = 0
        player_dead = True
        if player in players:
            players.remove(player)

<<<<<<< HEAD
    #if player in players:
        #print(player.pos, player.angle)
        
    data = n.send(player.send_data())  # Send player data to server
    #move players to the new data
    #print(data)
    for playerdict in data:
        
        if playerdict is None:
            continue
        i = playerdict["id"]
        if playerdict["id"] == player.id:
            player.health = playerdict["health"]
            players[i].health = playerdict["health"]
            print(playerdict["health"])
            continue
        else:
            #print("gegner ausgeführt")
            players[i].pos = pygame.Vector2(playerdict["pos"])
            players[i].angle = playerdict["angle"]
            players[i].health = playerdict["health"]
            players[i].ammo = playerdict["ammo"]
            players[i].points = playerdict["points"]

=======
        
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae

# Function to draw the world
def draw_world(surface):
    surface.fill((255, 255, 255))
    for wall in walls:
        pygame.draw.rect(surface, (0, 0, 0), wall)


def create_players():
    numofplayers = n.getNumOfPlayers()
    for i in range(numofplayers):
        if i == player.id:
            continue
        else:
            pos = (WORLD_WIDTH // 2 + i * 50, WORLD_HEIGHT // 2 + i * 50)
            Player(pos, id=i, name=f"Player {i}")


# Setup
<<<<<<< HEAD
players = {}



ClientId = n.getId()
print(f"Client ID: {ClientId}")
pygame.display.set_caption(f"Hackers: Terminal Lockdown - Client {ClientId}")

player = Client((WORLD_WIDTH // 2.5, WORLD_HEIGHT // 2.2), id=ClientId)
print(f"sending player: {player}")
#players=n.send(player)
print(players)

create_players()




=======
player = Client((WORLD_WIDTH // 2.5, WORLD_HEIGHT // 2.2))
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae
camera = Camera(WORLD_WIDTH, WORLD_HEIGHT, ZOOM)
bullets = []  # Liste aller Bullets

testhack = HackingPoint((WORLD_WIDTH // 2.5, WORLD_HEIGHT // 2.2))

<<<<<<< HEAD

=======
#bots
bot=Player((1000,800),"bot1")
Player((1000, 600),"bot2")
  # Add a bot player for testing
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae


# CHATGPT generierte Wände für test-zwecke

# Outer walls (bigger rectangle)
Wall(0, 0, 2400, 20)           # Top outer wall
Wall(0, 1780, 2400, 20)        # Bottom outer wall
Wall(0, 0, 20, 1800)           # Left outer wall
Wall(2380, 0, 20, 1800)        # Right outer wall

# Inner maze walls with bigger doors (larger gaps)

# Horizontal walls
Wall(150, 150, 400, 20)
Wall(650, 200, 20, 350)
Wall(670, 550, 20, 350)
Wall(690, 900, 300, 20)
Wall(1200, 600, 20, 500)
Wall(1220, 1100, 600, 20)
Wall(1850, 400, 20, 800)
Wall(1500, 300, 600, 20)

# Vertical walls
Wall(200, 200, 20, 400)        # vertical with big door gap below
Wall(400, 600, 20, 400)
Wall(800, 700, 400, 20)
Wall(1400, 1200, 20, 400)
Wall(1600, 1400, 400, 20)

# Add some door-sized gaps for easy passage
# For example, gaps between vertical walls or shorter walls where needed



# --- Main loop ---
player_dead = False
while True:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
<<<<<<< HEAD
    #players = n.send(players[player.id])        
    
    updategame()
    
    ### remove 10 health from player if z key is pressed for testing
    keys = pygame.key.get_pressed()
=======
            
    ### test ###
        # Manual control for bot1 using arrow keys
    keys = pygame.key.get_pressed()
    bot_direction = pygame.Vector2(0, 0)

    if keys[pygame.K_UP]:    bot_direction.y -= 1
    if keys[pygame.K_DOWN]:  bot_direction.y += 1
    if keys[pygame.K_LEFT]:  bot_direction.x -= 1
    if keys[pygame.K_RIGHT]: bot_direction.x += 1

    if bot_direction.length() > 0:
        bot_direction = bot_direction.normalize()
        bot.angle = math.atan2(bot_direction.y, bot_direction.x)
        move = bot_direction * bot.speed

        # Try move logic (reuse)
        new_pos = bot.pos + move
        bot_rect = pygame.Rect(new_pos.x - 20, new_pos.y - 10, 40, 20)
        if not any(bot_rect.colliderect(wall) for wall in walls):
            bot.pos = new_pos
    ### test ###
    updategame()
    
    ### remove 10 health from player if z key is pressed for testing
>>>>>>> 72482c5fb7ea5c88aadce0d5011910e6257d03ae
    if keys[pygame.K_z]:
        player.health -= 10
    ###
    pygame.display.flip()
