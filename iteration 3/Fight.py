from pygame_functions import *
from pygame.locals import *


def Game():

	playerWalkSprite = "boyninjarun.png"
	screenSize(1000,800)
	setBackgroundColour("dark green")
	#load the sprite, tell it how many frames so that it is split equally
	player = makeSprite(playerWalkSprite, 24)
	computer = makeSprite("girlninjarun.png", 24)
	walkRate = 15
	playerXpos = 200
	computerXpos = 800

	# position the sprite, by it's centre. (True)
	moveSprite(player, playerXpos, 600, True)
	showSprite(player)
	# postion and show the computer sprite
	moveSprite(computer, computerXpos, 600, True)
	showSprite(computer)

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
			return True

		if keyPressed("right"):
			playerXpos += walkRate
			changeSpriteImage(player, 0*8 + frame)
			moveSprite(player, playerXpos, 600, True)
		elif keyPressed("left"):
			playerXpos -= walkRate
			changeSpriteImage(player, 2*8 + frame)
			moveSprite(player, playerXpos, 600, True)
		elif keyPressed("up"):
			changeSpriteImage(player, 3*8 + frame)
		else:
			# This will be the idle animation.
			changeSpriteImage(player, 1*8 + 5)

		if keyPressed("d"):
			computerXpos += walkRate
			changeSpriteImage(computer, 0*8 + frame)
			moveSprite(computer, computerXpos, 600, True)
		elif keyPressed("a"):
			computerXpos -= walkRate
			changeSpriteImage(computer, 2*8 + frame)
			moveSprite(computer, computerXpos, 600, True)
		else:
			# This will be the idle animation.
			changeSpriteImage(computer, 1*8 + 5)


		# Keeps the frame rate set to 120 - AND allows exit from pygame
		tick(120)
