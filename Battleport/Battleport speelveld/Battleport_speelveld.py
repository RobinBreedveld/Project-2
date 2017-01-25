import pygame
from pygame.locals import*
pygame.init()
import pygame.gfxdraw
import psycopg2

#database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=battleport user=postgres password=<zelf invullen>")
    cursor = connection.cursor()
    
    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()
    
    return results



def download_scores():
    return interact_with_database("SELECT * FROM highscore")


#sounds
click = pygame.mixer.Sound("click.ogg")
pygame.mixer.music.load("sea.ogg")
mainmenu_music = pygame.mixer.Sound("warmusic.ogg")
mainmenu_music.play(-1)
#pictures
game_background = pygame.image.load('game_background.bmp')
menu_background = pygame.image.load('menu_background.bmp')
options_background = pygame.image.load('options_background.bmp')
highscores_background = pygame.image.load('highscores_background.bmp')
help_background = pygame.image.load('help_background.bmp')
logo1 = pygame.image.load('logo1.bmp')
tekst1 = pygame.image.load('tekst1.png')
tekst2 = pygame.image.load('tekst2.png')
menu_header = pygame.transform.scale(pygame.image.load('header_mainmenu.bmp'),(400,120))
highscore_header = pygame.transform.scale(pygame.image.load('header_highscore.bmp'),(400,120))
options_header = pygame.transform.scale(pygame.image.load('header_options.bmp'),(400,120))
help_header = pygame.transform.scale(pygame.image.load('header_help.bmp'),(400,120))
rotateLeftActive = pygame.image.load('draai_links_active.png')
rotateRightActive = pygame.image.load('draai_rechts_active.png')
rotateLeftInactive = pygame.image.load('draai_links_inactive.png')
rotateRightInactive = pygame.image.load('draai_rechts_inactive.png')
pijlDownActive = pygame.image.load('pijl_down_active.png')
pijlDownInactive = pygame.image.load('pijl_down_inactive.png')
pijlUpActive = pygame.transform.rotate(pijlDownActive, 180)
pijlUpInactive = pygame.transform.rotate(pijlDownInactive, 180)
pijlLeftActive = pygame.transform.rotate(pijlDownActive, 270)
pijlLeftInactive = pygame.transform.rotate(pijlDownInactive, 270)
pijlRightActive = pygame.transform.rotate(pijlDownActive, 90)
pijlRightInactive = pygame.transform.rotate(pijlDownInactive, 90)
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
invisible = (255, 255, 255)
screen = pygame.display.set_mode((w, h))
def block(x, y, w, h, color):
    pygame.draw.rect(screen, color, [x, y, w, h])
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    return False
def button(msg, x, y, w, h, color_active, color_inactive, action=None, font="freesansbold.ttf"):
     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if (x + w > mouse[0] > x) and (y + h > mouse[1] > y):
         block(x, y, w, h, color_active)
         if click[0] == 1 and action != None:
            return action
     else:
         block(x, y, w, h, color_inactive)
     smallText = pygame.font.Font(font, 30)
     textSurf, textRect = text_object(msg, smallText, black)
     textRect.center = ((x + (w/2)), (y + (h/2)))
     screen.blit(textSurf, textRect)
def clickable_picture(x, y, w, h, picture_active, picture_inactive, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x + w > mouse[0] > x) and (y + h > mouse[1] > y):
        screen.blit(picture_active, (x, y))
        if click[0] == 1:
            return action
    else:
        screen.blit(picture_inactive, (x, y))
    
def text_object(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
def text(msg, font, x, y, w, h, color):
     font = font
     textSurf, textRect = text_object(msg, font, color)
     textRect.center = ((x + (w/2)), (y + (h/2)))
     screen.blit(textSurf, textRect)
class Coordinate:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        self.Px = 48 + (self.X * 32)
        self.Py = 64 + (self.Y * 32)
class Help1:
    def __init__(self):
        self.type = "help1"
        self.returnbutton = None
    def buttons(self):
        # returnbutton
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 200,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50, 300,400,50,grey,white,None)
        self.cardbutton = button("Cards",50, 400,400,50,grey,white,None)
        self.prevbutton = button("<",1200, 650,50,50,grey,white,None)
        self.nextbutton = button(">",1251, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(tekst1, (500,80))
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
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 200,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50, 300,400,50,grey,white,None)
        self.cardbutton = button("Cards",50, 400,400,50,grey,white,None)
        self.prevbutton = button("<",1200, 650,50,50,grey,white,None)
        self.nextbutton = button(">",1251, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(tekst1, (500,80))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()
class Helpr1:
    def __init__(self):
        self.type = "helpr1"
        self.returnbutton = None
    def buttons(self):
        # returnbutton
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 200,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50, 300,400,50,grey,white,None)
        self.cardbutton = button("Cards",50, 400,400,50,grey,white,None)
        self.prevbutton = button("<",1200, 650,50,50,grey,white,"help")
        self.nextbutton = button(">",1251, 650,50,50,grey,white,None)
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(tekst2, (500,80))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()
class Highscores:
    def __init__(self):
        self.type = "highscores"
        self.quitbutton = None
        self.highscore = download_scores()
        self.font = pygame.font.Font(None, 100)
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
        self.score_text = self.font.render((str(self.highscore)),
                                                   1, (255, 255, 255))
        screen.blit(self.score_text, (400, 300))

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
        screen.blit(logo1,((w * 0.33),(h * 0.2)))
        self.buttons()
        self.texts()
        screen.blit(menu_header, (50,50))
        pygame.display.flip()
class Ship:
    def __init__(self, length, x, y, color, rotation, name):
        self.Name = name
        self.Length = length
        self.Width = 32
        self.Height = self.Length * 32
        self.Coordinate = Coordinate(x, y)
        if self.Length == 2:
            self.Movement = 3
        elif self.Length == 3:
            self.Movement = 2
        else:
            self.Movement = 1
        self.Color = color
        self.Rotation = rotation
        self.selectbutton = None
        self.selected = 0
        self.Active = False
    def clickpicture(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (self.Coordinate.Px + self.Width > mouse[0] > self.Coordinate.Px) and (self.Coordinate.Py + self.Height > mouse[1] > self.Coordinate.Py):
            if click[0] == 1:
                self.selected = 1
            else:
                self.selected = 0
        if self.selected == 1:
            self.Active = True
    def move(self):
        if turn == self.Color:
            self.Steps = self.Movement

    def draw(self):
        if self.Length == 2:
            if self.Color == "rood":
                if self.Rotation == 0:
                    screen.blit(boot2rood, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 90:
                    screen.blit(boot2rood90, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 180:
                    screen.blit(boot2rood180, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 270:
                    screen.blit(boot2rood270, (self.Coordinate.Px, self.Coordinate.Py))
            else:
                if self.Rotation == 0:
                    screen.blit(boot2groen, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 90:
                    screen.blit(boot2groen90, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 180:
                    screen.blit(boot2groen180, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 270:
                    screen.blit(boot2groen270, (self.Coordinate.Px, self.Coordinate.Py))
        elif self.Length == 3:
            if self.Color == "rood":
                if self.Rotation == 0:
                    screen.blit(boot3rood, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 90:
                    screen.blit(boot3rood90, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 180:
                    screen.blit(boot3rood180, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 270:
                    screen.blit(boot3rood270, (self.Coordinate.Px, self.Coordinate.Py))
            else:
                if self.Rotation == 0:
                    screen.blit(boot3groen, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 90:
                    screen.blit(boot3groen90, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 180:
                    screen.blit(boot3groen180, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 270:
                    screen.blit(boot3groen270, (self.Coordinate.Px, self.Coordinate.Py))
        else:
            if self.Color == "rood":
                if self.Rotation == 0:
                    screen.blit(boot4rood, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 90:
                    screen.blit(boot4rood90, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 180:
                    screen.blit(boot4rood180, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 270:
                    screen.blit(boot4rood270, (self.Coordinate.Px, self.Coordinate.Py))
            else:
                if self.Rotation == 0:
                    screen.blit(boot4groen, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 90:
                    screen.blit(boot4groen90, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 180:
                    screen.blit(boot4groen180, (self.Coordinate.Px, self.Coordinate.Py))
                elif self.Rotation == 270:
                    screen.blit(boot4groen270, (self.Coordinate.Px, self.Coordinate.Py))
class Battleport:
    def __init__(self):
        screen.fill(background_blue)
        self.type = "battleport"
        self.quitbutton = None
        self.helpbutton = None
        self.ship1rood = Ship(2, 1, 0, "rood", 180, "rood1")
        self.ship2rood = Ship(3, 4, 0, "rood", 180, "rood2")
        self.ship3rood = Ship(3, 12, 0, "rood", 180, "rood3")
        self.ship4rood = Ship(4, 18, 0, "rood", 180, "rood4")
        self.ship1groen = Ship(2, 11, 18, "groen", 0, "groen1")
        self.ship2groen = Ship(3, 6, 17, "groen", 0, "groen2")
        self.ship3groen = Ship(3, 2, 17, "groen", 0, "groen3")
        self.ship4groen = Ship(4, 18, 16, "groen", 0, "groen4")
    def buttons(self): 
        # helpbutton ingame
        self.helpbutton = button("?", 1100, 26, 80, 80, grey, white, "help")
        # pausebutton
        self.savebutton = button("||", 1190, 26, 80, 80, grey, white)
        # quitbutton
        self.quitbutton = button("X", 1280, 26, 80, 80, grey, white, "quit")
    def draw(self):
        screen.fill((background_blue))
        screen.blit(game_background, (0,0))
        self.buttons()
        self.ship1rood.clickpicture()
        self.ship2rood.clickpicture()
        self.ship3rood.clickpicture()
        self.ship4rood.clickpicture()
        self.ship1groen.clickpicture()
        self.ship2groen.clickpicture()
        self.ship3groen.clickpicture()
        self.ship4groen.clickpicture()
        if self.ship1rood.Active:
            self.move_up_button = clickable_picture(799, 60, 50, 50, pijlUpActive, pijlUpInactive, "up",)
            self.move_down_button = clickable_picture(799, 180, 50, 50, pijlDownActive, pijlDownInactive, "down")
            self.move_left_button = clickable_picture(739, 120, 50, 50, pijlLeftActive, pijlLeftInactive, "left")
            self.move_right_button = clickable_picture(859, 120, 50, 50, pijlRightActive, pijlRightInactive, "right")
            self.cancel_button = button("X", 799, 120, 50, 50, grey, white, "cancel")
            self.rotate_left_button = clickable_picture(739, 60, 50, 50, rotateLeftActive, rotateLeftInactive, "rotate_left")
            self.rotate_left_button = clickable_picture(859, 60, 50, 50, rotateRightActive, rotateRightInactive, "rotate_right")
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
            pygame.mixer.Sound.play(click)
            pygame.mixer.music.play(-1)
            mainmenu_music.stop()
            running = Battleport()
        elif running.exitbutton == "exit":
            pygame.mixer.Sound.play(click)
            pygame.quit()
            quit()
        elif running.optionsbutton == "options":
            pygame.mixer.Sound.play(click)
            running = Options()
        elif running.highscoresbutton == "highscores":
            pygame.mixer.Sound.play(click)
            running = Highscores()
        elif running.helpbutton == "help":
            pygame.mixer.Sound.play(click)
            running = Help1()
    elif running.type == "battleport":
        if running.quitbutton == "quit":
            pygame.mixer.Sound.play(click)
            pygame.mixer.music.stop()
            running = Menu()
        elif running.helpbutton == "help":
            pygame.mixer.Sound.play(click)
            running = Help2()

    elif running.type == "options":
        if running.quitbutton == "quit":
            pygame.mixer.Sound.play(click)
            running = Menu()
    elif running.type == "highscores":
        if running.quitbutton == "quit":
            pygame.mixer.Sound.play(click)
            running = Menu()
    elif running.type == "help1":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Menu()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Helpr1()
        elif running.rulesbutton == "rules1":
            #pygame.mixer.Sound.play(click)
            running = Help1()
    elif running.type == "help2":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Battleport()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Helpr1()

    elif running.type == "helpr1":
        if running.prevbutton == "help":
            pygame.mixer.Sound.play(click)
            running = Help1()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help1()
    running.draw()