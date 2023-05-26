import pygame
import os
pygame.init()

def file_path(filename):
    folder = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder, filename)
    return path

WIN_WIDTH = 1000
WIN_HEIGHT = 600
FPS = 60

background = pygame.image.load(file_path(r"images_labirint\black fon.jpg"))
background = pygame.transform.scale(background, (WIN_WIDTH, WIN_HEIGHT))

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

level = 1

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if level == 1:
        window.blit(background, (0, 0))

    clock.tick(FPS)
    pygame.display.update()





