import pygame
from pygame.locals import*
pygame.init()
import pygame.gfxdraw
import psycopg2

#database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=battleport user=postgres password=<wachtwoord hier>")
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
instructions_pg1 = pygame.image.load('Instructions_pg1.bmp')
instructions_pg2 = pygame.image.load('Instructions_pg2.bmp')
instructions_pg3 = pygame.image.load('Instructions_pg3.bmp')
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
range_indicator = pygame.image.load('range_indicator.png')
attack_indicator = pygame.image.load('attack_indicator.png')
ship_stats = pygame.image.load('ship_stats.bmp')
o1 = pygame.image.load('o1.png')
o2 = pygame.image.load('o2.png')
o3 = pygame.image.load('o3.png')
o4 = pygame.image.load('o4.png')
o5 = pygame.image.load('o5.png')
d1 = pygame.image.load('d1.png')
d2 = pygame.image.load('d2.png')
d3 = pygame.image.load('d3.png')
d4 = pygame.image.load('d4.png')
u1 = pygame.image.load('u1.png')
u2 = pygame.image.load('u2.png')
u3 = pygame.image.load('u3.png')
u4 = pygame.image.load('u4.png')
u5 = pygame.image.load('u5.png')
s1 = pygame.image.load('s1.png')
s2 = pygame.image.load('s2.png')
s3 = pygame.image.load('s3.png')
s4 = pygame.image.load('s4.png')
s5 = pygame.image.load('s5.png')
s6 = pygame.image.load('s6.png')

o1 = pygame.transform.scale(o1,(250,345))
o2 = pygame.transform.scale(o2,(250,345))
o3 = pygame.transform.scale(o3,(250,345)) 
o4 = pygame.transform.scale(o4,(250,345))
o5 = pygame.transform.scale(o5,(250,345))
d1 = pygame.transform.scale(d1,(250,345))
d2 = pygame.transform.scale(d2,(250,345))
d3 = pygame.transform.scale(d3,(250,345))
d4 = pygame.transform.scale(d4,(250,345))
u1 = pygame.transform.scale(u1,(250,345))
u2 = pygame.transform.scale(u2,(250,345))
u3 = pygame.transform.scale(u3,(250,345))
u4 = pygame.transform.scale(u4,(250,345))
u5 = pygame.transform.scale(u5,(250,345))
s1 = pygame.transform.scale(s1,(250,345))
s2 = pygame.transform.scale(s2,(250,435))
s3 = pygame.transform.scale(s3,(250,345))
s4 = pygame.transform.scale(s4,(250,345))
s5 = pygame.transform.scale(s5,(250,345))
s6 = pygame.transform.scale(s6,(250,345))

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
boot4groen90 = pygame.transform.rotate(boot4groen, 90)
boot4groen180 = pygame.transform.rotate(boot4groen, 180)
boot4groen270 = pygame.transform.rotate(boot4groen, 270)
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
def button(msg, x, y, w, h, color_active, color_inactive, action=None, font="freesansbold.ttf", size=30):
     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if (x + w > mouse[0] > x) and (y + h > mouse[1] > y):
         block(x, y, w, h, color_active)
         if click[0] == 1 and action != None:
            return action
     else:
         block(x, y, w, h, color_inactive)
     smallText = pygame.font.Font(font, size)
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
    def Update(self):
        self.Px = 48 + (self.X * 32)
        self.Py = 64 + (self.Y * 32)
class Help1:
    def __init__(self):
        self.type = "help1"
        self.returnbutton = None
    def buttons(self):
        # returnbutton
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        #self.prevbutton = button("<",839, 650,50,50,grey,white,None)
        self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(tekst1, (864,50))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()
#Helpmenu regels pg2
class Helpr1:
    def __init__(self):
        self.type = "helpr1"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        #self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(tekst2, (864,50))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()
#Helpmenu instructions pg1
class Helpi1:
    def __init__(self):
        self.type = "helpi1"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        #self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(instructions_pg1, (864,50))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()
#Helpmenu instructions pg2
class Helpi2:
    def __init__(self):
        self.type = "helpi2"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        #self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(instructions_pg2, (864,50))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()
#Helpmenu extra instructions
class Helpx1:
    def __init__(self):
        self.type = "helpx1"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        #self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        #self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(instructions_pg3, (864,50))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()

#Helpmenu vanaf game
class Help2:
    def __init__(self):
        self.type = "help2"
        self.returnbutton = None
    def buttons(self):
        # returnbutton
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        #self.prevbutton = button("<",839, 650,50,50,grey,white,None)
        self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(tekst1, (864,50))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()
#Helpmenu regels pg2
class Help2r1:
    def __init__(self):
        self.type = "help2r1"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        #self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(tekst2, (864,50))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()
#Helpmenu instructions pg1
class Help2i1:
    def __init__(self):
        self.type = "help2i1"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        #self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(instructions_pg1, (864,50))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()
#Helpmenu instructions pg2
class Help2i2:
    def __init__(self):
        self.type = "help2i2"
        self.returnbutton = None
    def buttons(self):
        # returnbutton
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        #self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(instructions_pg2, (864,50))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()
#Helpmenu extra instructions
class Help2x1:
    def __init__(self):
        self.type = "help2x1"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        #self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        #self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(instructions_pg3, (864,50))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()
class Cards1:
    def __init__ (self):
        self.type = "cards1"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        #self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(o1, (500,50))
        screen.blit(o2, (750,50))
        screen.blit(o3, (1000,50))
        screen.blit(o4, (500,395))
        screen.blit(o5, (750,395))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()

class Cards2:
    def __init__ (self):
        self.type = "cards2"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(d1, (500,50))
        screen.blit(d2, (750,50))
        screen.blit(d3, (1000,50))
        screen.blit(d4, (500,395))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()

class Cards3:
    def __init__ (self):
        self.type = "cards3"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(u1, (500,50))
        screen.blit(u2, (750,50))
        screen.blit(u3, (1000,50))
        screen.blit(u4, (500,395))
        screen.blit(u5, (750,395))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()

class Cards4:
    def __init__ (self):
        self.type = "cards4"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        #self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(s1, (500,50))
        screen.blit(s2, (750,50))
        screen.blit(s3, (1000,50))
        screen.blit(s4, (500,395))
        screen.blit(s5, (750,395))
        screen.blit(s6, (1000,395))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()
#--------------------------------------- hep menu to game

class Cards1g:
    def __init__ (self):
        self.type = "cards1g"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        #self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(o1, (500,50))
        screen.blit(o2, (750,50))
        screen.blit(o3, (1000,50))
        screen.blit(o4, (500,395))
        screen.blit(o5, (750,395))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()

class Cards2g:
    def __init__ (self):
        self.type = "cards2g"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(d1, (500,50))
        screen.blit(d2, (750,50))
        screen.blit(d3, (1000,50))
        screen.blit(d4, (500,395))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()

class Cards3g:
    def __init__ (self):
        self.type = "cards3g"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(u1, (500,50))
        screen.blit(u2, (750,50))
        screen.blit(u3, (1000,50))
        screen.blit(u4, (500,395))
        screen.blit(u5, (750,395))
        self.buttons()
        self.texts()
        screen.blit(help_header, (50,50))
        pygame.display.flip()

class Cards4g:
    def __init__ (self):
        self.type = "cards4g"
        self.returnbutton = None
    def buttons(self):
        self.returnbutton = button("Back", 50, 650, 400, 50, grey, white, "return")
        self.rulesbutton = button("Rules",50, 220,400,50,grey,white,"rules1")
        self.instructionbutton = button("Instructions",50,300,400,50,grey,white,"instructions1")
        self.extrabutton = button("Extra",50, 380,400,50,grey,white,"extra")
        self.cardbutton = button("Cards",50, 460,400,50,grey,white,"cards1")
        self.prevbutton = button("<",839, 650,50,50,grey,white,"help")
        #self.nextbutton = button(">",1289, 650,50,50,grey,white,"next")
    def texts(self):
        text("HELP", pygame.font.Font("freesansbold.ttf", 50), 50, 50, 300, 75, white)
    def draw(self):
        screen.fill((background_blue))
        screen.blit(help_background, (0,0))
        screen.blit(s1, (500,50))
        screen.blit(s2, (750,50))
        screen.blit(s3, (1000,50))
        screen.blit(s4, (500,395))
        screen.blit(s5, (750,395))
        screen.blit(s6, (1000,395))
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
        self.Steps = 0
        self.Stance = "normal"
        self.Range = self.Length
        #rechterkant
        self.pos1 = Coordinate((x - 4), y)
        self.pos2 = Coordinate((x - 3), y)
        self.pos3 = Coordinate((x - 2), y)
        self.pos4 = Coordinate((x - 1), y)
        self.pos5 = Coordinate((x - 4), y + 1)
        self.pos6 = Coordinate((x - 3), y + 1)
        self.pos7 = Coordinate((x - 2), y + 1)
        self.pos8 = Coordinate((x - 1), y + 1)
        self.pos9 = Coordinate((x - 4), y + 2)
        self.pos10 = Coordinate((x - 3), y + 2)
        self.pos11 = Coordinate((x - 2), y + 2)
        self.pos12 = Coordinate((x - 1), y + 2)
        self.pos13 = Coordinate((x - 4), y + 3)
        self.pos14 = Coordinate((x - 3), y + 3)
        self.pos15 = Coordinate((x - 2), y + 3)
        self.pos16 = Coordinate((x - 1), y + 3)
        #linkerkant
        self.pos17 = Coordinate((x + 4), y)
        self.pos18 = Coordinate((x + 3), y)
        self.pos19 = Coordinate((x + 2), y)
        self.pos20 = Coordinate((x + 1), y)
        self.pos21 = Coordinate((x + 4), y + 1)
        self.pos22 = Coordinate((x + 3), y + 1)
        self.pos23 = Coordinate((x + 2), y + 1)
        self.pos24 = Coordinate((x + 1), y + 1)
        self.pos25 = Coordinate((x + 4), y + 2)
        self.pos26 = Coordinate((x + 3), y + 2)
        self.pos27 = Coordinate((x + 2), y + 2)
        self.pos28 = Coordinate((x + 1), y + 2)
        self.pos29 = Coordinate((x + 4), y + 3)
        self.pos30 = Coordinate((x + 3), y + 3)
        self.pos31 = Coordinate((x + 2), y + 3)
        self.pos32 = Coordinate((x + 1), y + 3)
        #onderkant
        self.pos33 = Coordinate(x, y + self.Length)
        self.pos34 = Coordinate(x, y + self.Length + 1)
        self.pos35 = Coordinate(x, y + self.Length + 2)
        self.pos36 = Coordinate(x, y + self.Length + 3)
        #bovenkant
        self.pos37 = Coordinate(x, y - self.Length)
        self.pos38 = Coordinate(x, y - self.Length - 1)
        self.pos39 = Coordinate(x, y - self.Length - 2)
        self.pos40 = Coordinate(x, y - self.Length - 3)
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
        self.Steps = self.Movement
    def rotate(self, amount):
        self.Rotation += amount
        self.Steps -= 1
        if self.Rotation == 360:
            self.Rotation = 0
        if self.Rotation == -90:
            self.Rotation = 270
    def attack(self):
        if self.Stance == "attack":
            self.Range = self.Length
            #linkerkant
            self.pos1.X = self.Coordinate.X - 4
            self.pos1.Y = self.Coordinate.Y
            self.pos2.X = self.Coordinate.X - 3
            self.pos2.Y = self.Coordinate.Y
            self.pos3.X = self.Coordinate.X - 2
            self.pos3.Y = self.Coordinate.Y
            self.pos4.X = self.Coordinate.X - 1
            self.pos4.Y = self.Coordinate.Y
            self.pos5.X = self.Coordinate.X - 4
            self.pos5.Y = self.Coordinate.Y + 1
            self.pos6.X = self.Coordinate.X - 3
            self.pos6.Y = self.Coordinate.Y + 1
            self.pos7.X = self.Coordinate.X - 2
            self.pos7.Y = self.Coordinate.Y + 1
            self.pos8.X = self.Coordinate.X - 1
            self.pos8.Y = self.Coordinate.Y + 1
            self.pos9.X = self.Coordinate.X - 4
            self.pos9.Y = self.Coordinate.Y + 2
            self.pos10.X = self.Coordinate.X - 3
            self.pos10.Y = self.Coordinate.Y + 2
            self.pos11.X = self.Coordinate.X - 2
            self.pos11.Y = self.Coordinate.Y + 2
            self.pos12.X = self.Coordinate.X - 1
            self.pos12.Y = self.Coordinate.Y + 2
            self.pos13.X = self.Coordinate.X - 4
            self.pos13.Y = self.Coordinate.Y + 3
            self.pos14.X = self.Coordinate.X - 3
            self.pos14.Y = self.Coordinate.Y + 3
            self.pos15.X = self.Coordinate.X - 2
            self.pos15.Y = self.Coordinate.Y + 3
            self.pos16.X = self.Coordinate.X - 1
            self.pos16.Y = self.Coordinate.Y + 3
            #rechterkant
            self.pos17.X = self.Coordinate.X + 4
            self.pos17.Y = self.Coordinate.Y
            self.pos18.X = self.Coordinate.X + 3
            self.pos18.Y = self.Coordinate.Y 
            self.pos19.X = self.Coordinate.X + 2
            self.pos19.Y = self.Coordinate.Y
            self.pos20.X = self.Coordinate.X + 1
            self.pos20.Y = self.Coordinate.Y
            self.pos21.X = self.Coordinate.X + 4
            self.pos21.Y = self.Coordinate.Y + 1
            self.pos22.X = self.Coordinate.X + 3
            self.pos22.Y = self.Coordinate.Y + 1
            self.pos23.X = self.Coordinate.X + 2
            self.pos23.Y = self.Coordinate.Y + 1
            self.pos24.X = self.Coordinate.X + 1
            self.pos24.Y = self.Coordinate.Y + 1
            self.pos25.X = self.Coordinate.X + 4
            self.pos25.Y = self.Coordinate.Y + 2
            self.pos26.X = self.Coordinate.X + 3
            self.pos26.Y = self.Coordinate.Y + 2
            self.pos27.X = self.Coordinate.X + 2
            self.pos27.Y = self.Coordinate.Y + 2
            self.pos28.X = self.Coordinate.X + 1
            self.pos28.Y = self.Coordinate.Y + 2
            self.pos29.X = self.Coordinate.X + 4
            self.pos29.Y = self.Coordinate.Y + 3
            self.pos30.X = self.Coordinate.X + 3
            self.pos30.Y = self.Coordinate.Y + 3
            self.pos31.X = self.Coordinate.X + 2
            self.pos31.Y = self.Coordinate.Y + 3
            self.pos32.X = self.Coordinate.X + 1
            self.pos32.Y = self.Coordinate.Y + 3
            #onderkant
            self.pos33.X = self.Coordinate.X
            self.pos33.Y = self.Coordinate.Y + self.Length
            self.pos34.X = self.Coordinate.X
            self.pos34.Y = self.Coordinate.Y + self.Length + 1
            self.pos35.X = self.Coordinate.X
            self.pos35.Y = self.Coordinate.Y + self.Length + 2
            self.pos36.X = self.Coordinate.X
            self.pos36.Y = self.Coordinate.Y + self.Length + 3
            #bovenkant
            self.pos37.X = self.Coordinate.X
            self.pos37.Y = self.Coordinate.Y - 1
            self.pos38.X = self.Coordinate.X
            self.pos38.Y = self.Coordinate.Y - 2
            self.pos39.X = self.Coordinate.X
            self.pos39.Y = self.Coordinate.Y - 3
            self.pos40.X = self.Coordinate.X
            self.pos40.Y = self.Coordinate.Y - 4
            #linkerkant
            self.pos1.Update()
            self.pos2.Update()
            self.pos3.Update()
            self.pos4.Update()
            self.pos5.Update()
            self.pos6.Update()
            self.pos7.Update()
            self.pos8.Update()
            self.pos9.Update()
            self.pos10.Update()
            self.pos11.Update()
            self.pos12.Update()
            self.pos13.Update()
            self.pos14.Update()
            self.pos15.Update()
            self.pos16.Update()
            #rechterkant
            self.pos17.Update()
            self.pos18.Update()
            self.pos19.Update()
            self.pos20.Update()
            self.pos21.Update()
            self.pos22.Update()
            self.pos23.Update()
            self.pos24.Update()
            self.pos25.Update()
            self.pos26.Update()
            self.pos27.Update()
            self.pos28.Update()
            self.pos29.Update()
            self.pos30.Update()
            self.pos31.Update()
            self.pos32.Update()
            #onderkant
            self.pos33.Update()
            self.pos34.Update()
            self.pos35.Update()
            self.pos36.Update()
            #bovenkant
            self.pos37.Update()
            self.pos38.Update()
            self.pos39.Update()
            self.pos40.Update()
            if self.Length > 3:
                screen.blit(range_indicator, (self.pos1.Px, self.pos1.Py))
                screen.blit(range_indicator, (self.pos5.Px, self.pos5.Py))
                screen.blit(range_indicator, (self.pos17.Px, self.pos17.Py))
                screen.blit(range_indicator, (self.pos21.Px, self.pos21.Py))
                screen.blit(range_indicator, (self.pos9.Px, self.pos9.Py))
                screen.blit(range_indicator, (self.pos25.Px, self.pos25.Py))
                screen.blit(range_indicator, (self.pos13.Px, self.pos13.Py))
                screen.blit(range_indicator, (self.pos29.Px, self.pos29.Py))
                screen.blit(range_indicator, (self.pos36.Px, self.pos36.Py))
                screen.blit(range_indicator, (self.pos40.Px, self.pos40.Py))
            if self.Length > 2:
                if self.Length > 3:
                    screen.blit(range_indicator, (self.pos14.Px, self.pos14.Py))
                    screen.blit(range_indicator, (self.pos30.Px, self.pos30.Py))
                screen.blit(range_indicator, (self.pos2.Px, self.pos2.Py))
                screen.blit(range_indicator, (self.pos6.Px, self.pos6.Py))
                screen.blit(range_indicator, (self.pos10.Px, self.pos10.Py))
                screen.blit(range_indicator, (self.pos18.Px, self.pos18.Py))
                screen.blit(range_indicator, (self.pos22.Px, self.pos22.Py))
                screen.blit(range_indicator, (self.pos26.Px, self.pos26.Py))
                screen.blit(range_indicator, (self.pos35.Px, self.pos35.Py))
                screen.blit(range_indicator, (self.pos39.Px, self.pos39.Py))
            if self.Length > 1:
                if self.Length > 3:
                    screen.blit(range_indicator, (self.pos15.Px, self.pos15.Py))
                    screen.blit(range_indicator, (self.pos31.Px, self.pos31.Py))
                    screen.blit(range_indicator, (self.pos16.Px, self.pos16.Py))
                    screen.blit(range_indicator, (self.pos32.Px, self.pos32.Py))
                if self.Length > 2:
                    screen.blit(range_indicator, (self.pos11.Px, self.pos11.Py))
                    screen.blit(range_indicator, (self.pos27.Px, self.pos27.Py))
                    screen.blit(range_indicator, (self.pos12.Px, self.pos12.Py))
                    screen.blit(range_indicator, (self.pos28.Px, self.pos28.Py))
                screen.blit(range_indicator, (self.pos3.Px, self.pos3.Py))
                screen.blit(range_indicator, (self.pos7.Px, self.pos7.Py))
                screen.blit(range_indicator, (self.pos19.Px, self.pos19.Py))
                screen.blit(range_indicator, (self.pos23.Px, self.pos23.Py))
                screen.blit(range_indicator, (self.pos34.Px, self.pos34.Py))
                screen.blit(range_indicator, (self.pos38.Px, self.pos38.Py))
                screen.blit(range_indicator, (self.pos4.Px, self.pos4.Py))
                screen.blit(range_indicator, (self.pos8.Px, self.pos8.Py))
                screen.blit(range_indicator, (self.pos20.Px, self.pos20.Py))
                screen.blit(range_indicator, (self.pos24.Px, self.pos24.Py))
                screen.blit(range_indicator, (self.pos33.Px, self.pos33.Py))
                screen.blit(range_indicator, (self.pos37.Px, self.pos37.Py))
        elif self.Stance == "defensive":
            self.Range = self.Length + 1
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
        self.ship4rood = Ship(4, 15, 5, "rood", 180, "rood4")
        self.ship1groen = Ship(2, 11, 18, "groen", 0, "groen1")
        self.ship2groen = Ship(3, 6, 17, "groen", 0, "groen2")
        self.ship3groen = Ship(3, 2, 17, "groen", 0, "groen3")
        self.ship4groen = Ship(4, 18, 16, "groen", 0, "groen4")
        self.move_up_button_pressed = False
        self.move_down_button_pressed = False
        self.move_left_button_pressed = False
        self.move_right_button_pressed = False
        self.rotate_left_button_pressed = False
        self.rotate_right_button_pressed = False
        self.attack_button_pressed = False
        self.Turn = "rood"
    def buttons(self): 
        # helpbutton ingame
        self.helpbutton = button("?", 1100, 26, 80, 80, grey, white, "help")
        # pausebutton
        self.savebutton = button("||", 1190, 26, 80, 80, grey, white)
        # quitbutton
        self.quitbutton = button("X", 1280, 26, 80, 80, grey, white, "quit")
    def update(self):
        self.ship1rood.clickpicture()
        self.ship2rood.clickpicture()
        self.ship3rood.clickpicture()
        self.ship4rood.clickpicture()
        self.ship1groen.clickpicture()
        self.ship2groen.clickpicture()
        self.ship3groen.clickpicture()
        self.ship4groen.clickpicture()
        if self.ship1rood.Active:
            self.ship1rood.move()
            screen.blit(ship_stats,(889, 58))
            self.move_up_button = clickable_picture(769, 60, 50, 50, pijlUpActive, pijlUpInactive, True)
            self.move_down_button = clickable_picture(769, 180, 50, 50, pijlDownActive, pijlDownInactive, True)
            self.move_left_button = clickable_picture(709, 120, 50, 50, pijlLeftActive, pijlLeftInactive, True)
            self.move_right_button = clickable_picture(829, 120, 50, 50, pijlRightActive, pijlRightInactive, True)
            self.cancel_button = button("X", 769, 120, 50, 50, grey, white, True)
            self.rotate_left_button = clickable_picture(709, 60, 50, 50, rotateLeftActive, rotateLeftInactive, True)
            self.rotate_right_button = clickable_picture(829, 60, 50, 50, rotateRightActive, rotateRightInactive, True)
            self.attack_button = button("Attack", 709, 180, 50, 50, grey, white, True, "freesansbold.ttf", 15)
            if self.cancel_button:
                self.ship1rood.Active = False
            if self.move_up_button:
                self.move_up_button_pressed = True
                self.move_up_button = False
            elif self.move_up_button_pressed:
                self.ship1rood.Coordinate.Y -= 1
                self.ship1rood.Steps -= 1
                self.move_up_button_pressed = False
            if self.move_down_button:
                self.move_down_button_pressed = True
                self.move_down_button = False
            elif self.move_down_button_pressed:
                self.ship1rood.Coordinate.Y += 1
                self.ship1rood.Steps -= 1
                self.move_down_button_pressed = False
            if self.move_left_button:
                self.move_left_button_pressed = True
                self.move_left_button = False
            elif self.move_left_button_pressed:
                self.ship1rood.Coordinate.X -= 1
                self.ship1rood.Steps -= 1
                self.move_left_button_pressed = False
            if self.move_right_button:
                self.move_right_button_pressed = True
                self.move_right_button = False
            elif self.move_right_button_pressed:
                self.ship1rood.Coordinate.X += 1
                self.ship1rood.Steps -= 1
                self.move_right_button_pressed = False
            if self.rotate_left_button:
                self.rotate_left_button_pressed = True
                self.rotate_left_button = False
            elif self.rotate_left_button_pressed:
                self.ship1rood.rotate(90)
                self.rotate_left_button_pressed = False
                if self.ship1rood.Rotation == 270:
                    self.ship1rood.Coordinate.X -= 1
                    self.ship1rood.Coordinate.Y += 1
                if self.ship1rood.Rotation == 0:
                    self.ship1rood.Coordinate.X += 1
                if self.ship1rood.Rotation == 180:
                    self.ship1rood.Coordinate.Y -= 1
            if self.rotate_right_button:
                self.rotate_right_button_pressed = True
                self.rotate_right_button = False
            elif self.rotate_right_button_pressed:
                self.ship1rood.rotate(-90)
                self.rotate_right_button_pressed = False
                if self.ship1rood.Rotation == 90:
                    self.ship1rood.Coordinate.Y += 1
                if self.ship1rood.Rotation == 270:
                    self.ship1rood.Coordinate.X -= 1
                if self.ship1rood.Rotation == 180:
                    self.ship1rood.Coordinate.X += 1
                    self.ship1rood.Coordinate.Y -= 1
            if self.attack_button:
                self.attack_button_pressed = True
                self.attack_button = False
            elif self.attack_button_pressed:
                self.ship1rood.Stance = "attack"
                self.ship1rood.attack()
                self.stop_attack_button = button("stop attack", 829, 180, 50, 50, grey, white, True, 'freesansbold.ttf', 15)
                if self.stop_attack_button:
                    self.attack_button_pressed = False
        if self.ship2rood.Active:
            self.ship2rood.move()
            screen.blit(ship_stats,(889, 58))
            self.move_up_button = clickable_picture(769, 60, 50, 50, pijlUpActive, pijlUpInactive, True)
            self.move_down_button = clickable_picture(769, 180, 50, 50, pijlDownActive, pijlDownInactive, True)
            self.move_left_button = clickable_picture(709, 120, 50, 50, pijlLeftActive, pijlLeftInactive, True)
            self.move_right_button = clickable_picture(829, 120, 50, 50, pijlRightActive, pijlRightInactive, True)
            self.cancel_button = button("X", 769, 120, 50, 50, grey, white, True)
            self.rotate_left_button = clickable_picture(709, 60, 50, 50, rotateLeftActive, rotateLeftInactive, True)
            self.rotate_right_button = clickable_picture(829, 60, 50, 50, rotateRightActive, rotateRightInactive, True)
            self.attack_button = button("Attack", 709, 180, 50, 50, grey, white, True, "freesansbold.ttf", 15)
            if self.cancel_button:
                self.ship2rood.Active = False
            if self.move_up_button:
                self.move_up_button_pressed = True
                self.move_up_button = False
            elif self.move_up_button_pressed:
                self.ship2rood.Coordinate.Y -= 1
                self.ship2rood.Steps -= 1
                self.move_up_button_pressed = False
            if self.move_down_button:
                self.move_down_button_pressed = True
                self.move_down_button = False
            elif self.move_down_button_pressed:
                self.ship2rood.Coordinate.Y += 1
                self.ship2rood.Steps -= 1
                self.move_down_button_pressed = False
            if self.move_left_button:
                self.move_left_button_pressed = True
                self.move_left_button = False
            elif self.move_left_button_pressed:
                self.ship2rood.Coordinate.X -= 1
                self.ship2rood.Steps -= 1
                self.move_left_button_pressed = False
            if self.move_right_button:
                self.move_right_button_pressed = True
                self.move_right_button = False
            elif self.move_right_button_pressed:
                self.ship2rood.Coordinate.X += 1
                self.ship2rood.Steps -= 1
                self.move_right_button_pressed = False
            if self.rotate_left_button:
                self.rotate_left_button_pressed = True
                self.rotate_left_button = False
            elif self.rotate_left_button_pressed:
                self.ship2rood.rotate(90)
                self.rotate_left_button_pressed = False
                if self.ship2rood.Rotation == 270:
                    self.ship2rood.Coordinate.X -= 2
                    self.ship2rood.Coordinate.Y += 2
                if self.ship2rood.Rotation == 0:
                    self.ship2rood.Coordinate.X += 2
                if self.ship2rood.Rotation == 180:
                    self.ship2rood.Coordinate.Y -= 2
            if self.rotate_right_button:
                self.rotate_right_button_pressed = True
                self.rotate_right_button = False
            elif self.rotate_right_button_pressed:
                self.ship2rood.rotate(-90)
                self.rotate_right_button_pressed = False
                if self.ship2rood.Rotation == 90:
                    self.ship2rood.Coordinate.Y += 2
                if self.ship2rood.Rotation == 270:
                    self.ship2rood.Coordinate.X -= 2
                if self.ship2rood.Rotation == 180:
                    self.ship2rood.Coordinate.X += 2
                    self.ship2rood.Coordinate.Y -= 2
            if self.attack_button:
                self.attack_button_pressed = True
                self.attack_button = False
            elif self.attack_button_pressed:
                self.ship2rood.Stance = "attack"
                self.ship2rood.attack()
                self.stop_attack_button = button("stop attack", 829, 180, 50, 50, grey, white, True, 'freesansbold.ttf', 15)
                if self.stop_attack_button:
                    self.attack_button_pressed = False
        if self.ship3rood.Active:
            self.ship3rood.move()
            screen.blit(ship_stats,(889, 58))
            self.move_up_button = clickable_picture(769, 60, 50, 50, pijlUpActive, pijlUpInactive, True)
            self.move_down_button = clickable_picture(769, 180, 50, 50, pijlDownActive, pijlDownInactive, True)
            self.move_left_button = clickable_picture(709, 120, 50, 50, pijlLeftActive, pijlLeftInactive, True)
            self.move_right_button = clickable_picture(829, 120, 50, 50, pijlRightActive, pijlRightInactive, True)
            self.cancel_button = button("X", 769, 120, 50, 50, grey, white, True)
            self.rotate_left_button = clickable_picture(709, 60, 50, 50, rotateLeftActive, rotateLeftInactive, True)
            self.rotate_right_button = clickable_picture(829, 60, 50, 50, rotateRightActive, rotateRightInactive, True)
            self.attack_button = button("Attack", 709, 180, 50, 50, grey, white, True, "freesansbold.ttf", 15)
            if self.cancel_button:
                self.ship3rood.Active = False
            if self.move_up_button:
                self.move_up_button_pressed = True
                self.move_up_button = False
            elif self.move_up_button_pressed:
                self.ship3rood.Coordinate.Y -= 1
                self.ship3rood.Steps -= 1
                self.move_up_button_pressed = False
            if self.move_down_button:
                self.move_down_button_pressed = True
                self.move_down_button = False
            elif self.move_down_button_pressed:
                self.ship3rood.Coordinate.Y += 1
                self.ship3rood.Steps -= 1
                self.move_down_button_pressed = False
            if self.move_left_button:
                self.move_left_button_pressed = True
                self.move_left_button = False
            elif self.move_left_button_pressed:
                self.ship3rood.Coordinate.X -= 1
                self.ship3rood.Steps -= 1
                self.move_left_button_pressed = False
            if self.move_right_button:
                self.move_right_button_pressed = True
                self.move_right_button = False
            elif self.move_right_button_pressed:
                self.ship3rood.Coordinate.X += 1
                self.ship3rood.Steps -= 1
                self.move_right_button_pressed = False
            if self.rotate_left_button:
                self.rotate_left_button_pressed = True
                self.rotate_left_button = False
            elif self.rotate_left_button_pressed:
                self.ship3rood.rotate(90)
                self.rotate_left_button_pressed = False
                if self.ship3rood.Rotation == 270:
                    self.ship3rood.Coordinate.X -= 2
                    self.ship3rood.Coordinate.Y += 2
                if self.ship3rood.Rotation == 0:
                    self.ship3rood.Coordinate.X += 2
                if self.ship3rood.Rotation == 180:
                    self.ship3rood.Coordinate.Y -= 2
            if self.rotate_right_button:
                self.rotate_right_button_pressed = True
                self.rotate_right_button = False
            elif self.rotate_right_button_pressed:
                self.ship3rood.rotate(-90)
                self.rotate_right_button_pressed = False
                if self.ship3rood.Rotation == 90:
                    self.ship3rood.Coordinate.Y += 2
                if self.ship3rood.Rotation == 270:
                    self.ship3rood.Coordinate.X -= 2
                if self.ship3rood.Rotation == 180:
                    self.ship3rood.Coordinate.X += 2
                    self.ship3rood.Coordinate.Y -= 2
            if self.attack_button:
                self.attack_button_pressed = True
                self.attack_button = False
            elif self.attack_button_pressed:
                self.ship3rood.Stance = "attack"
                self.ship3rood.attack()
                self.stop_attack_button = button("stop attack", 829, 180, 50, 50, grey, white, True, 'freesansbold.ttf', 15)
                if self.stop_attack_button:
                    self.attack_button_pressed = False
        if self.ship4rood.Active:
            self.ship4rood.move()
            screen.blit(ship_stats,(889, 58))
            self.move_up_button = clickable_picture(769, 60, 50, 50, pijlUpActive, pijlUpInactive, True)
            self.move_down_button = clickable_picture(769, 180, 50, 50, pijlDownActive, pijlDownInactive, True)
            self.move_left_button = clickable_picture(709, 120, 50, 50, pijlLeftActive, pijlLeftInactive, True)
            self.move_right_button = clickable_picture(829, 120, 50, 50, pijlRightActive, pijlRightInactive, True)
            self.cancel_button = button("X", 769, 120, 50, 50, grey, white, True)
            self.rotate_left_button = clickable_picture(709, 60, 50, 50, rotateLeftActive, rotateLeftInactive, True)
            self.rotate_right_button = clickable_picture(829, 60, 50, 50, rotateRightActive, rotateRightInactive, True)
            self.attack_button = button("Attack", 709, 180, 50, 50, grey, white, True, "freesansbold.ttf", 15)
            if self.cancel_button:
                self.ship4rood.Active = False
            if self.move_up_button:
                self.move_up_button_pressed = True
                self.move_up_button = False
            elif self.move_up_button_pressed:
                self.ship4rood.Coordinate.Y -= 1
                self.ship4rood.Steps -= 1
                self.move_up_button_pressed = False
            if self.move_down_button:
                self.move_down_button_pressed = True
                self.move_down_button = False
            elif self.move_down_button_pressed:
                self.ship4rood.Coordinate.Y += 1
                self.ship4rood.Steps -= 1
                self.move_down_button_pressed = False
            if self.move_left_button:
                self.move_left_button_pressed = True
                self.move_left_button = False
            elif self.move_left_button_pressed:
                self.ship4rood.Coordinate.X -= 1
                self.ship4rood.Steps -= 1
                self.move_left_button_pressed = False
            if self.move_right_button:
                self.move_right_button_pressed = True
                self.move_right_button = False
            elif self.move_right_button_pressed:
                self.ship4rood.Coordinate.X += 1
                self.ship4rood.Steps -= 1
                self.move_right_button_pressed = False
            if self.rotate_left_button:
                self.rotate_left_button_pressed = True
                self.rotate_left_button = False
            elif self.rotate_left_button_pressed:
                self.ship4rood.rotate(90)
                self.rotate_left_button_pressed = False
                if self.ship4rood.Rotation == 270:
                    self.ship4rood.Coordinate.X -= 3
                    self.ship4rood.Coordinate.Y += 3
                if self.ship4rood.Rotation == 0:
                    self.ship4rood.Coordinate.X += 3
                if self.ship4rood.Rotation == 180:
                    self.ship4rood.Coordinate.Y -= 3
            if self.rotate_right_button:
                self.rotate_right_button_pressed = True
                self.rotate_right_button = False
            elif self.rotate_right_button_pressed:
                self.ship4rood.rotate(-90)
                self.rotate_right_button_pressed = False
                if self.ship4rood.Rotation == 90:
                    self.ship4rood.Coordinate.Y += 3
                if self.ship4rood.Rotation == 270:
                    self.ship4rood.Coordinate.X -= 3
                if self.ship4rood.Rotation == 180:
                    self.ship4rood.Coordinate.X += 3
                    self.ship4rood.Coordinate.Y -= 3
            if self.attack_button:
                self.attack_button_pressed = True
                self.attack_button = False
            elif self.attack_button_pressed:
                self.ship4rood.Stance = "attack"
                self.ship4rood.attack()
                self.stop_attack_button = button("stop attack", 829, 180, 50, 50, grey, white, True, 'freesansbold.ttf', 15)
                if self.stop_attack_button:
                    self.attack_button_pressed = False
        if self.ship1groen.Active:
            self.ship1groen.move()
            screen.blit(ship_stats,(889, 58))
            self.move_up_button = clickable_picture(769, 60, 50, 50, pijlUpActive, pijlUpInactive, True)
            self.move_down_button = clickable_picture(769, 180, 50, 50, pijlDownActive, pijlDownInactive, True)
            self.move_left_button = clickable_picture(709, 120, 50, 50, pijlLeftActive, pijlLeftInactive, True)
            self.move_right_button = clickable_picture(829, 120, 50, 50, pijlRightActive, pijlRightInactive, True)
            self.cancel_button = button("X", 769, 120, 50, 50, grey, white, True)
            self.rotate_left_button = clickable_picture(709, 60, 50, 50, rotateLeftActive, rotateLeftInactive, True)
            self.rotate_right_button = clickable_picture(829, 60, 50, 50, rotateRightActive, rotateRightInactive, True)
            self.attack_button = button("Attack", 709, 180, 50, 50, grey, white, True, "freesansbold.ttf", 15)
            if self.cancel_button:
                self.ship1groen.Active = False
            if self.move_up_button:
                self.move_up_button_pressed = True
                self.move_up_button = False
            elif self.move_up_button_pressed:
                self.ship1groen.Coordinate.Y -= 1
                self.ship1groen.Steps -= 1
                self.move_up_button_pressed = False
            if self.move_down_button:
                self.move_down_button_pressed = True
                self.move_down_button = False
            elif self.move_down_button_pressed:
                self.ship1groen.Coordinate.Y += 1
                self.ship1groen.Steps -= 1
                self.move_down_button_pressed = False
            if self.move_left_button:
                self.move_left_button_pressed = True
                self.move_left_button = False
            elif self.move_left_button_pressed:
                self.ship1groen.Coordinate.X -= 1
                self.ship1groen.Steps -= 1
                self.move_left_button_pressed = False
            if self.move_right_button:
                self.move_right_button_pressed = True
                self.move_right_button = False
            elif self.move_right_button_pressed:
                self.ship1groen.Coordinate.X += 1
                self.ship1groen.Steps -= 1
                self.move_right_button_pressed = False
            if self.rotate_left_button:
                self.rotate_left_button_pressed = True
                self.rotate_left_button = False
            elif self.rotate_left_button_pressed:
                self.ship1groen.rotate(90)
                self.rotate_left_button_pressed = False
                if self.ship1groen.Rotation == 270:
                    self.ship1groen.Coordinate.X -= 1
                    self.ship1groen.Coordinate.Y += 1
                if self.ship1groen.Rotation == 0:
                    self.ship1groen.Coordinate.X += 1
                if self.ship1groen.Rotation == 180:
                    self.ship1groen.Coordinate.Y -= 1
            if self.rotate_right_button:
                self.rotate_right_button_pressed = True
                self.rotate_right_button = False
            elif self.rotate_right_button_pressed:
                self.ship1groen.rotate(-90)
                self.rotate_right_button_pressed = False
                if self.ship1groen.Rotation == 90:
                    self.ship1groen.Coordinate.Y += 1
                if self.ship1groen.Rotation == 270:
                    self.ship1groen.Coordinate.X -= 1
                if self.ship1groen.Rotation == 180:
                    self.ship1groen.Coordinate.X += 1
                    self.ship1groen.Coordinate.Y -= 1
            if self.attack_button:
                self.attack_button_pressed = True
                self.attack_button = False
            elif self.attack_button_pressed:
                self.ship1groen.Stance = "attack"
                self.ship1groen.attack()
                self.stop_attack_button = button("stop attack", 829, 180, 50, 50, grey, white, True, 'freesansbold.ttf', 15)
                if self.stop_attack_button:
                    self.attack_button_pressed = False
        if self.ship2groen.Active:
            self.ship2groen.move()
            screen.blit(ship_stats,(889, 58))
            self.move_up_button = clickable_picture(769, 60, 50, 50, pijlUpActive, pijlUpInactive, True)
            self.move_down_button = clickable_picture(769, 180, 50, 50, pijlDownActive, pijlDownInactive, True)
            self.move_left_button = clickable_picture(709, 120, 50, 50, pijlLeftActive, pijlLeftInactive, True)
            self.move_right_button = clickable_picture(829, 120, 50, 50, pijlRightActive, pijlRightInactive, True)
            self.cancel_button = button("X", 769, 120, 50, 50, grey, white, True)
            self.rotate_left_button = clickable_picture(709, 60, 50, 50, rotateLeftActive, rotateLeftInactive, True)
            self.rotate_right_button = clickable_picture(829, 60, 50, 50, rotateRightActive, rotateRightInactive, True)
            self.attack_button = button("Attack", 709, 180, 50, 50, grey, white, True, "freesansbold.ttf", 15)
            if self.cancel_button:
                self.ship2groen.Active = False
            if self.move_up_button:
                self.move_up_button_pressed = True
                self.move_up_button = False
            elif self.move_up_button_pressed:
                self.ship2groen.Coordinate.Y -= 1
                self.ship2groen.Steps -= 1
                self.move_up_button_pressed = False
            if self.move_down_button:
                self.move_down_button_pressed = True
                self.move_down_button = False
            elif self.move_down_button_pressed:
                self.ship2groen.Coordinate.Y += 1
                self.ship2groen.Steps -= 1
                self.move_down_button_pressed = False
            if self.move_left_button:
                self.move_left_button_pressed = True
                self.move_left_button = False
            elif self.move_left_button_pressed:
                self.ship2groen.Coordinate.X -= 1
                self.ship2groen.Steps -= 1
                self.move_left_button_pressed = False
            if self.move_right_button:
                self.move_right_button_pressed = True
                self.move_right_button = False
            elif self.move_right_button_pressed:
                self.ship2groen.Coordinate.X += 1
                self.ship2groen.Steps -= 1
                self.move_right_button_pressed = False
            if self.rotate_left_button:
                self.rotate_left_button_pressed = True
                self.rotate_left_button = False
            elif self.rotate_left_button_pressed:
                self.ship2groen.rotate(90)
                self.rotate_left_button_pressed = False
                if self.ship2groen.Rotation == 270:
                    self.ship2groen.Coordinate.X -= 2
                    self.ship2groen.Coordinate.Y += 2
                if self.ship2groen.Rotation == 0:
                    self.ship2groen.Coordinate.X += 2
                if self.ship2groen.Rotation == 180:
                    self.ship2groen.Coordinate.Y -= 2
            if self.rotate_right_button:
                self.rotate_right_button_pressed = True
                self.rotate_right_button = False
            elif self.rotate_right_button_pressed:
                self.ship2groen.rotate(-90)
                self.rotate_right_button_pressed = False
                if self.ship2groen.Rotation == 90:
                    self.ship2groen.Coordinate.Y += 2
                if self.ship2groen.Rotation == 270:
                    self.ship2groen.Coordinate.X -= 2
                if self.ship2groen.Rotation == 180:
                    self.ship2groen.Coordinate.X += 2
                    self.ship2groen.Coordinate.Y -= 2
            if self.attack_button:
                self.attack_button_pressed = True
                self.attack_button = False
            elif self.attack_button_pressed:
                self.ship2groen.Stance = "attack"
                self.ship2groen.attack()
                self.stop_attack_button = button("stop attack", 829, 180, 50, 50, grey, white, True, 'freesansbold.ttf', 15)
                if self.stop_attack_button:
                    self.attack_button_pressed = False
        if self.ship3groen.Active:
            self.ship3groen.move()
            screen.blit(ship_stats,(889, 58))
            self.move_up_button = clickable_picture(769, 60, 50, 50, pijlUpActive, pijlUpInactive, True)
            self.move_down_button = clickable_picture(769, 180, 50, 50, pijlDownActive, pijlDownInactive, True)
            self.move_left_button = clickable_picture(709, 120, 50, 50, pijlLeftActive, pijlLeftInactive, True)
            self.move_right_button = clickable_picture(829, 120, 50, 50, pijlRightActive, pijlRightInactive, True)
            self.cancel_button = button("X", 769, 120, 50, 50, grey, white, True)
            self.rotate_left_button = clickable_picture(709, 60, 50, 50, rotateLeftActive, rotateLeftInactive, True)
            self.rotate_right_button = clickable_picture(829, 60, 50, 50, rotateRightActive, rotateRightInactive, True)
            self.attack_button = button("Attack", 709, 180, 50, 50, grey, white, True, "freesansbold.ttf", 15)
            if self.cancel_button:
                self.ship3groen.Active = False
            if self.move_up_button:
                self.move_up_button_pressed = True
                self.move_up_button = False
            elif self.move_up_button_pressed:
                self.ship3groen.Coordinate.Y -= 1
                self.ship3groen.Steps -= 1
                self.move_up_button_pressed = False
            if self.move_down_button:
                self.move_down_button_pressed = True
                self.move_down_button = False
            elif self.move_down_button_pressed:
                self.ship3groen.Coordinate.Y += 1
                self.ship3groen.Steps -= 1
                self.move_down_button_pressed = False
            if self.move_left_button:
                self.move_left_button_pressed = True
                self.move_left_button = False
            elif self.move_left_button_pressed:
                self.ship3groen.Coordinate.X -= 1
                self.ship3groen.Steps -= 1
                self.move_left_button_pressed = False
            if self.move_right_button:
                self.move_right_button_pressed = True
                self.move_right_button = False
            elif self.move_right_button_pressed:
                self.ship3groen.Coordinate.X += 1
                self.ship3groen.Steps -= 1
                self.move_right_button_pressed = False
            if self.rotate_left_button:
                self.rotate_left_button_pressed = True
                self.rotate_left_button = False
            elif self.rotate_left_button_pressed:
                self.ship3groen.rotate(90)
                self.rotate_left_button_pressed = False
                if self.ship3groen.Rotation == 270:
                    self.ship3groen.Coordinate.X -= 2
                    self.ship3groen.Coordinate.Y += 2
                if self.ship3groen.Rotation == 0:
                    self.ship3groen.Coordinate.X += 2
                if self.ship3groen.Rotation == 180:
                    self.ship3groen.Coordinate.Y -= 2
            if self.rotate_right_button:
                self.rotate_right_button_pressed = True
                self.rotate_right_button = False
            elif self.rotate_right_button_pressed:
                self.ship3groen.rotate(-90)
                self.rotate_right_button_pressed = False
                if self.ship3groen.Rotation == 90:
                    self.ship3groen.Coordinate.Y += 2
                if self.ship3groen.Rotation == 270:
                    self.ship3groen.Coordinate.X -= 2
                if self.ship3groen.Rotation == 180:
                    self.ship3groen.Coordinate.X += 2
                    self.ship3groen.Coordinate.Y -= 2
            if self.attack_button:
                self.attack_button_pressed = True
                self.attack_button = False
            elif self.attack_button_pressed:
                self.ship3groen.Stance = "attack"
                self.ship3groen.attack()
                self.stop_attack_button = button("stop attack", 829, 180, 50, 50, grey, white, True, 'freesansbold.ttf', 15)
                if self.stop_attack_button:
                    self.attack_button_pressed = False
        if self.ship4groen.Active:
            self.ship4groen.move()
            screen.blit(ship_stats,(889, 58))
            self.move_up_button = clickable_picture(769, 60, 50, 50, pijlUpActive, pijlUpInactive, True)
            self.move_down_button = clickable_picture(769, 180, 50, 50, pijlDownActive, pijlDownInactive, True)
            self.move_left_button = clickable_picture(709, 120, 50, 50, pijlLeftActive, pijlLeftInactive, True)
            self.move_right_button = clickable_picture(829, 120, 50, 50, pijlRightActive, pijlRightInactive, True)
            self.cancel_button = button("X", 769, 120, 50, 50, grey, white, True)
            self.rotate_left_button = clickable_picture(709, 60, 50, 50, rotateLeftActive, rotateLeftInactive, True)
            self.rotate_right_button = clickable_picture(829, 60, 50, 50, rotateRightActive, rotateRightInactive, True)
            self.attack_button = button("Attack", 709, 180, 50, 50, grey, white, True, "freesansbold.ttf", 15)
            if self.cancel_button == "cancel":
                self.ship4groen.Active = False
            if self.move_up_button:
                self.move_up_button_pressed = True
                self.move_up_button = False
            elif self.move_up_button_pressed:
                self.ship4groen.Coordinate.Y -= 1
                self.ship4groen.Steps -= 1
                self.move_up_button_pressed = False
            if self.move_down_button:
                self.move_down_button_pressed = True
                self.move_down_button = False
            elif self.move_down_button_pressed:
                self.ship4groen.Coordinate.Y += 1
                self.ship4groen.Steps -= 1
                self.move_down_button_pressed = False
            if self.move_left_button:
                self.move_left_button_pressed = True
                self.move_left_button = False
            elif self.move_left_button_pressed:
                self.ship4groen.Coordinate.X -= 1
                self.ship4groen.Steps -= 1
                self.move_left_button_pressed = False
            if self.move_right_button:
                self.move_right_button_pressed = True
                self.move_right_button = False
            elif self.move_right_button_pressed:
                self.ship4groen.Coordinate.X += 1
                self.ship4groen.Steps -= 1
                self.move_right_button_pressed = False
            if self.rotate_left_button:
                self.rotate_left_button_pressed = True
                self.rotate_left_button = False
            elif self.rotate_left_button_pressed:
                self.ship4groen.rotate(90)
                self.rotate_left_button_pressed = False
                if self.ship4groen.Rotation == 270:
                    self.ship4groen.Coordinate.X -= 3
                    self.ship4groen.Coordinate.Y += 3
                if self.ship4groen.Rotation == 0:
                    self.ship4groen.Coordinate.X += 3
                if self.ship4groen.Rotation == 180:
                    self.ship4groen.Coordinate.Y -= 3
            if self.rotate_right_button:
                self.rotate_right_button_pressed = True
                self.rotate_right_button = False
            elif self.rotate_right_button_pressed:
                self.ship4groen.rotate(-90)
                self.rotate_right_button_pressed = False
                if self.ship4groen.Rotation == 90:
                    self.ship4groen.Coordinate.Y += 3
                if self.ship4groen.Rotation == 270:
                    self.ship4groen.Coordinate.X -= 3
                if self.ship4groen.Rotation == 180:
                    self.ship4groen.Coordinate.X += 3
                    self.ship4groen.Coordinate.Y -= 3
            if self.attack_button:
                self.attack_button_pressed = True
                self.attack_button = False
            elif self.attack_button_pressed:
                self.ship4groen.Stance = "attack"
                self.ship4groen.attack()
                self.stop_attack_button = button("stop attack", 829, 180, 50, 50, grey, white, True, 'freesansbold.ttf', 15)
                if self.stop_attack_button:
                    self.attack_button_pressed = False
        self.ship1rood.Coordinate.Update()
        self.ship2rood.Coordinate.Update()
        self.ship3rood.Coordinate.Update()
        self.ship4rood.Coordinate.Update()
        self.ship1groen.Coordinate.Update()
        self.ship2groen.Coordinate.Update()
        self.ship3groen.Coordinate.Update()
        self.ship4groen.Coordinate.Update()
    def draw(self):
        screen.fill((background_blue))
        screen.blit(game_background, (0,0))
        self.buttons()
        self.update()
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
            pygame.mixer.music.stop()
            mainmenu_music.play(-1)
            running = Menu()
    elif running.type == "highscores":
        if running.quitbutton == "quit":
            pygame.mixer.Sound.play(click)
            running = Menu()
    elif running.type == "help1":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Menu()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help1()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Helpr1()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Helpi1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Helpx1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1()
    elif running.type == "helpr1":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Menu()
        elif running.prevbutton == "help":
            pygame.mixer.Sound.play(click)
            running = Help1()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help1()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Helpi1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Helpx1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1()
    elif running.type == "helpi1":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Menu()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help1()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Helpi2()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Helpi1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Helpx1()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Helpi2()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help1()
            running = Helpi2()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Helpi1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Helpx1()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Helpi2()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1()
    elif running.type == "helpi2":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Menu()
        elif running.prevbutton == "help":
            pygame.mixer.Sound.play(click)
            running = Helpi1()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help1()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Helpi1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Helpx1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1()
    elif running.type == "helpx1":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Menu()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help1()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Helpi1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Helpx1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1()

    elif running.type == "help2":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Battleport()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Help2i1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Help2x1()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Help2r1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1g()
    elif running.type == "help2r1":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Battleport()
        elif running.prevbutton == "help":
            pygame.mixer.Sound.play(click)
            running = Help2()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help2()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Help2i1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Help2x1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1()
    elif running.type == "help2i1":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Battleport()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help2()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Help2i2()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Help2i1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Help2x1()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Help2i2()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help2()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1()
    elif running.type == "help2i2":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Battleport()
        elif running.prevbutton == "help":
            pygame.mixer.Sound.play(click)
            running = Help2i1()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help2()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Help2i1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Help2x1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1()
    elif running.type == "help2x1":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Battleport()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help2()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Help2i1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Help2x1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1()
    #cards menu (offensive) cards1
    elif running.type == "cards1":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Menu()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help2()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Help2i1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Help2x1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Cards2()
    #cards menu (defensive) cards2
    elif running.type == "cards2":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Menu()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help2()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Help2i1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Help2x1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Cards3()
        elif running.prevbutton == "help":
            pygame.mixer.Sound.play(click)
            running = Cards1()
    elif running.type == "cards3":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Menu()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help2()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Help2i1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Help2x1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Cards4()
        elif running.prevbutton == "help":
            pygame.mixer.Sound.play(click)
            running = Cards2()

    elif running.type == "cards4":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Menu()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help2()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Help2i1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Help2x1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1()
        elif running.prevbutton == "help":
            pygame.mixer.Sound.play(click)
            running = Cards3()

    #cards menu (in game)
    elif running.type == "cards1g":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Battleport()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help2()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Help2i1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Help2x1()
        elif running.cardbutton == "cards1g":
            pygame.mixer.Sound.play(click)
            running = Cards1g()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Cards2g()
    #cards menu (in game)
    elif running.type == "cards2g":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Battleport()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help2()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Help2i1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Help2x1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1g()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Cards3g()
        elif running.prevbutton == "help":
            pygame.mixer.Sound.play(click)
            running = Cards1g()

            # cards menu (in game)
    elif running.type == "cards3g":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Battleport()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help2()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Help2i1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Help2x1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1g()
        elif running.nextbutton == "next":
            pygame.mixer.Sound.play(click)
            running = Cards4g()
        elif running.prevbutton == "help":
            pygame.mixer.Sound.play(click)
            running = Cards2g()
        #cards menu in game
    elif running.type == "cards4g":
        if running.returnbutton == "return":
            pygame.mixer.Sound.play(click)
            running = Battleport()
        elif running.rulesbutton == "rules1":
            pygame.mixer.Sound.play(click)
            running = Help2()
        elif running.instructionbutton == "instructions1":
            pygame.mixer.Sound.play(click)
            running = Help2i1()
        elif running.extrabutton == "extra":
            pygame.mixer.Sound.play(click)
            running = Help2x1()
        elif running.cardbutton == "cards1":
            pygame.mixer.Sound.play(click)
            running = Cards1g()
        elif running.prevbutton == "help":
            pygame.mixer.Sound.play(click)
            running = Cards3g()

    running.draw()