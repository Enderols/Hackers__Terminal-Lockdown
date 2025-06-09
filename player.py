import pygame
import math

class Player:
    def __init__(self, id, pos, color, width=40, height=20):
        self.id = id
        self.pos = pygame.Vector2(pos)  # [x, y]
        self.width = width
        self.height = height
        self.color = color
        self.vel = 3
        self.angle = 0  # Radians

    def move(self, mouse_pos):
        # Update angle to face mouse
        direction = pygame.Vector2(mouse_pos) - self.pos
        if direction.length() > 0:
            self.angle = math.atan2(direction.y, direction.x)

        # Move relative to facing direction
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(math.cos(self.angle), math.sin(self.angle))
        right = pygame.Vector2(-forward.y, forward.x)
        move = pygame.Vector2(0, 0)
        if keys[pygame.K_w]:
            move += forward
        if keys[pygame.K_s]:
            move -= forward
        if keys[pygame.K_a]:
            move -= right
        if keys[pygame.K_d]:
            move += right
        if move.length() > 0:
            move = move.normalize() * self.vel
            self.pos += move


    def draw(self, win):
        # Triangle points (relative to center, pointing right)
        points = [
            (self.width // 2, 0),  # tip
            (-self.width // 2, -self.height // 2),  # back top
            (-self.width // 2, self.height // 2),   # back bottom
        ]
        # Rotate points
        rotated_points = []
        for px, py in points:
            rx = px * math.cos(self.angle) - py * math.sin(self.angle)
            ry = px * math.sin(self.angle) + py * math.cos(self.angle)
            rotated_points.append((self.pos.x + rx, self.pos.y + ry))
        pygame.draw.polygon(win, self.color, rotated_points)

