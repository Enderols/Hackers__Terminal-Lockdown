import pygame
import math
import sys
import _thread 

# --- Settings ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
ZOOM = 1
# --- pygame setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hackers: Terminal Lockdown")
clock = pygame.time.Clock()

# --- Game objects ---
# Walls class
walls = []
class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        walls.append(self.rect)

WORLD_WIDTH, WORLD_HEIGHT = 2400, 1800  # Bigger world now

# Hacking points
hackpoints = []
class HackingPoint:
    def __init__(self,pos):
        self.image_orig = pygame.Surface((40, 20), pygame.SRCALPHA)
        pygame.draw.rect(self.image_orig, (255, 0, 0), (0, 0, 40, 20))
        self.pos = pygame.Vector2(pos)
        self.health = 100
        self.angle = 0
        self.speed = 4
        hackpoints.append(self)






#Player class
players = []
class Player:
    def __init__(self, pos):
        self.image_orig = pygame.Surface((40, 20), pygame.SRCALPHA)
        pygame.draw.polygon(self.image_orig, (0, 0, 255), [(0, 0), (40, 10), (0, 20)])
        self.pos = pygame.Vector2(pos)
        self.angle = 0
        self.speed = 4
        self.health = 100
        players.append(self)

        self.shoot_cooldown = 0
        self.shoot_delay = 24  # 24 Frames = 0.4s bei 60 FPS

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
        if keys[pygame.K_h]:
            
            for hackpoint in hackpoints:
                if self.pos.distance_to(hackpoint.pos) < 100:
                    hackpoint.health -= 10
                    print(f"Hacking Point Health: {hackpoint.health}")
                    #wait for 1 second to simulate hacking
                    pygame.time.delay(1000)  # 1 second delay
                    
                    if hackpoint.health <= 0:
                        print("Hacking Point destroyed!")
                        hackpoints.remove(hackpoint)
                        #change the color of the hacking point to indicate destruction
                        hackpoint.image_orig.fill((0, 0, 0, 0))



        

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
        bullet = Bullet(self.pos, self.angle)
        bullets.append(bullet)  # Bullet zur globalen Liste hinzufügen

# Bullet class
class Bullet:
    def __init__(self, pos, angle):
        self.pos = pygame.Vector2(pos)
        self.angle = angle
        self.speed = 50  # Geschwindigkeit der Kugel
        self.radius = 5
        self.rect = pygame.Rect(self.pos.x - self.radius, self.pos.y - self.radius, self.radius*2, self.radius*2)

    def update(self):
        # Bullet bewegt sich
        velocity = pygame.Vector2(math.cos(self.angle), math.sin(self.angle)) * self.speed
        self.pos += velocity
        self.rect.topleft = (self.pos.x - self.radius, self.pos.y - self.radius)

        # Prüfe Kollision mit Wänden
        for wall in walls:
            if self.rect.colliderect(wall):
                return True  # Kollision -> Bullet soll entfernt werden
        # OWenn Bullet außerhalb Welt ist, auch entfernen
        # test if bullet hits player
        for Player in [player]:
            if self.rect.colliderect(pygame.Rect(Player.pos.x - 20, Player.pos.y - 10, 40, 20)):
                Player.health -= 10
                return True #Bullet gets removed

        if not pygame.Rect(0, 0, WORLD_WIDTH, WORLD_HEIGHT).colliderect(self.rect):
            return True

        return False  # Keine Kollision

    def draw(self, surface):
        pygame.draw.circle(surface, (0, 0, 0), (int(self.pos.x), int(self.pos.y)), self.radius)

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

# Function to draw the world
def draw_world(surface):
    surface.fill((255, 255, 255))
    for wall in walls:
        pygame.draw.rect(surface, (0, 0, 0), wall)

# Setup
player = Player((WORLD_WIDTH // 2.5, WORLD_HEIGHT // 2.2))
camera = Camera(WORLD_WIDTH, WORLD_HEIGHT, ZOOM)
bullets = []  # Liste aller Bullets

testhack = HackingPoint((WORLD_WIDTH // 2.5, WORLD_HEIGHT // 2.2))


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
while True:
    
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    world_surface = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))
    draw_world(world_surface)

    view_rect = camera.get_view_rect(player.pos)
    mouse_screen = pygame.Vector2(pygame.mouse.get_pos())
    mouse_world = mouse_screen / ZOOM + view_rect.topleft

    keys = pygame.key.get_pressed()
    player.update(mouse_world, keys)
    player.draw(world_surface)
    
    
    # Bullets updaten und zeichnen
    for bullet in bullets[:]:
        collided = bullet.update()
        if collided:
            bullets.remove(bullet)
        else:
            bullet.draw(world_surface)
    # Draw the hacking point
    testhack.image = pygame.transform.rotate(testhack.image_orig, -math.degrees(testhack.angle))
    testhack.rect = testhack.image.get_rect(center=testhack.pos)
    world_surface.blit(testhack.image, testhack.rect.topleft)
    screen.blit(camera.apply(world_surface, view_rect), (0, 0))
    pygame.display.flip()
    
    
#test haha
