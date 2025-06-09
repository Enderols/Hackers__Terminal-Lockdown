import pygame
import pickle
from network import Network
from player import Player




width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")



def redraw_window(win, players):
    win.fill((255, 255, 255))
    for player in players:
        if player is not None:
            player.draw(win)
        else:
            continue

    pygame.display.update()


def main():
    players = []
    run = True
    clock = pygame.time.Clock()
    n = Network()
    
    players.append(n.getPlayer())
    playerId = players[0].id
    pygame.display.set_caption(f"Client {playerId}")

    players = n.send(players[0])
    
    while run:
        clock.tick(60)
        print("Players : ", len(players))
        players = n.send(players[playerId])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        mouse_pos = pygame.mouse.get_pos()
        players[playerId].move(mouse_pos)
        redraw_window(win, players)
        
main()