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

BLACK = (0, 0, 0)
GREEN = (15, 245, 7)
PINK = (245, 7, 130)
WHITE = (255, 255, 255)
BLUE = (47, 0, 255)
ORANGE = (255, 132, 0)
PURPLE = (208, 0, 255)
RED = (255, 0, 0)


pygame.mixer_music.load(file_path(r"musics_labirint\win1.mp3"))
pygame.mixer_music.set_volume(0.05)
pygame.mixer_music.play(-1)

music_shoot = pygame.mixer.Sound(file_path(r"musics_labirint\shoot1.ogg"))
music_shoot.set_volume(0.25)

background = pygame.image.load(file_path(r"images_labirint\black fon.jpg"))
background = pygame.transform.scale(background, (WIN_WIDTH, WIN_HEIGHT))

bye_fon = pygame.image.load(file_path(r"images_labirint\bye.png"))
bye_fon = pygame.transform.scale(bye_fon, (300, 300))

victory_image = pygame.image.load(r"images_labirint\WINNER FON.png")
victory_image = pygame.transform.scale(victory_image, (WIN_WIDTH, WIN_HEIGHT))

lose_image = pygame.image.load(r"images_labirint\LOSER FON.png")
lose_image = pygame.transform.scale(lose_image, (WIN_WIDTH, WIN_HEIGHT))

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

class Button():
    def __init__(self, x, y, width, height, background_color, action_color, text, text_color, text_x, text_y):
        self.rect = pygame.Rect(x, y, width, height)
        self.background_color = background_color
        self.action_color = action_color
        self.color = background_color
        shrift = pygame.font.SysFont("Helvetica", 55)
        self.text = shrift.render(text, True, text_color)
        self.text_x = text_x
        self.text_y = text_y

    def show(self):
        pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.text, (self.rect.x + self.text_x, self.rect.y + self.text_y))

class Arrow():
    def __init__(self, x, y, width, height, background_color, action_color, text, text_color, text_x, text_y):
        self.rect = pygame.Rect(x, y, width, height)
        self.background_color = background_color
        self.action_color = action_color
        self.color = background_color
        shrift = pygame.font.SysFont("Comic sans", 25)
        self.text = shrift.render(text, True, text_color)
        self.text_x = text_x
        self.text_y = text_y

    def show(self):
        pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.text, (self.rect.x + self.text_x, self.rect.y + self.text_y))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(file_path(image))
        self.image = pygame.transform.scale(self.image, (width, height))

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, x, y, width, height, image, speed_x, speed_y):
        super().__init__(x, y, width, height, image)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.direction = "left"
        self.image_l = self.image
        self.image_r = pygame.transform.flip(self.image, True, False)

    def shoot(self):
        if self.direction == "right":
            bullet = Bullet(self.rect.right, self.rect.centery, 3, 3, r"images_labirint\bullet.png", 7)
        elif self.direction == "left":
            bullet = Bullet(self.rect.left - 3, self.rect.centery, 3, 3, r"images_labirint\bullet.png", -7)
            bullet.image = pygame.transform.flip(bullet.image, True, False)

        bullets.add(bullet)

    def update(self):
        if self.speed_x < 0 and self.rect.left > 0 or self.speed_x > 0 and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed_x
        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_x > 0:
            for wall in walls_touched:
                self.rect.right = min(self.rect.right, wall.rect.left)
        if self.speed_x < 0:
            for wall in walls_touched:
                self.rect.left = max(self.rect.left, wall.rect.right)

        if self.speed_y < 0 and self.rect.top > 0 or self.speed_y > 0 and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed_y
        
        walls_touched = pygame.sprite. spritecollide(self, walls, False)
        if self.speed_y < 0:
            for wall in walls_touched:
                self.rect.top = max(self.rect.top, wall.rect.bottom)
        if self.speed_y > 0:
            for wall in walls_touched:
                self.rect.bottom = min(self.rect.bottom, wall.rect.top)

class Bullet(GameSprite):
    def __init__(self, x, y, width, height, image, speed_bullet):
        super().__init__(x, y, width, height, image)
        self.speed_bullet = speed_bullet

    def update(self):
        self.rect.x += self.speed_bullet
        if self.rect.left >= WIN_WIDTH or self.rect.right <= 0:
            self.kill()





class Enemy(GameSprite):
    def __init__(self, x, y, width, height, image, direction, min_XYZ, max_XYZ, speed):
        super().__init__(x, y, width, height, image)
        self.direction = direction
        self.min_XYZ = min_XYZ
        self.max_XYZ = max_XYZ
        self.speed = speed

        if self.direction == "right":
            self.image_r = self.image
            self.image_l = pygame.transform.flip(self.image, True, False)
        
        elif self.direction == "left":
            self.image_l = self.image
            self.image_r = pygame.transform.flip(self.image, True, False)

    def update(self):
        if self.direction == "left" or self.direction == "right":
            if self.direction == "left":
                self.rect.x -= self.speed
            
            elif self.direction == "right":
                self.rect.x += self.speed

            if self.rect.right >= self.max_XYZ:
                self.direction = "left"
                self.image = self.image_l

            if self.rect.left <= self.min_XYZ:
                self.direction = "right"
                self.image = self.image_r
            
        elif self.direction == "up" or self.direction == "down":
            if self.direction == "up":
                self.rect.y -= self.speed
            
            elif self.direction == "down":
                self.rect.y += self.speed
            
            if self.rect.top <= self.min_XYZ:
                self.direction = "down"

            if self.rect.bottom >= self.max_XYZ:
                self.direction = "up"



player = Player(15, 15, 15, 15, r"images_labirint\player.png", 0, 0)
finish = GameSprite(555, 555, 15, 15, r"images_labirint\finish.png")

enemies = pygame.sprite.Group()

enemy1 = Enemy(12, 215, 15, 15, r"images_labirint\enemy.png", "down", 215, 505, 3)
enemy2 = Enemy(95, 12, 15, 15, r"images_labirint\enemy.png", "right", 95, 305, 3)
enemy3 = Enemy(500, 485, 15, 15, r"images_labirint\enemy.png", "right", 485, 555, 3)
enemies.add(enemy1)
enemies.add(enemy2)
enemies.add(enemy3)

bullets = pygame.sprite.Group()

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

btn_start = Button(200, 200, 200, 100, GREEN, BLUE, "START", PINK, 30, 20)
btn_settings = Button(100, 325, 400, 100, GREEN, BLUE, "SETTINGS", PINK, 85, 20)
btn_exit = Button(200, 450, 200, 100, GREEN, BLUE, "EXIT", PINK, 50, 20)
game_name = pygame.font.SysFont("Arial", 105, 1).render("POTOM", True, WHITE)

btn_bye = Button(200, 475, 200, 100, GREEN, BLUE, "EXIT", PINK, 50, 20)
btn_back = Button(5, 5, 127, 65, GREEN, BLUE, "BACK", PINK, 1, 1)
btn_start_settings = Button(225, 500, 150, 65, GREEN, BLUE, "START", PINK, 1, 1)
btn_arrow_right = Arrow(450, 400, 48, 18, ORANGE, BLUE, "NEXT", RED, 1, 1)
btn_arrow_left = Arrow(102, 400, 47, 18, ORANGE, BLUE, "LAST", RED, 1, 1)

btn_arrow_plus_fon1 = Arrow(550, 25, 13, 22, ORANGE, BLUE, "+", RED, 1, 1)
btn_arrow_plus_win1 = Arrow(550, 75, 13, 22, ORANGE, BLUE, "+", RED, 1, 1)
btn_arrow_plus_lose1 = Arrow(550, 125, 13, 22, ORANGE, BLUE, "+", RED, 1, 1)

btn_arrow_minus_fon1 = Arrow(492, 25, 8, 22, ORANGE, BLUE, "-", RED, 1, 1)
btn_arrow_minus_win1 = Arrow(492, 75, 8, 22, ORANGE, BLUE, "-", RED, 1, 1)
btn_arrow_minus_lose1 = Arrow(492, 125, 8, 22, ORANGE, BLUE, "-", RED, 1, 1)

txt_volume_fon1 = pygame.font.SysFont("Arial", 25, 1).render("VOLUME FON MUSIC", True, WHITE)
txt_volume_win1 = pygame.font.SysFont("Arial", 25, 1).render("VOLUME WIN MUSIC", True, WHITE)
txt_volume_lose1 = pygame.font.SysFont("Arial", 25, 1).render("VOLUME LOSE MUSIC", True, WHITE)

volume_fon1 = 0.25
volume_win1 = 0.10
volume_lose1 = 0.10

txt_volume_number_fon1 = pygame.font.SysFont("Arial", 25, 1).render(str(volume_fon1), True, WHITE)
txt_volume_number_win1 = pygame.font.SysFont("Arial", 25, 1).render(str(volume_win1), True, WHITE)
txt_volume_number_lose1 = pygame.font.SysFont("Arial", 25, 1).render(str(volume_lose1), True, WHITE)

level = 0

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if level == 1:
            pygame.mixer_music.stop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.speed_x = -2.5
                    player.direction = "left"
                    player.image_l = player.image_l
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.speed_x = 2.5
                    player.direction = "right"
                    player.image_l = player.image_l
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.speed_y = 2.5
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.speed_y = -2.5
                if event.key == pygame.K_SPACE:
                    player.shoot()
                    music_shoot.play()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.speed_x = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.speed_x = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.speed_y = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.speed_y = 0

        elif level == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if btn_start.rect.collidepoint(x, y):
                    level = 1
                    pygame.mixer_music.load(file_path(r"musics_labirint\fon1.mp3"))
                    pygame.mixer_music.set_volume(0.25)
                    pygame.mixer_music.play(-1)

                elif btn_settings.rect.collidepoint(x, y):
                    level = 2

                elif btn_exit.rect.collidepoint(x, y):
                    level = "bye"
                    pygame.mixer_music.stop()
                    pygame.mixer_music.load(file_path(r"musics_labirint\bye1.mp3"))
                    pygame.mixer_music.set_volume(1)
                    pygame.mixer_music.play(-1)
            
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if btn_start.rect.collidepoint(x, y):
                    btn_start.color = btn_start.action_color
                
                elif btn_settings.rect.collidepoint(x, y):
                    btn_settings.color = btn_settings.action_color

                elif btn_exit.rect.collidepoint(x, y):
                    btn_exit.color = btn_exit.action_color

                else:
                    btn_start.color = btn_start.background_color
                    btn_settings.color = btn_settings.background_color
                    btn_exit.color = btn_exit.background_color
        
        elif level == 2:
            pygame.mixer_music.stop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if btn_back.rect.collidepoint(x, y):
                    level = 0
                
                elif btn_start_settings.rect.collidepoint(x, y):
                    level = 1
                
                elif btn_arrow_plus_fon1.rect.collidepoint(x, y):
                    volume_fon1 += 0.05
                    pygame.mixer_music.set_volume(volume_fon1)
            
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if btn_back.rect.collidepoint(x, y):
                    btn_back.color = btn_back.action_color

                elif btn_start_settings.rect.collidepoint(x, y):
                    btn_start_settings.color = btn_start_settings.action_color
                    
                elif btn_arrow_right.rect.collidepoint(x, y):
                    btn_arrow_right.color = btn_arrow_right.action_color

                elif btn_arrow_left.rect.collidepoint(x, y):
                    btn_arrow_left.color = btn_arrow_left.action_color
                
                elif btn_arrow_plus_fon1.rect.collidepoint(x, y):
                    btn_arrow_plus_fon1.color = btn_arrow_plus_fon1.action_color

                elif btn_arrow_plus_win1.rect.collidepoint(x, y):
                    btn_arrow_plus_win1.color = btn_arrow_plus_win1.action_color

                elif btn_arrow_plus_lose1.rect.collidepoint(x, y):
                    btn_arrow_plus_lose1.color = btn_arrow_plus_lose1.action_color

                elif btn_arrow_minus_fon1.rect.collidepoint(x, y):
                    btn_arrow_minus_fon1.color = btn_arrow_minus_fon1.action_color

                elif btn_arrow_minus_win1.rect.collidepoint(x, y):
                    btn_arrow_minus_win1.color = btn_arrow_minus_win1.action_color

                elif btn_arrow_minus_lose1.rect.collidepoint(x, y):
                    btn_arrow_minus_lose1.color = btn_arrow_minus_lose1.action_color

                else:
                    btn_back.color = btn_back.background_color
                    btn_start_settings.color = btn_start_settings.background_color
                    btn_arrow_right.color = btn_arrow_right.background_color
                    btn_arrow_left.color = btn_arrow_left.background_color
                    btn_arrow_plus_fon1.color = btn_arrow_plus_fon1.background_color
                    btn_arrow_plus_win1.color = btn_arrow_plus_win1.background_color
                    btn_arrow_plus_lose1.color = btn_arrow_plus_lose1.background_color
                    btn_arrow_minus_fon1.color = btn_arrow_minus_fon1.background_color
                    btn_arrow_minus_win1.color = btn_arrow_minus_win1.background_color
                    btn_arrow_minus_lose1.color = btn_arrow_minus_lose1.background_color

        elif level == "bye":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if btn_bye.rect.collidepoint(x, y):
                    game = False

                elif btn_back.rect.collidepoint(x, y):
                    level = 0
            
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if btn_bye.rect.collidepoint(x, y):
                    btn_bye.color = btn_bye.action_color
                
                elif btn_back.rect.collidepoint(x, y):
                    btn_back.color = btn_back.action_color
                
                else:
                    btn_bye.color = btn_bye.background_color
                    btn_back.color = btn_back.background_color


    if level == 1:
        window.blit(background, (0, 0))
        walls.draw(window)
        player.show()
        player.update()     
        enemies.draw(window)
        enemies.update()
        finish.show()
        bullets.draw(window)
        bullets.update()

        if pygame.sprite.collide_rect(player, finish):
            level = 10
            pygame.mixer_music.stop()
            pygame.mixer_music.load(file_path(r"musics_labirint\win1.mp3"))
            pygame.mixer_music.set_volume(0.10)
            pygame.mixer_music.play(-1)
    
        if pygame.sprite.spritecollide(player, enemies, False):
            level = 11
            pygame.mixer_music.stop()
            pygame.mixer_music.load(file_path(r"musics_labirint\lose1.mp3"))
            pygame.mixer_music.set_volume(0.10)
            pygame.mixer_music.play(1)
        
        pygame.sprite.groupcollide(bullets, walls, True, False)
        pygame.sprite.groupcollide(bullets, enemies, True, True)

    elif level == 0:
        window.fill(BLACK)
        btn_start.show()
        btn_settings.show()
        btn_exit.show()
        window.blit(game_name, (150, 40))

    elif level == 2:
        window.fill(BLACK)
        btn_back.show()
        btn_start_settings.show()
        btn_arrow_right.show()
        btn_arrow_left.show()
        btn_arrow_plus_fon1.show()
        btn_arrow_plus_win1.show()
        btn_arrow_plus_lose1.show()
        btn_arrow_minus_fon1.show()
        btn_arrow_minus_win1.show()
        btn_arrow_minus_lose1.show()
        window.blit(txt_volume_fon1, (250, 21))
        window.blit(txt_volume_win1, (251, 71))
        window.blit(txt_volume_lose1, (243, 121))
        window.blit(txt_volume_number_fon1, (505, 21))
        window.blit(txt_volume_number_win1, (505, 71))
        window.blit(txt_volume_number_lose1, (505, 121))
        

    elif level == "bye":
        window.fill(BLACK)
        btn_bye.show()
        window.blit(bye_fon, (150, 150))
        btn_back.show()

    elif level == 10:
        window.blit(victory_image, (0, 0))

    elif level == 11:
        window.blit(lose_image, (0, 0))

    clock.tick(FPS)
    pygame.display.update()




