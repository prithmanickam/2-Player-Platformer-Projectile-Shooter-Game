import pygame
from pygame.locals import *
import GameControl as g
import BackEnd as b

# initialising pygame, set screen res and create an instance of the game.
def main():
	# Pygame initialisation
	pygame.init()
	

	screenSize = width, height = 1280, 720

	# create an instance of our game
	
	game = g.Game(screenSize, "Anime Fighter", "Colonna MT")
	#game = g.Game(screenSize, "BashBashBong")
	#game = g.Game(screenSize, "Street Fighter", "Arial")
	
	# run the mainloop
	game.mainLoop()




#if this is the program that is run then do this:
if __name__ == "__main__":
	#print(pygame.font.get_fonts())
	main()


	
