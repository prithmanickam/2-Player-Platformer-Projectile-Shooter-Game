import pygame
from pygame.locals import *
import GameControl as g


# initialising pygame, set screen res and create and instance of the game.
def main():
	# Pygame initialisation
	pygame.init()
	

	screenSize = width, height = 960, 940

	# create an instance of our game
	game = g.Game(screenSize, "Street Figher")

	# run the mainloop
	game.mainLoop()




#if this is the program that is run then do this:
if __name__ == "__main__":
	main()


	
