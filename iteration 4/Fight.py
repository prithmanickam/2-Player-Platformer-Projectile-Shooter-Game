from pygame_functions import *
from pygame.locals import *
import Launcher
import random


def Game(options, name):



	print("This is a {} round match".format(options.rounds))
	print("Each round is {} minutes long".format(options.time))
	print("Music volume is set to {}".format(options.music))
	print("Sound volume is set to {}".format(options.sound))

	backgrounds = ["back.png", "back.png", "back.png"]
	setAutoUpdate(False)

	#playerWalkSprite = "links.gif"
	playerWalkSprite = "boyninjarun.png"
	screenSize(1000,800, name= name)
	#setBackgroundColour("dark green")
	setBackgroundImage(random.choice(backgrounds))

	scrollBackground(-80,0) # repositioning the background to centre it.

	label = makeLabel(name, 80, 275, 10,'red','zapfino', "clear", True, 1000)
	showLabel(label)
	



	#load the sprite, tell it how many frames so that it is split equally
	player = makeSprite(playerWalkSprite, 24)
	computer = makeSprite("girlninjarun.png", 24)
	onGround = 700
	scrollRate = 6
	walkRate = 15
	playerXpos = 200
	computerXpos = 800
	P1Left = options.keysP1[0]
	P1Right = options.keysP1[1]

	# position the sprite, by it's centre. (True)
	moveSprite(player, playerXpos, onGround, True)
	showSprite(player)
	# postion and show the computer sprite
	moveSprite(computer, computerXpos, onGround, True)
	showSprite(computer)


	pEdge = player.rect.width / 2
	screenW, screenH = pygame.display.get_surface().get_size()


	nextFrame = clock()

	frame = 0

	while True:

		# Making sure our animation frame comes every 80 miliseconds.
		if clock() > nextFrame:
			frame = (frame + 1) % 8
			#nextFrame = nextFrame + 80
			nextFrame += 80


		if keyPressed("x"):
			killSprite(player)
			killSprite(computer)
			return False, "Player WON!!!!!!!"



		if keyPressed(P1Right):
			playerXpos += walkRate
			if playerXpos > screenW - pEdge:
				playerXpos = screenW - pEdge
			changeSpriteImage(player, 0*8 + frame)
			moveSprite(player, playerXpos, onGround, True)
			if playerXpos < screenW - pEdge:
				scrollBackground(-scrollRate,0)  
		
		elif keyPressed(P1Left):
			playerXpos -= walkRate
			if playerXpos < (0 + pEdge):
				playerXpos = (0 + pEdge)
			changeSpriteImage(player, 2*8 + frame)
			moveSprite(player, playerXpos, onGround, True)
			if playerXpos > 0 + pEdge:
				scrollBackground(scrollRate,0)  
		
		else:
			# This will be the idle animation.
			changeSpriteImage(player, 1*8 + 5)



		if keyPressed(options.keysP2[1]):
			computerXpos += walkRate
			changeSpriteImage(computer, 0*8 + frame)
			moveSprite(computer, computerXpos, onGround, True)
		
		elif keyPressed(options.keysP2[0]):
			computerXpos -= walkRate
			changeSpriteImage(computer, 2*8 + frame)
			moveSprite(computer, computerXpos, onGround, True)
		
		else:
			# This will be the idle animation.
			changeSpriteImage(computer, 1*8 + 5)




		# We need to ensure that the characters are facing each other. Either with seperate left and right animations.
		# or, even better, using a 'flip' function.

		# Keeps the frame rate set to 120 - AND allows exit from pygame
		tick(120)
		updateDisplay()


if __name__ == '__main__':
	Launcher.main()

