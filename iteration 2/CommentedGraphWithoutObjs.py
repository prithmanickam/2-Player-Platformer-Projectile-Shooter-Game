
class Pages(object):
	#initialise it
	def __init__(self):
		#needs nodes list, edges list and the graph itself as a dictionary
		self.pages = []
		self.links = []
		self.graph = {}
		self.initPages()

	def initPages(self):
		pages = ("Main","Config","Start","Controls","Credits",
			"High Scores","Multi-Player","2-Player Select",
			"1-Player Select")
		for page in pages:
			self.add_page(page)

		links = (("Main","Config"),("Main","Start"),("Main","Controls"),
			("Main","Credits"),("Main","High Scores"),
			("Multi-Player", "2-Player Select"),("Multi-Player", "1-Player Select"))
		for link in links:
			self.add_link(link)

	# Adds nodes to itself.
	def add_page(self,node):
		#so if the node I want to add is not in the nodes list
		if node not in self.pages:
			#append it
			self.pages.append(node)
			#update the graph dictionary with the node as key and give it an empty list.
			self.graph[node] = []

	#Add an edge method.
	def add_link(self,edge):
		#if the edge doesn't exist
		if edge not in self.links:
			#append it.
			self.links.append(edge)

			#now update the graph.  an edge it is a tuple
			#in this case a tuple of two numbers a from and to node.
			#so extract them out into seperate variables.
			node1, node2 = edge

			#Is node1 in the graph
			if node1 in self.graph:
				#append node2 to the node1 list.
				self.graph[node1].append(node2)
			else:
				#Make a new dictionary entry for it if its not there.
				self.graph[node1] = [node2]
			#is node2 in the graph?
			if node2 in self.graph and node2 != node1:
				#then append node1 to the node2 list.
				self.graph[node2].append(node1)
			else:
				#or create a new one.
				self.graph[node2] = [node1]
				

	#Printing - Each prints out what it needs to by iterating over the relevany attribute.
	def showEdges(self):
		for link in self.links:
			print(link)

	def showNodes(self):
		for page in self.pages:
			print(page)
	#The graph needs the key and the page.
	def showGraph(self):
		for page in self.graph:
			print("page: {0} is joined to: {1}".format(page, self.graph[page]))

	def showPages(self):
		exclude = []
		for page in self.graph:
			print(page)
			print("_______________")
			exclude.append(page)
			for item in self.graph[page]:
				if item not in exclude:
					print(item)
			print()
			print()
		print("---------------\n")

	def showPage(self, page):
		for item in self.graph[page]:
			print(item)







if __name__ == '__main__':

	#build a graph and then play about with it to prove it all works.

	def title(title):
		border = "*******************"
		print(border + "\n" + title + "\n" + border)


	g = Pages()
	#g.showPages()
	g.showPage("Main")

	'''
	title("Pages")
	g.showNodes()
	title("Page Links")
	g.showEdges()
	title("Flow Diagram")
	g.showGraph()
	'''