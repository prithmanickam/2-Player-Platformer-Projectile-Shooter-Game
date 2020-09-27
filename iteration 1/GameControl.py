import pygame
from pygame.locals import *
import FrontEnd as f
import BackEnd as b

#This is where the main loops are - main game control

# game class that is instantiated in the Launcher
class Game():
	
	# Initialise what is needed
	def __init__(self, screenSize, name):
		self.screen = f.Screen(screenSize, name)
		# A Clock is needed to limit the framerate
		self.clock = pygame.time.Clock()
		# Options loaded in
		self.options = f.OptionConfigs()



	# The mainloop that controls the flow of the whole game
	def mainLoop(self):

		# Make sure it is possible to exit the game.
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					quit()

			self.menuLoop()

			self.gameLoop()

			self.resultsLoop()


	# menuLoop controls the flow of the menus
	def menuLoop(self):
		
		# read the event queue for key presses.
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					quit()
				elif event.type == KEYDOWN:
					print("MenuDOWN")
					if event.key == K_LEFT:
						print("Left")
					elif event.key == K_RIGHT:
						print("Right")
					elif event.key == K_ESCAPE:
						return
				elif event.type == KEYUP:
					print("MenuUP")

        	# Update the screen
			self.screen.refreshText("MainLoop")

	def gameLoop(self):
		
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					quit()
				elif event.type == KEYDOWN:
					print("MenuDOWN")
					if event.key == K_LEFT:
						print("Left")
					elif event.key == K_RIGHT:
						print("Right")
					elif event.key == K_ESCAPE:
						return
				elif event.type == KEYUP:
					print("MenuUP")

			self.screen.refreshText("GameLoop")

	

	def resultsLoop(self):
		
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					quit()
				elif event.type == KEYDOWN:
					print("MenuDOWN")
					if event.key == K_LEFT:
						print("Left")
					elif event.key == K_RIGHT:
						print("Right")
					elif event.key == K_ESCAPE:
						return
				elif event.type == KEYUP:
					print("MenuUP")

			self.screen.refreshText("ResultLoop")



