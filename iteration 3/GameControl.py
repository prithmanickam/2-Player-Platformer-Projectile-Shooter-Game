import pygame
from pygame.locals import *
import FrontEnd as f
import BackEnd as b
import Fight

WHITE = 250,250,250

#This is where the main loops are... main game control


# game class that is instantiated in the Launcher
class Game():
	
	# Initialise what we need
	def __init__(self, screenSize, name):
		self.screen = f.Screen(screenSize, name)
		# A Clock is needed to limit our framerate
		self.clock = pygame.time.Clock()
		# Options loaded in
		self.options = f.OptionConfigs()

		self.fightOptions = None


	# mainloop that controls the flow of the whole game
	def mainLoop(self):

		# Make sure it is possible to get out of the game.
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					quit()

			self.menuLoop()

			self.gameLoop()

			self.resultsLoop()


	# menuLoop that controls the flow of the menus
	def menuLoop(self):

		print("Entering Menu Loop")

		menu = b.Pages()
		position = 0		
		play = False

		# read the event queue for key presses.
		while True:
			#options = menu.currentPage.connectedPageNameStrings
			numberOptions = len(menu.currentPage.connectedPages) - 1 # used to constrain the selection
			

			for event in pygame.event.get():
				if event.type == QUIT:
					quit()
				elif event.type == KEYDOWN:
					if event.key == K_UP:
						menu.currentPage.connectedPages[position].highlightOff()
						position = position - 1
						if position < 0: # Ensure that it can't go out of bounds
							position = 0
					elif event.key == K_DOWN:
						menu.currentPage.connectedPages[position].highlightOff()
						position = position + 1
						if position > numberOptions: # ensure it doesn't go below the list
							position = numberOptions
					elif event.key == K_LEFT:
						if menu.currentPage.connectedFrom:
							menu.currentPage = menu.currentPage.connectedFrom
							position = 0
					elif event.key == K_RETURN:
						menu.currentPage.connectedPages[position].highlightOff()
						menu.currentPage = menu.currentPage.connectedPages[position]
						position = 0
					elif event.key == K_ESCAPE:
						play = True
			
			if play:
				self.fightOptions = "Yay"
				print("Leaving Menu Loop")
				return # A neat way of moving into the game. (might decide to send a list of config data instead)
			
			menu.currentPage.connectedPages[position].highlightOn()
			self.screen.refreshMenu(menu.currentPage)


	def gameLoop(self):

		print("Entering Game Loop")
		
		self.screen.whiteout() # Clear the screen
		dead = False
		while not dead:
			dead = Fight.Game()
			
		print("Leaving Game Loop")
	

	def resultsLoop(self):

		print("Entering Results Loop")
				
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
						print("Laaving Results Loop")
						return
				elif event.type == KEYUP:
					print("MenuUP")


			self.screen.refreshText()



















