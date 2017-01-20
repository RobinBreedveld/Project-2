import pygame
from pygame.locals import*
game_background = pygame.image.load('game_background.bmp')
#menu_background = pygame.image.load('menu_background.bmp')
#boot2 = pygame.image.load('boot2.bmp')
#boot3 = pygame.image.load('boot3.bmp')
#boot4 = pygame.image.load('boot4.bmp')
pygame.font.get_fonts()
pygame.font.init()
h = 767
w = round((h/9) * 16)
background_blue = (25,25,112)
white = (255,255,255)
black = (0,0,0)
grey = (200,200,200)
screen = pygame.display.set_mode((w, h))
def block(x, y, w, h, color):
    pygame.draw.rect(screen, color, [x, y, w, h])
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False
def button(msg, x, y, w, h, color_active, color_inactive, action=None):
     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if (x + w > mouse[0] > x) and (y + h > mouse[1] > y):
         block(x, y, w, h, color_active)
         if click[0] == 1 and action != None:
             if action == "start":
                 running = Battleport()
     else:
         block(x, y, w, h, color_inactive)
     smallText = pygame.font.Font("freesansbold.ttf", 30)
     textSurf, textRect = text_object(msg, smallText)
     textRect.center = ((x + (w/2)), (y + (h/2)))
     screen.blit(textSurf, textRect)
def text_object(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
class Battleport:
    def __init__(self):
        screen.fill(background_blue)
    def buttons(self):
        button("?", 1100, 26, 80, 80, grey, white)
        button("||", 1190, 26, 80, 80, grey, white)
        button("X", 1280, 26, 80, 80, grey, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(game_background, (0,0))
        self.buttons()
        pygame.display.flip()
running = Battleport()
while not(process_events()):
    running.draw()