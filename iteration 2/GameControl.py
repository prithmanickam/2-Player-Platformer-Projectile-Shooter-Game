import pygame
from pygame.locals import *
import FrontEnd as f
import BackEnd as b
import fight as g

WHITE = 250,250,250

#This is where the main loops are... main game control


# Our game class that is instantiated in the Luancher
class Game():
	
	# Initialise what we need
	def __init__(self, screenSize, name):
		self.screen = f.Screen(screenSize, name)
		# A Clock is needed to limit our framerate
		self.clock = pygame.time.Clock()
		# Options loaded in
		self.options = f.OptionConfigs()

		self.fightOptions = None



	# Our mainloop that controls the flow of the whole game
	def mainLoop(self):

		# Make sure we can get out of the game.
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					quit()

			self.menuLoop()

			self.gameLoop()

			self.resultsLoop()


	# Our menuLoop that controls the flow of the menus - other loops below are self explanatory :)
	def menuLoop(self):
		menu = b.Pages()
		currentPage = menu.getPage()
		position = 0
		options = menu.getOptions(currentPage)
		currentOption = options[position]
		numberOptions = len(options) - 1 # used to constrain the selection

		play = False

		print(options)
		print("Page object: ", currentPage.name)
		
		# read the event queue for key presses.
		while True:

			for event in pygame.event.get():
				if event.type == QUIT:
					quit()
				elif event.type == KEYDOWN:
					if event.key == K_UP:
						position = position - 1
						if position < 0: # Ensure that we can't go out of bounds
							position = 0
						print("Up")
					elif event.key == K_DOWN:
						position = position + 1
						if position > numberOptions: # ensure we don't go below our list...
							position = numberOptions
						print("Down")
					elif event.key == K_RETURN:
						menu.last = menu.current
						menu.current = options[position] # Using a string to switch the page
						currentPage = menu.getPage()
						position = 0
						options = menu.getOptions(currentPage)
						currentOption = options[position]
						numberOptions = len(options) - 1
						self.screen.refreshText()
						print("Enter")
					elif event.key == K_ESCAPE:
						print("Escape")
						play = True
			if play:
				self.fightOptions = "Yay"
				return # A neat way of moving into the game. We may decide that we want to send a list of config data instead
			# Update the screen so we can see that we're doing something
			currentOption = options[position]
			self.screen.setTitleText(currentPage.name)
			self.screen.setOptionText(options, currentOption)
			self.screen.refreshText()

	def gameLoop(self):
		
		self.screen.whiteout() # Clear the screen
		fight = g.Game()

		dead = False
		while not dead:
			dead = fight.mainLoop(g.initialisePygame())

	

	def resultsLoop(self):
				
		self.screen.setTitleText("ResultsLoop")

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

        
			self.screen.refreshText()



