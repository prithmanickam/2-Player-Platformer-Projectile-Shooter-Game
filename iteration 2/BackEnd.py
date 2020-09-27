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
	def __init__(self, name):
		self.name = name
		self.graph = None


class Pages():
	def __init__(self):
		self.pages = []
		self.links = []
		self.graph = {}
		self.pageNames = None
		self.initPages()
		self.current = "Main"
		self.lastpage = None

	def initPages(self):
		pages = ("Main","Config","Start","Controls","Credits",
			"High Scores","Multi-Player","2-Player Select",
			"1-Player Select")
		self.pageNames = pages
		for page in pages:
			pageObj = Page(page)
			self.add_page(pageObj)

		links = (("Main","Config"),("Main","Start"),("Main","Controls"),
			("Main","Credits"),("Main","High Scores"),
			("Start", "2-Player Select"),("Start", "1-Player Select"))
		
		for link in links:
			link1, link2 = link
			ObjLinks = []
			for page in self.pages:
				if link1 == page.name or link2 == page.name:
					ObjLinks.append(page)
			self.add_link(ObjLinks)

		for page in self.pages:
			page.graph = self.graph


	def add_page(self,node):
		if node not in self.pages:
			self.pages.append(node)
			self.graph[node] = []

	def add_link(self,edge):
		if edge not in self.links:
			self.links.append(edge)
			
			node1, node2 = edge

			if node1 in self.graph:
				self.graph[node1].append(node2)
			else:
				self.graph[node1] = [node2]
			if node2 in self.graph and node2 != node1:
				self.graph[node2].append(node1)
			else:
				self.graph[node2] = [node1]


	def showPage(self,title):
		border = "*******************"
		for page in self.pages:
			if page.name == title:
				title = page
		print(border + "\n" + title.name + "\n" + border)
		self.showOptions(title)

	def showOptions(self):
		for item in self.graph[page]:
			if item.name != self.lastpage:
				print(item.name)

	def getOptions(self, page):
		
		options = []
		for item in self.graph[page]:
			options.append(item.name)
		return options

	def getPage(self):
		for page in self.pages:
			if page.name == self.current:
				return page





if __name__ == '__main__':

	
	g = Pages()
	#g.showPages()
	#g.showNodesOBJ()
	#g.showEdgesOBJ()

	
	currentPage = g.getPage()
	currentOptions = g.getOptions(currentPage)
	g.showPage(currentPage.name)

	g.lastpage = g.current
	g.current = currentOptions[1]
	currentPage = g.getPage()
	currentOptions = g.getOptions(currentPage)
	print(currentPage.name)

	g.showPage(currentPage.name)
	#print(currentPage.name)
	#g.showOptions(currentPage)
	#print(currentOptions)

	#g.current = currentOptions[0]

	#print(g.current)
	#currentPage = g.getPage()
	#currentOptions = g.getOptions(currentPage)

	#g.showOptions(currentPage)




	#g.showPage("Multi-Player")


