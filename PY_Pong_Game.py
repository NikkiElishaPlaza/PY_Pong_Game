import pygame

WIDTH, HEIGHT, = 700, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG GAME")


def main():
    run = True

    while run:
        for event in pygame.event.get():
            