import pygame
from pygame.locals import*
game_background = pygame.image.load('game_background.bmp')
menu_background = pygame.image.load('menu_background.bmp')
options_background = pygame.image.load('options_background.bmp')
highscores_background = pygame.image.load('highscores_background.bmp')
help_background = pygame.image.load('help_background.bmp')
menu_header = pygame.transform.scale(pygame.image.load('header_mainmenu.bmp'),(400,120))
highscore_header = pygame.transform.scale(pygame.image.load('header_highscore.bmp'),(400,120))
options_header = pygame.transform.scale(pygame.image.load('header_options.bmp'),(400,120))
help_header = pygame.transform.scale(pygame.image.load('header_help.bmp'),(400,120))
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
            pygame.quit()
            quit()
    return False
def button(msg, x, y, w, h, color_active, color_inactive, action=None):
     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if (x + w > mouse[0] > x) and (y + h > mouse[1] > y):
         block(x, y, w, h, color_active)
         if click[0] == 1 and action != None:
            return action
     else:
         block(x, y, w, h, color_inactive)
     smallText = pygame.font.Font("freesansbold.ttf", 30)
     textSurf, textRect = text_object(msg, smallText, black)
     textRect.center = ((x + (w/2)), (y + (h/2)))
     screen.blit(textSurf, textRect)
def text_object(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
def text(msg, font, x, y, w, h, color):
     font = font
     textSurf, textRect = text_object(msg, font, color)
     textRect.center = ((x + (w/2)), (y + (h/2)))
     screen.blit(textSurf, textRect)
class Help1:
    def __init__(self):
        self.type = "help1"
        self.returnbutton = None
    def buttons(self):
        # returnbutton
        self.returnbutton = button("Back to main menu", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 200,400,50,grey,white,None)
        self.instructionbutton = button("Instructions",50, 300,400,50,grey,white,None)
        self.cardbutton = button("Instructions",50, 400,400,50,grey,white,None)
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()
class Help2:
    def __init__(self):
        self.type = "help2"
        self.returnbutton = None
    def buttons(self):
        # returnbutton
        self.returnbutton = button("Back to game", 50, 650, 400, 50, grey, white, "return")
        self.returnbutton = button("Back to main menu", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 200,400,50,grey,white,None)
        self.instructionbutton = button("Instructions",50, 300,400,50,grey,white,None)
        self.cardbutton = button("Instructions",50, 400,400,50,grey,white,None)
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()
class Highscores:
    def __init__(self):
        self.type = "highscores"
        self.quitbutton = None
    def buttons(self):
        #quitbutton
        self.quitbutton = button("Back to main menu", 50, 650, 400, 50, grey, white, "quit")
    def texts(self):
        text("Highscores", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(highscores_background, (0,0))
        self.buttons()
        self.texts()
        screen.blit(highscore_header, (50,50))
        pygame.display.flip()
class Options:
    def __init__(self):
        self.type = "options"
        self.quitbutton = None
    def buttons(self):
        # quitbutton
        self.quitbutton = button("Back to main menu", 50, 650, 400, 50, grey, white, "quit")
    def texts(self):
        text("Options", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(options_background, (0,0))
        self.buttons()
        self.texts()
        screen.blit(options_header, (50,50))
        pygame.display.flip()
class Menu:
    def __init__(self):
        self.type = "menu"
        self.startbutton = None
        self.exitbutton = None
        self.optionsbutton = None
        self.highscoresbutton = None
        self.helpbutton = None
    def buttons(self):
        # startbutton
        self.startbutton = button("Start The Game!", 950, 150, 300, 70, grey, white, "start")
        # loadbutton
        loadbutton = button("Load A Game!", 950, 250, 300, 70, grey, white, "load")
        # highscoresbutton
        self.highscoresbutton = button("Highscores", 950, 350, 300, 70, grey, white, "highscores")
        # optionsbutton
        self.optionsbutton = button("Options", 950, 450, 300, 70, grey, white, "options")
        # helpbutton
        self.helpbutton = button("!!!HELP!!!", 950, 550, 300, 70, grey, white, "help")
        # exitbutton
        self.exitbutton = button("Exit The Game", 950, 650, 300, 70, grey, white, "exit")
    def texts(self):
        text("Main Menu", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(menu_background, (0,0))
        self.buttons()
        self.texts()
        screen.blit(menu_header, (50,50))
        pygame.display.flip()
class Battleport:
    def __init__(self):
        screen.fill(background_blue)
        self.type = "battleport"
        self.quitbutton = None
        self.helpbutton = None
    def buttons(self):
        # helpbutton ingame
        self.helpbutton = button("?", 1100, 26, 80, 80, grey, white, "help")
        # pausebutton
        self.pausebutton = button("||", 1190, 26, 80, 80, grey, white)
        # quitbutton
        self.quitbutton = button("X", 1280, 26, 80, 80, grey, white, "quit")
    #def texts(self):
        
    def draw(self):
        screen.fill((background_blue))
        screen.blit(game_background, (0,0))
        self.buttons()
        #self.texts()
        pygame.display.flip()
running = Menu()
while not(process_events()):
    if running.type == "menu":
        if running.startbutton == "start":
            running = Battleport()
        elif running.exitbutton == "exit":
            pygame.quit()
            quit()
        elif running.optionsbutton == "options":
            running = Options()
        elif running.highscoresbutton == "highscores":
            running = Highscores()
        elif running.helpbutton == "help":
            running = Help1()
    elif running.type == "battleport":
        if running.quitbutton == "quit":
            running = Menu()
        elif running.helpbutton == "help":
            running = Help2()
    elif running.type == "options":
        if running.quitbutton == "quit":
            running = Menu()
    elif running.type == "highscores":
        if running.quitbutton == "quit":
            running = Menu()
    elif running.type == "help1":
        if running.returnbutton == "return":
            running = Menu()
    elif running.type == "help2":
        if running.returnbutton == "return":
            running = Battleport()
    running.draw()