import pygame
from pygame.locals import *
import Launcher


#Game logic: AI, animations, scoring

# Not much going on in here yet.



class AILogic():
	def __init__(self):
		pass
	def __str__(self):
		return "AI Working"



class Page():
	def __init__(self,title, name, prompt = "Blank"):
		self.title = title
		self.name = name
		self.prompt = prompt
		self.boundsDict = {}
		self.selections = []
		self.connectedPages = []
		self.connectedPageNameStrings = []
		self.connectedFrom = None
		self.highlighted = False
		self.colour = pygame.Color("black")


	def updateStrings(self):
		for page in self.connectedPages:
			self.connectedPageNameStrings.append(page.name)

	def highlightOn(self):
		self.highlighted = True
		self.colour = pygame.Color("red")
	
	def highlightOff(self):
		self.highlited = False
		self.colour = pygame.Color("black")


class Pages():

	def __init__(self, name):
		self.title = name
		self.page_list = self.createMenu()
		self.currentPage = self.setCurrentPage()

	def setCurrentPage(self):
		for page in self.page_list:
			if page.name == "Main":
				return page

	def createMenu(self):
	
		pages = ((self.title,"Main","UP/DOWN to choose, ENTER to select"),
				("Game Select","Start","UP/DOWN to choose, ENTER to select, BACKSPACE = back"),
				("Configuration Screen","Config","UP/DOWN to select, LEFT/RIGHT to adjust, BACKSPACE = back"),
				("Control Screen","Controls","Stuff"),
				(self.title,"Credits","BACKSPACE = back"),
				("High Score Table","High Scores","Stuff"),
				("Choose Characters","2-Player Select","Stuff"),
				("Choose Character","1-Player Select","Stuff"))
	
		links = (("Main","Start"),
				("Main","Config"),
				("Main","Controls"),
				("Main","Credits"),
				("Main","High Scores"),
				("Start", "1-Player Select"),
				("Start", "2-Player Select"))
	
		return self.create(pages, links)
	



	def create(self, pages, links):
		page_list = []
		for page in pages:
			title, name, prompt = page
			obj = Page(title, name, prompt)
			page_list.append(obj)
	
		for link in links:
			link1, link2 = link
	
			for page in page_list:
				if link1 == page.name:
					for linkpage in page_list:
						if link2 == linkpage.name:
							page.connectedPages.append(linkpage)
							linkpage.connectedFrom = page
	
		for page in page_list:
			page.updateStrings()
	
		return page_list
	
	def showPages(self):
		for page in self.page_list:
			print("Page title:  ",page.title)
	
			print("it's selection:  ",page.name)
			print("Connections")
			if page.connectedPages:
				for connection in page.connectedPages:
					print(" - ",connection.name)
			else:
				print("None")
			if page.connectedFrom:
				print("From - ", page.connectedFrom.name)
			else:
				print("From -  NONE")
	
			print("\n\n")


def createConfigPage(page):
	page.connectedPages = []
	# Config page options
	options = ["Time","Rounds","Sound Volume","Music Volume"]
	# Each boundaries. Either: [min,max] or [Mulitple Steps]
	page.boundsDict = {"Time":[15,30,45,60,90], "Rounds":[1,3,5,7,10], "Sound Volume": [0,10], "Music Volume": [0,11]}


	for option in options:
		page.connectedPages.append(Page(option,option))

def createCreditsPage(page):
	page.connectedPages = []

	options = ["by Manickam", " ", " ", "Code algorithms by David Perryman", "Pygame_functions etc"]

	for option in options:
		page.connectedPages.append(Page(option, option))

if __name__ == '__main__':
	Launcher.main()
	
