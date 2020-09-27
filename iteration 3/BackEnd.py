import pygame
from pygame.locals import *


#Game logic: AI, animations, scoring

# Not much going on in here yet.



class AILogic():
	def __init__(self):
		pass
	def __str__(self):
		return "AI Working"



class Page():
	
	def __init__(self,title, name):
		self.title = title
		self.name = name
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

	def __init__(self):
		self.page_list = self.createMenu()
		self.currentPage = self.setCurrentPage()

	def setCurrentPage(self):
		for page in self.page_list:
			if page.name == "Main":
				return page

	def createMenu(self):
	
		pages = (("Street Fighter", "Main"),("Configuration Screen","Config"),("Game Select","Start"),("Control Screen","Controls"),("Credits","Credits"),
				("High Score Table","High Scores"),("Choose Characters","2-Player Select"),("Choose Character",
				"1-Player Select"))
	
		links = (("Main","Config"),("Main","Start"),("Main","Controls"),
				("Main","Credits"),("Main","High Scores"),
				("Start", "2-Player Select"),("Start", "1-Player Select"))
	
		return self.create(pages, links)
	
	def create(self, pages, links):
		page_list = []
		for page in pages:
			title, name = page
			obj = Page(title, name)
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


if __name__ == '__main__':

	p = Page("Test","TestName")
	pass