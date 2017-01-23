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
#boot2
  #groen
boot2groen = pygame.image.load('boot2groen.png')
boot2groen90 = pygame.transform.rotate(boot2groen, 90)
boot2groen180 = pygame.transform.rotate(boot2groen, 180)
boot2groen270 = pygame.transform.rotate(boot2groen, 270)
  #rood
boot2rood = pygame.image.load('boot2rood.png')
boot2rood90 = pygame.transform.rotate(boot2rood, 90)
boot2rood180 = pygame.transform.rotate(boot2rood, 180)
boot2rood270 = pygame.transform.rotate(boot2rood, 270)
#boot3
  #groen
boot3groen = pygame.image.load('boot3groen.png')
boot3groen90 = pygame.transform.rotate(boot3groen, 90)
boot3groen180 = pygame.transform.rotate(boot3groen, 180)
boot3groen270 = pygame.transform.rotate(boot3groen, 270)
  #rood
boot3rood = pygame.image.load('boot3rood.png')
boot3rood90 = pygame.transform.rotate(boot3rood, 90)
boot3rood180 = pygame.transform.rotate(boot3rood, 180)
boot3rood270 = pygame.transform.rotate(boot3rood, 270)
#boot4
  #groen
boot4groen = pygame.image.load('boot4groen.png')
boot3groen90 = pygame.transform.rotate(boot4groen, 90)
boot3groen180 = pygame.transform.rotate(boot4groen, 180)
boot3groen270 = pygame.transform.rotate(boot4groen, 270)
  #rood
boot4rood = pygame.image.load('boot4rood.png')
boot4rood90 = pygame.transform.rotate(boot4rood, 90)
boot4rood180 = pygame.transform.rotate(boot4rood, 180)
boot4rood270 = pygame.transform.rotate(boot4rood, 270)

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
        self.startbutton = button("Start Game", 950, 150, 300, 70, grey, white, "start")
        # loadbutton
        loadbutton = button("Load Game", 950, 250, 300, 70, grey, white, "load")
        # highscoresbutton
        self.highscoresbutton = button("Highscores", 950, 350, 300, 70, grey, white, "highscores")
        # optionsbutton
        self.optionsbutton = button("Options", 950, 450, 300, 70, grey, white, "options")
        # helpbutton
        self.helpbutton = button("Help", 950, 550, 300, 70, grey, white, "help")
        # exitbutton
        self.exitbutton = button("Exit Game", 950, 650, 300, 70, grey, white, "exit")
    def texts(self):
        text("Main Menu", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(menu_background, (0,0))
        self.buttons()
        self.texts()
        screen.blit(menu_header, (50,50))
        pygame.display.flip()
class Ship:
    def __init__(self, length, x, y, color, rotation):
        self.Length = length
        self.X = x
        self.Y = y
        self.Color = color
        self.Rotation = rotation
    def draw(self):
        if self.Length == 2:
            if self.Color == "rood":
                if self.Rotation == 0:
                    screen.blit(boot2rood, (self.X, self.Y))
                elif self.Rotation == 90:
                    screen.blit(boot2rood90, (self.X,self.Y))
                elif self.Rotation == 180:
                    screen.blit(boot2rood180, (self.X,self.Y))
                elif self.Rotation == 270:
                    screen.blit(boot2rood270, (self.X,self.Y))
            else:
                if self.Rotation == 0:
                    screen.blit(boot2groen, (self.X, self.Y))
                elif self.Rotation == 90:
                    screen.blit(boot2groen90, (self.X,self.Y))
                elif self.Rotation == 180:
                    screen.blit(boot2groen180, (self.X,self.Y))
                elif self.Rotation == 270:
                    screen.blit(boot2groen270, (self.X,self.Y))
        elif self.Length == 3:
            if self.Color == "rood":
                if self.Rotation == 0:
                    screen.blit(boot3rood, (self.X, self.Y))
                elif self.Rotation == 90:
                    screen.blit(boot3rood90, (self.X,self.Y))
                elif self.Rotation == 180:
                    screen.blit(boot3rood180, (self.X,self.Y))
                elif self.Rotation == 270:
                    screen.blit(boot3rood270, (self.X,self.Y))
            else:
                if self.Rotation == 0:
                    screen.blit(boot3groen, (self.X, self.Y))
                elif self.Rotation == 90:
                    screen.blit(boot3groen90, (self.X,self.Y))
                elif self.Rotation == 180:
                    screen.blit(boot3groen180, (self.X,self.Y))
                elif self.Rotation == 270:
                    screen.blit(boot3groen270, (self.X,self.Y))
        else:
            if self.Color == "rood":
                if self.Rotation == 0:
                    screen.blit(boot4rood, (self.X, self.Y))
                elif self.Rotation == 90:
                    screen.blit(boot4rood90, (self.X,self.Y))
                elif self.Rotation == 180:
                    screen.blit(boot4rood180, (self.X,self.Y))
                elif self.Rotation == 270:
                    screen.blit(boot4rood270, (self.X,self.Y))
            else:
                if self.Rotation == 0:
                    screen.blit(boot4groen, (self.X, self.Y))
                elif self.Rotation == 90:
                    screen.blit(boot4groen90, (self.X,self.Y))
                elif self.Rotation == 180:
                    screen.blit(boot4groen180, (self.X,self.Y))
                elif self.Rotation == 270:
                    screen.blit(boot4groen270, (self.X,self.Y))
class Battleport:
    def __init__(self):
        screen.fill(background_blue)
        self.type = "battleport"
        self.quitbutton = None
        self.helpbutton = None
        self.ship1rood = Ship(2, 79, 65, "rood", 180)
        self.ship2rood = Ship(3, 144, 65, "rood", 180)
        self.ship3rood = Ship(3, 209, 65, "rood", 180)
        self.ship4rood = Ship(4, 274, 65, "rood", 270)
        self.ship1groen = Ship(2, 79, 640, "groen", 0)
        self.ship2groen = Ship(3, 144, 609, "groen", 0)
        self.ship3groen = Ship(3, 209, 609, "groen", 0)
        self.ship4groen = Ship(4, 274, 576, "groen", 0)
    def buttons(self): 
        # helpbutton ingame
        self.helpbutton = button("?", 1100, 26, 80, 80, grey, white, "help")
        # pausebutton
        self.savebutton = button("||", 1190, 26, 80, 80, grey, white)
        # quitbutton
        self.quitbutton = button("X", 1280, 26, 80, 80, grey, white, "quit")
    #def texts(self):
        
    def draw(self):
        screen.fill((background_blue))
        screen.blit(game_background, (0,0))
        self.buttons()
        #self.texts()
        self.ship1rood.draw()
        self.ship2rood.draw()
        self.ship3rood.draw()
        self.ship4rood.draw()
        self.ship1groen.draw()
        self.ship2groen.draw()
        self.ship3groen.draw()
        self.ship4groen.draw()
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