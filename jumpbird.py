import random # For generating random numbers
import sys #To exit the program
import pygame #pip install pygame
from pygame.locals import * 
FPS = 35
SCREENWIDTH = 601
SCREENHEIGHT = 520
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'C:/Users/jitendra kumar saini/Pictures/flippinbird/bird.png'
BACKGROUND = 'C:/Users/jitendra kumar saini/Pictures/flippinbird/background.jpg'
WALL = 'C:/Users/jitendra kumar saini/Pictures/flippinbird/pipe.png'


def welcomeScreen():

    playery = int(SCREENWIDTH/5)
    playerx = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playery = int(SCREENWIDTH/5)
    playerx = int(SCREENWIDTH/2)
    basex = 0

    # Create 2 pipes for blitting on the screen
    newwall1 = getRandomwall()
    newwall2 = getRandomwall()

    # List of upper pipes
    rightwall = [
        {'y': SCREENWIDTH+200, 'x':newwall1[0]['x']},
        {'y': SCREENWIDTH+200+(SCREENWIDTH/2), 'x':newwall2[0]['x']},
    ]
    # List of lower pipes
    leftwall = [
        {'y': SCREENWIDTH+200, 'x':newwall1[1]['x']},
        {'y': SCREENWIDTH+200+(SCREENWIDTH/2), 'x':newwall2[1]['x']},
    ]

    wallVelY = -4

    playerVelX = -9
    playerMaxVelX = 10
    playerMinVelX = -8
    playerAccX = 1

    playerJumpAccv = -8 # velocity while jumping
    playerJumped = False # It is true only when the bird is jumping


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playerx > 0:
                    playerVelX = playerJumpAccv
                    playerJumped = True
                    GAME_SOUNDS['download (4)'].play()


        crashTest = isCollide(playerx, playery, rightwall, leftwall) # This function will return true if the player is crashed
        if crashTest:
            return     

        #check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in rightwall:
            pipeMidPos = pipe['y'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                print(f"Your score is {score}") 
                GAME_SOUNDS['download (2)'].play()

        if playerVelX <playerMaxVelX and not playerJumped:
            playerVelX += playerAccX

        if playerJumped:
            playerJumped = False            
        playerHeight = GAME_SPRITES['player'].get_height()
        playerx = playerx + min(playerVelX, GROUNDY - playerx - playerHeight)

        # Moving Pipes
        for rightwall, leftwall in zip(rightwall, leftwall):
            rightwall['y'] += wallVelY
            leftwall['y'] += wallVelY

        # Adding Pipes
        if 0<rightwall[0]['y']<5:
            newpipe = getRandomwall()
            rightwall.append(newpipe[0])
            leftwall.append(newpipe[1])

        # Removing Pipes
        if rightwall[0]['y'] < -GAME_SPRITES['wall'][0].get_width():
            rightwall.pop(0)
            leftwall.pop(0)
        
        # Blitting The Sprites
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for rightwall, leftwall in zip(rightwall, leftwall):
            SCREEN.blit(GAME_SPRITES['wall'][0], (rightwall['y'], rightwall['x']))
            SCREEN.blit(GAME_SPRITES['wall'][1], (leftwall['y'], leftwall['x']))

        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery> GROUNDY - 25  or playery<0:
        GAME_SOUNDS['download (1)'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['download (1)'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['download (1)'].play()
            return True

    return False

def getRandomPipe():
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper Pipe
        {'x': pipeX, 'y': y2} #lower Pipe
    ]
    return pipe
if __name__ == "__main__":
    pygame.init() # Initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Jumping Bird by JITENDRA')
    GAME_SPRITES['numbers'] = ( 
        pygame.image.load('C:/Users/jitendra kumar saini/Pictures/flippinbird/download.png').convert_alpha(),
        pygame.image.load('C:/Users/jitendra kumar saini/Pictures/flippinbird/download (1).png').convert_alpha(),
        pygame.image.load('C:/Users/jitendra kumar saini/Pictures/flippinbird/download (2).png').convert_alpha(),
        pygame.image.load('C:/Users/jitendra kumar saini/Pictures/flippinbird/download (3).png').convert_alpha(),
        pygame.image.load('C:/Users/jitendra kumar saini/Pictures/flippinbird/download (4).png').convert_alpha(),
        pygame.image.load('C:/Users/jitendra kumar saini/Pictures/flippinbird/download (5).png').convert_alpha(),
        pygame.image.load('C:/Users/jitendra kumar saini/Pictures/flippinbird/download (6).png').convert_alpha(),
        pygame.image.load('C:/Users/jitendra kumar saini/Pictures/flippinbird/download (7).png').convert_alpha(),
        pygame.image.load('C:/Users/jitendra kumar saini/Pictures/flippinbird/download (8).png').convert_alpha(),
        pygame.image.load('C:/Users/jitendra kumar saini/Pictures/flippinbird/download (9).png').convert_alpha(),
    
    )

    GAME_SPRITES['message'] =pygame.image.load('C:/Users/jitendra kumar saini/Pictures/flippinbird/T_P-removebg-preview-removebg-preview.png').convert_alpha()
    GAME_SPRITES['base'] =pygame.image.load('C:/Users/jitendra kumar saini/Pictures/flippinbird/base2.png').convert_alpha()
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( WALL).convert_alpha(), 180), 
    pygame.image.load(WALL).convert_alpha()
    )

    # Game sounds
    GAME_SOUNDS['download'] = pygame.mixer.Sound('C:/Users/jitendra kumar saini/Music/flippingbird/download.wav')
    GAME_SOUNDS['download (1)'] = pygame.mixer.Sound('C:/Users/jitendra kumar saini/Music/flippingbird/download (1).wav')
    GAME_SOUNDS['download (2)'] = pygame.mixer.Sound('C:/Users/jitendra kumar saini/Music/flippingbird/download (2).wav')
    GAME_SOUNDS['download (3)'] = pygame.mixer.Sound('C:/Users/jitendra kumar saini/Music/flippingbird/download (3).wav')
    GAME_SOUNDS['download (4)'] = pygame.mixer.Sound('C:/Users/jitendra kumar saini/Music/flippingbird/download (4).wav') 

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen()
        mainGame() 