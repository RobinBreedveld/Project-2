import pygame
from pygame.locals import*
game_background = pygame.image.load('game_background.bmp')
menu_background = pygame.image.load('menu_background.bmp')
#boot2 = pygame.image.load('boot2.bmp')
#boot3 = pygame.image.load('boot3.bmp')
#boot4 = pygame.image.load('boot4.bmp')
h = 767
w = round((h/9) * 16)
background_blue = (25,25,112)
white = (255,255,255)
black = (0,0,0)
screen = pygame.display.set_mode((w, h))
def block(x, y, w, h, color):
    pygame.draw.rect(screen, color, [x, y, w, h])
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False
class Menu:
    def buttons(self):
        self.startbutton = block(1000, 150, 200, 70, white)
        self.loadbutton = block(1000, 250, 200, 70, white)
        self.highscoresbutton = block(1000, 350, 200, 70, white)
        self.optionsbutton = block(1000, 450, 200, 70, white)
        self.helpbutton = block(1000, 550, 200, 70, white)
        self.exitbutton = block(1000, 650, 200, 70, white)
    def draw(self):
        while not(process_events()):
            screen.fill((background_blue))
            screen.blit(menu_background, (0,0))
            self.buttons()
            pygame.display.flip()
class Battleport:
    def __init__(self):
        screen.fill(background_blue)
    def buttons(self):
        self.button1 = block(1100, 26, 80, 80, (white))
        self.button2 = block(1190, 26, 80, 80, (white))
        self.button3 = block(1280, 26, 80, 80, (white))
    def draw(self):
        while not(process_events()):
            screen.fill((background_blue))
            screen.blit(game_background, (0,0))
            self.buttons()
            pygame.display.flip()
running = Battleport()
running.draw()