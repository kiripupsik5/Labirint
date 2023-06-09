import pygame
import os
pygame.init()

def file_path(filename):
    folder = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder, filename)
    return path

WIN_WIDTH = 600
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

player = GameSprite(15, 15, 50, 25, r"images_labirint\player.png")
enemy1 = GameSprite(25, 25, 50, 25, r"images_labirint\enemy.png")
finish = GameSprite(25, 25, 50, 25, r"images_labirint\finish.png")

#название стен_расположение стен v-vertical,  h-horizontal_номер рядка в котором расположенны стены_номер редактируемой стены
walls = pygame.sprite.Group()
wall_v_1_1 = GameSprite(560, 0, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_1_1)
wall_v_1_2 = GameSprite(480, 0, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_1_2)
wall_v_1_3 = GameSprite(400, 0, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_1_3)
wall_v_1_4 = GameSprite(320, 0, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_1_4)

wall_h_1_1 = GameSprite(0, 40, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_1_1)
wall_h_1_2 = GameSprite(80, 40, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_1_2)
wall_h_1_3 = GameSprite(160, 40, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_1_3)
wall_h_1_4 = GameSprite(240, 40, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_1_4)


wall_v_2_1 = GameSprite(40, 40, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_2_1)
wall_v_2_2 = GameSprite(120, 40, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_2_2)
wall_v_2_3 = GameSprite(200, 40, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_2_3)
wall_v_2_4 = GameSprite(280, 40, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_2_4)
wall_v_2_5 = GameSprite(360, 40, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_2_5)
wall_v_2_6 = GameSprite(440, 40, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_2_6)
wall_v_2_7 = GameSprite(520, 40, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_2_7)

wall_h_2_1 = GameSprite(40, 80, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_2_1)
wall_h_2_2 = GameSprite(120, 80, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_2_2)
wall_h_2_3 = GameSprite(200, 80, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_2_3)
wall_h_2_4 = GameSprite(280, 80, 180, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_2_4)
wall_h_2_5 = GameSprite(500, 80, 100, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_2_5)


wall_v_3_1 = GameSprite(80, 80, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_3_1)
wall_v_3_2 = GameSprite(160, 80, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_3_2)
wall_v_3_3 = GameSprite(240, 80, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_3_3)
wall_v_3_4 = GameSprite(360, 80, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_3_4)
wall_v_3_5 = GameSprite(520, 80, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_3_5)

wall_h_3_1 = GameSprite(0, 120, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_3_1)
wall_h_3_2 = GameSprite(80, 120, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_3_2)
wall_h_3_3 = GameSprite(160, 120, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_3_3)
wall_h_3_4 = GameSprite(240, 120, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_3_4)
wall_h_3_5 = GameSprite(320, 120, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_3_5)
wall_h_3_6 = GameSprite(440, 120, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_3_6)
wall_h_3_7 = GameSprite(520, 120, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_3_7)


wall_v_4_1 = GameSprite(160, 120, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_4_1)
wall_v_4_2 = GameSprite(240, 120, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_4_2)
wall_v_4_3 = GameSprite(320, 120, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_4_3)
wall_v_4_4 = GameSprite(400, 120, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_4_4)
wall_v_4_5 = GameSprite(480, 120, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_4_5)
wall_v_4_6 = GameSprite(560, 120, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_4_6)

wall_h_4_1 = GameSprite(40, 160, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_4_1)
wall_h_4_2 = GameSprite(120, 160, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_4_2)
wall_h_4_3 = GameSprite(200, 160, 60, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_4_3)
wall_h_4_4 = GameSprite(300, 160, 25, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_4_4)
wall_h_4_5 = GameSprite(360, 160, 80, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_4_5)
wall_h_4_6 = GameSprite(480, 160, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_4_6)


wall_v_5_1 = GameSprite(80, 160, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_5_1)
wall_v_5_2 = GameSprite(160, 160, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_5_2)
wall_v_5_3 = GameSprite(240, 160, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_5_3)
wall_v_5_4 = GameSprite(360, 160, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_5_4)
wall_v_5_5 = GameSprite(440, 160, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_5_5)
wall_v_5_6 = GameSprite(520, 160, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_5_6)

wall_h_5_1 = GameSprite(0, 200, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_5_1)
wall_h_5_2 = GameSprite(160, 200, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_5_2)
wall_h_5_3 = GameSprite(320, 200, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_5_3)
wall_h_5_4 = GameSprite(440, 200, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_5_4)
wall_h_5_5 = GameSprite(520, 200, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_5_5)


wall_v_6_1 = GameSprite(80, 200, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_6_1)
wall_v_6_2 = GameSprite(120, 200, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_6_2)
wall_v_6_3 = GameSprite(280, 200, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_6_3)
wall_v_6_4 = GameSprite(400, 200, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_6_4)
wall_v_6_5 = GameSprite(440, 200, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_6_5)
wall_v_6_6 = GameSprite(520, 200, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_6_6)

wall_h_6_1 = GameSprite(40, 240, 120, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_6_1)
wall_h_6_2 = GameSprite(200, 240, 120, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_6_2)
wall_h_6_3 = GameSprite(360, 240, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_6_3)
wall_h_6_4 = GameSprite(480, 240, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_6_4)


wall_v_7_1 = GameSprite(40, 240, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_7_1)
wall_v_7_2 = GameSprite(120, 240, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_7_2)
wall_v_7_3 = GameSprite(200, 240, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_7_3)
wall_v_7_4 = GameSprite(280, 240, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_7_4)
wall_v_7_5 = GameSprite(320, 240, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_7_5)
wall_v_7_6 = GameSprite(400, 240, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_7_6)
wall_v_7_7 = GameSprite(480, 240, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_7_7)
wall_v_7_8 = GameSprite(560, 240, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_7_8)

wall_h_7_1 = GameSprite(320, 280, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_7_1)
wall_h_7_2 = GameSprite(440, 280, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_7_2)
wall_h_7_3 = GameSprite(520, 280, 80, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_7_3)


wall_v_8_1 = GameSprite(80, 280, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_8_1)
wall_v_8_2 = GameSprite(160, 280, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_8_2)
wall_v_8_3 = GameSprite(240, 280, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_8_3)
wall_v_8_4 = GameSprite(320, 280, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_8_4)
wall_v_8_5 = GameSprite(400, 280, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_8_5)
wall_v_8_6 = GameSprite(520, 280, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_8_6)

wall_h_8_1 = GameSprite(40, 320, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_8_1)
wall_h_8_2 = GameSprite(160, 320, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_8_2)
wall_h_8_3 = GameSprite(240, 320, 85, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_8_3)
wall_h_8_4 = GameSprite(360, 320, 120, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_8_4)


wall_v_9_1 = GameSprite(40, 320, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_9_1)
wall_v_9_2 = GameSprite(120, 320, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_9_2)
wall_v_9_3 = GameSprite(320, 320, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_9_3)
wall_v_9_4 = GameSprite(400, 320, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_9_4)
wall_v_9_5 = GameSprite(480, 320, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_9_5)
wall_v_9_6 = GameSprite(560, 320, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_9_6)

wall_h_9_1 = GameSprite(80, 360, 200, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_9_1)
wall_h_9_2 = GameSprite(320, 360, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_9_2)
wall_h_9_3 = GameSprite(520, 360, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_9_3)



wall_v_10_1 = GameSprite(40, 360, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_10_1)
wall_v_10_2 = GameSprite(160, 360, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_10_2)
wall_v_10_3 = GameSprite(240, 360, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_10_3)
wall_v_10_4 = GameSprite(320, 360, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_10_4)
wall_v_10_5 = GameSprite(360, 360, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_10_5)
wall_v_10_6 = GameSprite(440, 360, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_10_6)
wall_v_10_7 = GameSprite(520, 360, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_10_7)

wall_h_10_1 = GameSprite(40, 400, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_10_1)
wall_h_10_2 = GameSprite(400, 400, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_10_2)
wall_h_10_3 = GameSprite(480, 400, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_10_3)
wall_h_10_4 = GameSprite(560, 400, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_10_4)


wall_v_11_1 = GameSprite(40, 400, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_11_1)
wall_v_11_2 = GameSprite(120, 400, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_11_2)
wall_v_11_3 = GameSprite(200, 400, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_11_3)
wall_v_11_4 = GameSprite(280, 400, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_11_4)
wall_v_11_5 = GameSprite(360, 400, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_11_5)
wall_v_11_6 = GameSprite(440, 400, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_11_6)
wall_v_11_7 = GameSprite(520, 400, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_11_7)

wall_h_11_1 = GameSprite(80, 440, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_11_1)
wall_h_11_2 = GameSprite(160, 440, 240, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_11_2)
wall_h_11_3 = GameSprite(480, 440, 80, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_11_3)


wall_v_12_1 = GameSprite(120, 440, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_12_1)
wall_v_12_2 = GameSprite(200, 440, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_12_2)
wall_v_12_3 = GameSprite(440, 440, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_12_3)
wall_v_12_4 = GameSprite(520, 440, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_12_4)

wall_h_12_1 = GameSprite(40, 480, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_12_1)
wall_h_12_2 = GameSprite(120, 480, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_12_2)
wall_h_12_3 = GameSprite(280, 480, 165, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_12_3)


wall_v_13_1 = GameSprite(40, 480, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_13_1)
wall_v_13_2 = GameSprite(120, 480, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_13_2)
wall_v_13_3 = GameSprite(160, 480, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_13_3)
wall_v_13_4 = GameSprite(240, 480, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_13_4)
wall_v_13_5 = GameSprite(320, 480, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_13_5)
wall_v_13_6 = GameSprite(400, 480, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_13_6)
wall_v_13_7 = GameSprite(480, 480, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_13_7)
wall_v_13_8 = GameSprite(560, 480, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_13_8)

wall_h_13_1 = GameSprite(0, 520, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_13_1)
wall_h_13_2 = GameSprite(80, 520, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_13_2)
wall_h_13_3 = GameSprite(160, 520, 120, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_13_3)
wall_h_13_4 = GameSprite(440, 520, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_13_4)


wall_v_14_1 = GameSprite(80, 520, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_14_1)
wall_v_14_2 = GameSprite(200, 520, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_14_2)
wall_v_14_3 = GameSprite(360, 520, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_14_3)
wall_v_14_4 = GameSprite(440, 520, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_14_4)
wall_v_14_5 = GameSprite(520, 520, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_14_5)


wall_h_14_1 = GameSprite(40, 560, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_14_1)
wall_h_14_2 = GameSprite(120, 560, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_14_2)
wall_h_14_3 = GameSprite(280, 560, 120, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_14_3)
wall_h_14_4 = GameSprite(480, 560, 45, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_14_4)
wall_h_14_5 = GameSprite(560, 560, 40, 5, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_h_14_5)


wall_v_15_1 = GameSprite(160, 560, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_15_1)
wall_v_15_2 = GameSprite(240, 560, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_15_2)
wall_v_15_3 = GameSprite(440, 560, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_15_3)
wall_v_15_4 = GameSprite(520, 560, 5, 40, r"images_labirint\whiteFon walls.jpg")
walls.add(wall_v_15_4)

level = 1

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if level == 1:
        window.blit(background, (0, 0))
        walls.draw(window)
        player.show()
        enemy1.show()
        finish.show()

    clock.tick(FPS)
    pygame.display.update()





