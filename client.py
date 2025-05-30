import pygame
import pickle
from network import Network
from player import Player




width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")






def redraw_window(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    
    p = n.getP()
    
    while run:
        clock.tick(60)
        p2 = n.send(p)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        p.move()
        redraw_window(win, p, p2)
        
main()