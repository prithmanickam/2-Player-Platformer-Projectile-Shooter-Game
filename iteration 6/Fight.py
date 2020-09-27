from pygame_functions import *
from pygame.locals import *
import Launcher
import random





#one way to do shooting - can create a bullet object with the following behaviours
class bullet():
    #Initialise the bullet with it's sprite, speed, position, life attribute, directions and size
    def __init__(self,bullet,speed, size = 1):
        self.bullet = bullet
        self.speed = speed
        self.x = 0
        self.y = 0
        self.life = 0
        self.dir = True
        self.size = size


    # When it's fired - update where it is, how it and reset how long it lasts
    def shoot(self, x, y, right):
        self.x = x
        self.y = y
        moveSprite(self.bullet, self.x, self.y, True)
        showSprite(self.bullet)
        self.life = 100
        self.dir = right

        #rotate so it's facin the right way
        if right:
            transformSprite(self.bullet, 0, self.size)
        else:
            transformSprite(self.bullet, 180, self.size)


    #each frame update it's position if it still has life - otherwise hide it.
    def update(self, frame):
        if self.life > 0:
            changeSpriteImage(self.bullet, 0*8 + frame)
            if self.dir:
                self.x += self.speed
            else:
                self.x -= self.speed
            moveSprite(self.bullet, self.x, self.y, True)
            self.life -= 1
        else:
            hideSprite(self.bullet)
            


def checkEdge(direction, playerXpos, screenW, pEdge, scrollRate):
    # check whether it is hitting the screen edge. direction = True for going Right
    if direction:
        if playerXpos > screenW - pEdge:
            playerXpos = screenW - pEdge
        if playerXpos < screenW - pEdge:
            scrollBackground(-scrollRate,0)
    else:
        if playerXpos < (0 + pEdge):
            playerXpos = (0 + pEdge)
        if playerXpos > 0 + pEdge:
            scrollBackground(scrollRate,0)

    return playerXpos


def Game(options, name, scrSize):

    print("\n**********************************************")
    print("In Fight.py with the following settings")
    print("This is a {} round match".format(options.rounds))
    print("Each round is {} minutes long".format(options.time))
    print("Music volume is set to {}".format(options.music))
    print("Sound volume is set to {}".format(options.sound))
    print("**********************************************\n")

    backgrounds = ["back.png", "back.png", "back.png"]
    setAutoUpdate(False)

    screenWidth, screenHeight = scrSize
    screenSize(screenWidth, screenHeight, name= name)
    #setBackgroundColour("dark green")
    setBackgroundImage(random.choice(backgrounds))

    scrollBackground(-80,0) # repositioning the background to centre it.

    label = makeLabel(name, 80, 275, 10,'red','zapfino', "clear", True, screenWidth)
    showLabel(label)
    



    #load the sprite, tell it how many frames so that it is split equally
    player1 = makeSprite("boyninjarun.png", 24)
    player2 = makeSprite("girlninjarun.png", 24)

    #trying to load up projectiles 
    proj1Sprite = makeSprite("projectile1.3.png", 8)
##  proj2 = makeSprite("projectile2", 8)
    p1Proj = bullet(proj1Sprite, 50, 0.5)

        
    onGround = 700
    scrollRate = 6
    walkRate = 6
    player1Xpos = 800
    player1Ypos = onGround
    player2Xpos = 200
    jumpSteps = 10
    P1Left = options.keysP1[0]
    P1Right = options.keysP1[1]
    P1Jump = options.keysP1[2]
    P1shoot = options.keysP1[3]
    P2Left = options.keysP2[0]
    P2Right = options.keysP2[1]
    P2Jump = options.keysP2[2]

    p1JumpSteps = jumpSteps
    p1IsJumping = False

    # position the sprite, by it's centre. (True)
    moveSprite(player1, player1Xpos, onGround, True)
    showSprite(player1)
    # postion and show the computer sprite
    moveSprite(player2, player2Xpos, onGround, True)
    showSprite(player2)


    pEdge = player1.rect.width / 2
    cEdge = player2.rect.width / 2

    screenW, screenH = pygame.display.get_surface().get_size()


    nextFrame = clock()

    frame = 0

    right = True



    while True:

        # Making sure our animation frame comes every 80 miliseconds.
        if clock() > nextFrame:
            frame = (frame + 1) % 8
            #nextFrame = nextFrame + 80
            nextFrame += 80


        if keyPressed("x"):
            killSprite(player1)
            killSprite(player2)
            killSprite(p1Proj)
            return False, "Player WON!!!!!!!"



        if keyPressed(P1Right):
            right = True
            player1Xpos += walkRate
            player1Xpos = checkEdge(True, player1Xpos, screenW, pEdge, scrollRate)
            changeSpriteImage(player1, 0*8 + frame)
            #moveSprite(player, playerXpos, onGround, True)
            if touching(player1, player2):
                player1Xpos = player1Xpos - walkRate - 5
            
        
        elif keyPressed(P1Left):
            right = False
            player1Xpos -= walkRate
            player1Xpos = checkEdge(False, player1Xpos, screenW, pEdge, scrollRate)
            changeSpriteImage(player1, 2*8 + frame)
            #moveSprite(player, player1Xpos, onGround, True)
            if touching(player1, player2):
                player1Xpos = player1Xpos + walkRate + 5
            
        else:
            # This will be the idle animation.
            changeSpriteImage(player1, 1*8 + 5)

        
        if not p1IsJumping:

        #If the player isn't currently jumping, then check to see if they pressed the jump button.
        #Otherwise, ignore any jump input.
            if keyPressed(P1Jump):
                p1IsJumping = True

        else:
            # Jump using a quadratic equation - giving a nice curve.
            if p1JumpSteps >= -jumpSteps:
                neg = 1
                if p1JumpSteps < 0:
                    neg = -1
                player1Ypos -= 0.5 * (p1JumpSteps ** 2)  * neg
                p1JumpSteps -= 1
            else:
                p1IsJumping = False
                p1JumpSteps = jumpSteps


        moveSprite(player1, player1Xpos, player1Ypos, True)



        #shooting for player 1
        if keyPressed(P1shoot):
            p1Proj.shoot(player1Xpos, player1Ypos, right)
        p1Proj.update(frame)



        if keyPressed(P2Right):
            player2Xpos += walkRate
            player2Xpos = checkEdge(True, player2Xpos, screenW, cEdge, scrollRate)
            changeSpriteImage(player2, 0*8 + frame)
            moveSprite(player2, player2Xpos, onGround, True)
            if touching(player1, player2):
                player2Xpos = player2Xpos - walkRate - 5
        
        elif keyPressed(P2Left):
            player2Xpos -= walkRate
            player2Xpos = checkEdge(False, player2Xpos, screenW, cEdge, scrollRate)
            changeSpriteImage(player2, 2*8 + frame)
            moveSprite(player2, player2Xpos, onGround, True)
            if touching(player1, player2):
                player2Xpos = player2Xpos + walkRate + 5
        
        else:
            # This will be the idle animation.
            changeSpriteImage(player2, 1*8 + 5)


        # Keeps the frame rate set to 120 - AND allows exit from pygame
        tick(120)
        updateDisplay()


if __name__ == '__main__':
    Launcher.main()

