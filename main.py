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

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(file_path(image))
        self.image = pygame.transform.scale(self.image, (width, height))

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

walls = pygame.sprite.Group()
wall1 = GameSprite(100, 100, 5, 300, r"images_labirint\whiteFon walls.jpg")
walls.add(wall1)
wall2 = GameSprite(150, 150, 25, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall2)

level = 1

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if level == 1:
        window.blit(background, (0, 0))
        walls.draw(window)

    clock.tick(FPS)
    pygame.display.update()





