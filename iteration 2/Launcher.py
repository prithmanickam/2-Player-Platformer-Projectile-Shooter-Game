import pygame
from pygame.locals import *
import GameControl as g
import BackEnd as b

# initialising pygame, set screen res and create and instance of the game.
def main():
	# Pygame initialisation
	pygame.init()
	

	screenSize = width, height = 1000, 800

	# create an instance of the game
	game = g.Game(screenSize, "Street Figher")

	# run the mainloop
	game.mainLoop()




#if this is the program that is run then do this:
if __name__ == "__main__":
	main()

