import pygame
from pygame.locals import *
import FrontEnd as f
import BackEnd as b
import Fight
from pygame_functions import *
import Launcher

WHITE = 250,250,250

#This is where the main loops are... main game control


# game class that is instantiated in the Launcher
class Game():
	
	# Initialise what we need
	def __init__(self, screenSize, name, font = 'calibri'):
		self.screen = f.Screen(screenSize, name, font)
		self.screenSize = screenSize
		self.name = name
		# A Clock is needed to limit our framerate
		self.clock = pygame.time.Clock()
		# Options loaded in
		self.options = f.OptionConfigs()
		#self.options.cleanConfigFile()

		self.fightOptions = None


	# mainloop that controls the flow of the whole game
	def mainLoop(self):

		# Make sure wit is possible to exit the game.
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
		#promptText = "UP/DOWN to choose, ENTER to select"

		menu = b.Pages(self.name)
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
						if position < 0: # Ensure that we can't go out of bounds
							position = 0
					elif event.key == K_DOWN:
						menu.currentPage.connectedPages[position].highlightOff()
						position = position + 1
						if position > numberOptions: # ensure we don't go below our list...
							position = numberOptions
					elif event.key == K_BACKSPACE:
						if menu.currentPage.connectedFrom:
							menu.currentPage.connectedPages[position].highlightOff()
							menu.currentPage = menu.currentPage.connectedFrom
							position = 0
					elif event.key == K_RETURN:
						page = menu.currentPage.connectedPages[position]
						if page.name == "Config":
							self.configMenu(page)

						elif page.name == "1-Player Select" or page.name == "2-Player Select":
							play = self.playerSelectMenu(page.name)
						elif page.name == "Credits":
							self.creditsPage(page)
						elif page.name == "High Scores":
							self.highScores(page)
						elif page.name == "Controls":
							self.controlsMenu(page)

						if menu.currentPage.connectedPages[position].connectedPages:
							menu.currentPage.connectedPages[position].highlightOff()
							menu.currentPage = menu.currentPage.connectedPages[position]
							position = 0
					
			
			if play:
				self.fightOptions = "Yay"
				print("Leaving Menu Loop")
				return # A neat way of moving into the game. Might decide to send a list of config data instead
			
			menu.currentPage.connectedPages[position].highlightOn()
			self.screen.refreshMenu(menu.currentPage)


	def gameLoop(self):

		print("Entering Game Loop")
		
		
		self.screen.whiteout() # Clear the screen
		playing = True
		while playing:
			playing, strResult = Fight.Game(self.options, self.name, self.screenSize)
			
		print("From GameControl Module", strResult)

	def resultsLoop(self):

		print("Entering Results Loop")
		
		self.screen.setTitleText("Results")
		self.screen.setPromptText("Press Enter to continue")
		
		
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					quit()
				elif event.type == KEYDOWN:
					if event.key == K_RETURN:
						print("Leaving Results Loop")
						return
				
			self.screen.refreshText()

	def optionAdd(self,option,add,name,bounds):
		
		upper = bounds[name][len(bounds[name])-1]
		lower = bounds[name][0]
		# Restrict selections to the bounds of max, min or by index if there are more than two options
		if len(bounds[name]) > 2:
			currentIndex = bounds[name].index(option)
			currentIndex += add
			if currentIndex > len(bounds[name]) - 1:
				currentIndex = len(bounds[name]) - 1
			if currentIndex < 0:
				currentIndex = 0
			option = bounds[name][currentIndex]
		else:
			option += add
			if option > upper:
				option = upper
			if option < lower:
				option = lower

		return option

	def optionChange(self, name, add, bounds):
		if name == "Time":
			self.options.time = self.optionAdd(self.options.time,add,name,bounds)
		if name == "Sound Volume":
			self.options.sound = self.optionAdd(self.options.sound,add,name,bounds)
		elif name == "Music Volume":
			self.options.music = self.optionAdd(self.options.music,add,name,bounds)
		elif name == "Rounds":
			self.options.rounds = self.optionAdd(self.options.rounds,add,name,bounds)

	def configMenu(self, page):
		
		position = 0
		b.createConfigPage(page)

		self.screen.whiteout()
		
		while True:
			numberOptions = len(page.connectedPages) - 1

			for event in pygame.event.get():
				if event.type == QUIT:
					quit()
				elif event.type == KEYDOWN:
					if event.key == K_BACKSPACE:
						print("Leaving Config Menu")
						page.connectedPages = []
						self.options.saveConfig()
						return
					elif event.key == K_DOWN:
						page.connectedPages[position].highlightOff()
						position = position + 1
						if position > numberOptions: # ensure we don't go below our list...
							position = numberOptions
					elif event.key == K_UP:
						page.connectedPages[position].highlightOff()
						position = position - 1
						if position < 0: # ensure we don't go below our list...
							position = 0
					elif event.key == K_LEFT:
						self.optionChange(page.connectedPages[position].name, -1, page.boundsDict)
						
					elif event.key == K_RIGHT:
						self.optionChange(page.connectedPages[position].name, 1, page.boundsDict)
						
			
			page.connectedPages[position].highlightOn()
			self.screen.refreshMenu(page, True, self.options)	

	def playerSelectMenu(self,name):
		if name == "1-Player Select":
			return True
			print("1-PLAYER GAME SELECTED")
		else:
			print("2-PLAYER GAME SELECTED")
			return False

	def highScores(self, page):
		print("HERE ARE THE HIGH SCORES")

	def controlsMenu(self, page):
		print("HERE ARE THE CONTROLS")

	def creditsPage(self, page):
		print("Credits")
		b.createCreditsPage(page)
		self.screen.whiteout()

		while True:
			numberOptions = len(page.connectedPages) - 1

			for event in pygame.event.get():
				if event.type == QUIT:
					quit()
				elif event.type == KEYDOWN:
					if event.key == K_BACKSPACE:
						print("Leaving Credits")
						page.connectedPages = []
						return

			self.screen.refreshMenu(page)	

#Run the whole program from this module. For ease of development
if __name__ == "__main__":
	Launcher.main()












