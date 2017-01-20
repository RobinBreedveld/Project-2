import pygame
import time
import random
pygame.init()

display_height = 767
display_width = round((display_height/9)*16)


black   = (0,0,0)
white   = (255,255,255)
red     = (255,0,0)
green   = (0,255,0)
blue    = (0,0,255)
grey    = (128,128,128)
f_grey  = (225,225,225)
boat_width = 113
sblue   =  (25,25,112)


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Battleport')
clock= pygame.time.Clock()

boatImg = pygame.image.load('C:/Python34/Scripts/boatfinal2.png')
background1 = pygame.image.load('C:/Python34/Scripts/BG1.jpg')
logo1 = pygame.image.load('C:/Python34/Scripts/logo1.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text,(0,0))

def blockade(blockx,blocky,thingw,thingh,color):
    pygame.draw.rect(gameDisplay, color, [blockx,blocky, thingw,thingh])

def background(x,y):
    gameDisplay.blit(background1,(x,y))

def logo(x,y):
    gameDisplay.blit(logo,(x,y))

def boat(x,y):
    gameDisplay.blit(boatImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',60)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('Crashed, try again')




def game_intro():
    
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(grey)
        gameDisplay.blit(background1,(0,0))
        gameDisplay.blit(logo1,((display_width * 0.33),(display_height * 0.2)))
        largeText = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf, TextRect = text_objects("Battleport", largeText)
        TextRect.center = ((display_width*0.5),(display_height*0.1))
        gameDisplay.blit(TextSurf, TextRect)

        #buttons
        mouse = pygame.mouse.get_pos()
        #print(mouse)
        if (display_width * 0.7)+300 > mouse[0] > (display_width * 0.7) and 150+70 > mouse[1] > 150:
            pygame.draw.rect(gameDisplay,f_grey,((display_width * 0.7),150,300,70))
        else:
            pygame.draw.rect(gameDisplay,white,((display_width * 0.7),150,300,70))

        if (display_width * 0.7)+300 > mouse[0] > (display_width * 0.7) and 250+70 > mouse[1] > 250:
            pygame.draw.rect(gameDisplay,f_grey,((display_width * 0.7),250,300,70))
        else:
            pygame.draw.rect(gameDisplay,white,((display_width * 0.7),250,300,70))

        if (display_width * 0.7)+300 > mouse[0] > (display_width * 0.7) and 350+70 > mouse[1] > 350:
            pygame.draw.rect(gameDisplay,f_grey,((display_width * 0.7),350,300,70))
        else:
            pygame.draw.rect(gameDisplay,white,((display_width * 0.7),350,300,70))

        if (display_width * 0.7)+300 > mouse[0] > (display_width * 0.7) and 450+70 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay,f_grey,((display_width * 0.7),450,300,70))
        else:
            pygame.draw.rect(gameDisplay,white,((display_width * 0.7),450,300,70))

        if (display_width * 0.7)+300 > mouse[0] > (display_width * 0.7) and 550+70 > mouse[1] > 550:
            pygame.draw.rect(gameDisplay,f_grey,((display_width * 0.7),550,300,70))
        else:
            pygame.draw.rect(gameDisplay,white,((display_width * 0.7),550,300,70))

        if (display_width * 0.7)+300 > mouse[0] > (display_width * 0.7) and 650+70 > mouse[1] > 650:
            pygame.draw.rect(gameDisplay,f_grey,((display_width * 0.7),650,300,70))
        else:
            pygame.draw.rect(gameDisplay,white,((display_width * 0.7),650,300,70))

        if (display_width * 0.87)+150 > mouse[0] > (display_width * 0.87) and 30+35 > mouse[1] > 30:
            pygame.draw.rect(gameDisplay,f_grey,((display_width * 0.87),30,150,35))
        else:
            pygame.draw.rect(gameDisplay,white,((display_width * 0.87),30,150,35))

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Start game", smallText)
        TextRect.center = ( ((display_width * 0.7)+ (300/2)), (150+(70/2))   )
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Load game", smallText)
        TextRect.center = ( ((display_width * 0.7)+ (300/2)), (250+(70/2))   )
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Highscores", smallText)
        TextRect.center = ( ((display_width * 0.7)+ (300/2)), (350+(70/2))   )
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Options", smallText)
        TextRect.center = ( ((display_width * 0.7)+ (300/2)), (450+(70/2))   )
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Help", smallText)
        TextRect.center = ( ((display_width * 0.7)+ (300/2)), (550+(70/2))   )
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Exit game", smallText)
        TextRect.center = ( ((display_width * 0.7)+ (300/2)), (650+(70/2))   )
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf, TextRect = text_objects("|Placeholder| back", smallText)
        TextRect.center = ( ((display_width * 0.87)+ (150/2)), (30+(35/2))   )
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(50)

def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.3)

    x_change = 0

    blockade_startx = random.randrange(0, display_width)
    blockade_starty = -600
    blockade_speed = 4
    blockade_width = 100
    blockade_height = 100

    dodged = 0

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            #print(event)
        x += x_change
        gameDisplay.fill(white)

        #def blockade(blockx,blocky,thingw,thingh,color):
        blockade(blockade_startx, blockade_starty, blockade_width, blockade_height, red)
        blockade_starty += blockade_speed


        boat(x,y)
        things_dodged(dodged)
        if x > display_width - boat_width or x < 0:
            crash()
        if blockade_starty > display_height:
            blockade_starty = 0 - blockade_height
            blockade_startx = random.randrange(0,display_width)
            dodged += 1
            #blockade_speed += 1



        
        if y < blockade_starty+blockade_height:
            print('y crossover')

            if x > blockade_startx and x < blockade_startx+blockade_width or x +boat_width > blockade_startx and x + boat_width < blockade_startx + blockade_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(50)

game_intro()
game_loop()
pygame.quit()
quit()




