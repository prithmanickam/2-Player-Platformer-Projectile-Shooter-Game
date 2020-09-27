from pygame_functions import *
from pygame.locals import *
import Launcher
import random
import math #so that I can create a timer

class Bullet():
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
        self.life = 50
        self.dir = right

        #rotate so it's facing the right way
        if right:
            transformSprite(self.bullet, 0, self.size)
        else:
            transformSprite(self.bullet, 180, self.size)

    def kill(self):
        killSprite(self.bullet)

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
            return True
        else:
            hideSprite(self.bullet)
            return False
            
class Player():
    def __init__(self, body, bullet, startPos, screenW, scrollRate, keys):
        self.body = body
        self.bullet = bullet
        self.edge = body.rect.width / 2
        self.x, self.y = startPos
        self.right = True
        self.isJumping = False
        self.isFiring = False
        self.screenW = screenW
        self.scrollRate = scrollRate
        self.jumpStep = 10
        self.walkRate = 6
        self.L = keys[0]
        self.R = keys[1]
        self.J = keys[2]
        self.S = keys[3]
        self.otherPlayer = None

        self.update(1)
        showSprite(self.body)


    def walk(self, frame, direction):
        self.right = direction
        if self.right:
            self.x += self.walkRate
            self.collisionChecks()
        else:
            self.x -= self.walkRate
            self.collisionChecks()
        if self.right:
            changeSpriteImage(self.body, 0*8 + frame)
        else:
            changeSpriteImage(self.body, 2*8 + frame)


    def collisionChecks(self):
        # check whether it is hitting the screen edge. direction = True for going Right
        if self.right:
            if self.x > self.screenW - self.edge:
                self.x = self.screenW - self.edge
            if self.x < self.screenW - self.edge:
                scrollBackground(-self.scrollRate,0)
        else:
            if self.x < self.edge:
                self.x = self.edge
            if self.x > self.edge:
                scrollBackground(self.scrollRate,0)

        self.touching()

    def touching(self):
        if touching(self.body, self.otherPlayer.body):
            if self.right:
                self.x +=  -self.walkRate - 5
            else:
                self.x +=  self.walkRate + 5


        if self.otherPlayer.bullet:
        
            if touching(self.otherPlayer.bullet.bullet,self.body):
               print("damage dealt = 10")

    def stationary(self):
        changeSpriteImage(self.body, 1*8 + 5)

    def jump(self):
        if not self.isJumping: 
            self.isJumping = True

    def shoot(self):
        if not self.isFiring:    
            self.bullet.shoot(self.x, self.y, self.right)
            self.isFiring = True
        
    def kill(self):
        killSprite(self.body)
        self.bullet.kill()

    def addPlayer(self, player):
        self.otherPlayer = player

    def update(self, frame):
        moveSprite(self.body, self.x, self.y, True)
        if self.isJumping:
            if self.jumpStep >= -10:
                neg = 1
                if self.jumpStep < 0:
                    neg = -1
                self.y -= 0.5 * (self.jumpStep ** 2)  * neg
                self.jumpStep -= 1
            else:
                self.isJumping = False
                self.jumpStep = 10
        if self.isFiring:
            self.isFiring = self.bullet.update(frame)


def Game(options, name, scrSize):

    print("\n**********************************************")
    print("In Fight.py with the following settings")
    print("This is a {} round match".format(options.rounds))
    print("Each round is {} minutes long".format(options.time))
    print("Music volume is set to {}".format(options.music))
    print("Sound volume is set to {}".format(options.sound))
    print("**********************************************\n")


    #get time from options. It's currently in minutes, here it converts it to seconds.

    gameTimer = options.time * 60

    # update it in the game loop further down.

    backgrounds = ["back.png", "back.png", "back.png"]
    setAutoUpdate(False)

    screenW, screenH = scrSize
    screenSize(screenW, screenH, name= name)
    setBackgroundImage(random.choice(backgrounds))
    scrollBackground(-80,0) # repositioning the background to centre it.
    label = makeLabel(name, 80, 275, 10,'green','zapfino', "clear", True, screenW)
    showLabel(label)
    
    label2 = makeLabel('Timer:0' , 50, 255, 100,'red','zapfino', "clear", True, screenW)
    showLabel(label2)


    p1Proj = Bullet(makeSprite("projectile1.3.png", 8), 50, 0.5)
    p2Proj = Bullet(makeSprite("projectile1.3.png", 8), 50, 0.5)

    scrollRate = 6
    
    #Create some players - see the class for attribute definitions
    player1 = Player(makeSprite("boyninjarun.png", 24), p1Proj, (800, 700), screenW, scrollRate, options.keysP1)
    player2 = Player(makeSprite("girlninjarun.png", 24), p2Proj, (200, 700), screenW, scrollRate, options.keysP2)
    #Add references to each other for collision purposes
    player1.addPlayer(player2)
    player2.addPlayer(player1)

    seconds = clock()
    nextFrame = clock()
    frame = 0
    right = True

    while True:

        # Making sure the animation frame comes every 80 miliseconds.
        if clock() > nextFrame:
            frame = (frame + 1) % 8
            nextFrame += 80


        # Timer:
        if clock() > seconds: 
            gameTimer = gameTimer - 1
            if gameTimer < 1:
                gameTimer = 0
                print("Game has run out of time... what next? :)")
            changeLabel(label2, "Timer:{}".format(gameTimer))
            seconds += 1000 #Clock counts in 1000 miliseconds. So add 1000 each time.

        #Quick temp exit from game - this will be replaced by a win condition.
        if keyPressed("x"):
            player1.kill()
            player2.kill()
            return False, "Player WON!!!!!!!"

        #Player One movement control - Left/Right and stationary are lumped together so you can't do both
        #at the same time.
        if keyPressed(player1.R):
            player1.walk(frame, True)
        elif keyPressed(player1.L):
            player1.walk(frame, False)
        else:
            player1.stationary()
        #Jumping and shooting kept seperate so they can be done at the same time as walking
        if keyPressed(player1.J):
            player1.jump()
        if keyPressed(player1.S):
            player1.shoot()
           

        #Player Two movement control
        if keyPressed(player2.R):
            player2.walk(frame, True)
        elif keyPressed(player2.L):
            player2.walk(frame, False)
        else:
            player2.stationary()

        if keyPressed(player2.J):
            player2.jump()
        if keyPressed(player2.S):
            player2.shoot()
           

        #Update the players so they're in the right places
        player1.update(frame)
        player2.update(frame)

        tick(120)
        updateDisplay()


if __name__ == '__main__':
    Launcher.main()

