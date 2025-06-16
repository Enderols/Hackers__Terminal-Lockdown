import pygame
import math
import sys
import maps
from network import Network
import tkinter as tk

global username

def submit_username():
    global username  # Make it accessible outside the function
    username = entry.get()  # Store the entered username
    getUserWin.destroy()  # Close the window immediately

#Create username Input Window
getUserWin = tk.Tk()
getUserWin.title("Enter Username")
getUserWin.geometry("300x150")
label = tk.Label(getUserWin, text="Enter your username:")
label.pack(pady=10)
entry = tk.Entry(getUserWin, width=30)
entry.pack(pady=5)
submitButton = tk.Button(getUserWin, text="Submit", command=submit_username)
submitButton.pack(pady=10)
getUserWin.mainloop()

print("Username entered:", username)  # Example usage




# --- Settings ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600#
WORLD_WIDTH, WORLD_HEIGHT = 2400*2, 1800*2  #map size
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
    def __init__(self,pos,id):
        
        self.image_orig = pygame.Surface((40, 20), pygame.SRCALPHA)
        pygame.draw.rect(self.image_orig, (255, 0, 0), (0, 0, 40, 20))
        self.id =id
        
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

class Player:
    def __init__(self, pos, id,name="unknown"):
        self.image_orig = pygame.Surface((40, 20), pygame.SRCALPHA)
        pygame.draw.polygon(self.image_orig, (0, 0, 255), [(0, 0), (40, 10), (0, 20)])
        self.id = id
        self.pos = pygame.Vector2(pos)
        self.angle = 0
        self.speed = 8
        self.health = 100
        self.points = 0
        self.name = name
        self.hit_timer = 0  # Add this line
        players[self.id] = self
        self.hack_cooldown = 0
        self.hack_delay = 60  # 60 frames = 1 second at 60 FPS
        self.overhealth_timer = 0
        self.ammo = 20
        self.shot = False
        self.dead = False  # Track if the player is dead
        self.damagedict = {}  # Dictionary to track damage given to other players
        self.hackedpoints={}
        

        self.shoot_cooldown = 0
        self.shoot_delay = 24  # 24 Frames = 0.4s bei 60 FPS

    def update(self, mouse_world_pos, keys):
        

        forward = pygame.Vector2(math.cos(self.angle), math.sin(self.angle))
        right = pygame.Vector2(-forward.y, forward.x)
        move = pygame.Vector2(0, 0)

        # Decrease hit_timer if active
        if self.hit_timer > 0:
            self.hit_timer -= 1

    def draw(self, surface):
        if self.dead == False:
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
            self.shot = True
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
            for p in players.values():  # Use a copy of the list in case we remove a player
                if p is self:
                    continue
                player_rect = pygame.Rect(p.pos.x - 20, p.pos.y - 10, 40, 20)
                if player_rect.clipline((start.x, start.y), (end.x, end.y)):
                    p.health -= 10

                    self.damagedict[p.id] = p.health

                    p.hit_timer = 15
                    print(f"{p.name} got hit Health: {p.health}")
                    self.points += 5
                    if p.health <= 0:
                        p.die()
                        
                        print(f"{p.name} died!")
                        p.health = 0
                        ###
                    # Only hit one player per shot (optional: remove break if you want multi-hit)
                    break

            # Store the line coordinates for drawing
            global last_shot_coords, show_shot_line, shot_line_timer
            last_shot_coords = (start, end)
            show_shot_line = True
            shot_line_timer = 1  # Only show for 1 frame
    def die(self):
        self.health = 0
        self.dead = True
        if self in players:
            del players[self.id]
            
    

class Client(Player):
    def __init__(self,pos,id,name):
        super().__init__(pos,id,name)
        
    def update(self, mouse_world_pos, keys):
        if self.dead == True:
            return
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
                        self.points += 5
                        self.health += 30
                        self.ammo += 15
                        print(self.hackedpoints)
                        self.hackedpoints[hackpoint.id]=hackpoint.id
                        print(self.hackedpoints)

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
    
    def shoot(self):
        if self.ammo <= 0:
            print("Out of ammo!")
            return
        else:
            print(f"Remaining ammo: {self.ammo}")
            self.ammo -= 1
            self.shot = True
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
            for p in players.values():  # Use a copy of the list in case we remove a player
                if p is self:
                    continue
                player_rect = pygame.Rect(p.pos.x - 20, p.pos.y - 10, 40, 20)
                if player_rect.clipline((start.x, start.y), (end.x, end.y)):   
                    self.damagedict[p.id] = p.health
                    p.hit_timer = 15
                    self.points += 5
                    break

            # Store the line coordinates for drawing
            global last_shot_coords, show_shot_line, shot_line_timer
            last_shot_coords = (start, end)
            show_shot_line = True
            shot_line_timer = 1  # Only show for 1 frame

    def send_data(self):
        data_dict = {
            "pos": self.pos,
            "angle":self.angle,
            "health": self.health,
            "id": self.id,
            "ammo": self.ammo,
            "points": self.points,
            "givendamage": self.damagedict.copy(),
            "shot": self.shot,
            "hackpoints": self.hackedpoints.copy(),
            "name": self.name
            }
        if self.damagedict:
            print(self.damagedict)
        
        self.damagedict.clear()
        self.hackedpoints.clear()
        self.shot = False  # Clear after sending
        return data_dict.copy()
        
    

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
    
    world_surface = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))
    draw_world(world_surface)

    view_rect = camera.get_view_rect(player.pos)
    mouse_screen = pygame.Vector2(pygame.mouse.get_pos())
    mouse_world = mouse_screen / ZOOM + view_rect.topleft

    keys = pygame.key.get_pressed()
    for user in players.values():
        user.update(mouse_world, keys)
        user.draw(world_surface)

    # Draw the main player if not dead (for local player)
    if not player.dead:
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
    
    #health
    # Health bar settings
    bar_width = 200
    bar_height = 24
    bar_x = (SCREEN_WIDTH - bar_width) // 2
    bar_y = SCREEN_HEIGHT - 42

    # Calculate health ratio
    health_ratio = max(player.health, 0) / 100

    # Draw background bar (gray, full width)
    pygame.draw.rect(screen, (80, 80, 80), (bar_x, bar_y, bar_width, bar_height))

    # Draw foreground bar (green, proportional to health)
    pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, int(bar_width * health_ratio), bar_height))

    # Draw health text on top (as before)
    text = font.render(f"Health: {max(player.health, 0)}", True, (0, 0, 0), None)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
    screen.blit(text, text_rect)

    #ammo text
    text_ammo = font.render(f"Ammo: {player.ammo}", True, (0, 0, 0), (0, 255, 0))
    text_ammo_rect = text_ammo.get_rect(center=(SCREEN_WIDTH - 80, SCREEN_HEIGHT - 30))
    screen.blit(text_ammo, text_ammo_rect)

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
        player.dead = True
        if player in players:
            players.remove(player)

    #overhealth system
    if player.health > 100:
        player.overhealth_timer += 1
        if player.overhealth_timer >= 100:  # Wait 2 seconds at 60 FPS
            player.health -= 1  # Decrease overhealth slowly
            if player.health < 100:
                player.health = 100
            player.overhealth_timer = 0  # Reset timer after each decrease
    else:
        player.overhealth_timer = 0  # Reset timer if health <= 100
    
    
        
            

    #if player in players:
        #print(player.pos, player.angle)
        
    data = n.send(player.send_data())  # Send player data to server

    if len([i for i in data if i is not None and i["health"] > 0]) == 1:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((50, 50, 50, 180))  # RGBA: last value is alpha (transparency)
        screen.blit(overlay, (0, 0))
        winner = [i for i in data if i is not None and i["health"] > 0][0]["name"]
        game_over_text = font.render(f"Game ended. {winner} Won the game", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, game_over_rect)

    #move players to the new data
    #print(data)
    for playerdict in data:
        
        if playerdict is None:
            continue
        i = playerdict["id"]
        if playerdict["id"] == player.id:
            continue
        else:
            #print("gegner ausgeführt")
            players[i].pos = pygame.Vector2(playerdict["pos"])
            players[i].angle = playerdict["angle"]
            players[i].ammo = playerdict["ammo"]
            players[i].points = playerdict["points"]
            players[i].name = playerdict["name"]
            if playerdict["health"] <= 0:
                players[i].die()

            if playerdict["shot"]:
                players[i].shoot()

            if playerdict["hackpoints"]:
                for hack_id in playerdict["hackpoints"].values():
                    for hp in hackpoints[:]:  # Copy to avoid modifying while iterating
                        if hp.id == hack_id:
                            hackpoints.remove(hp)
            #winscreen#
    
    
    



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
players = {}



ClientId = n.getId()
print(f"Client ID: {ClientId}")
pygame.display.set_caption(f"Hackers: Terminal Lockdown - Client {ClientId} - {username}")

player = Client((WORLD_WIDTH // 2.5, WORLD_HEIGHT // 2.2), id=ClientId, name=username)
print(f"sending player: {player}")
#players=n.send(player)
print(players)

create_players()




camera = Camera(WORLD_WIDTH, WORLD_HEIGHT, ZOOM)
bullets = []  # Liste aller Bullets



testhack = HackingPoint((WORLD_WIDTH // 2.5, WORLD_HEIGHT // 2.2),1)
testhack2 = HackingPoint((WORLD_WIDTH // 3, WORLD_HEIGHT // 2.5),2)




#walls generieren

usedmap = maps.map3()
for currentwall in usedmap:
    Wall(*currentwall)



# --- Main loop ---

while True:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #players = n.send(players[player.id])        
    
    updategame()
    pygame.display.flip()