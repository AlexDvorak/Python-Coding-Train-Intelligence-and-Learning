from node import *
class Graph(object):
	def __init__(self):
		self.graph = {}
		self.nodes = []
		self.start = None
		self.end = None
	
	def setStart(self,node):
		self.start = node

	def setEnd(self,node):
		self.end = node

	def addNode(self,label):
		n = Node(label)
		self.graph[label] = n
		self.nodes.append(n)
		return n

	def clear(self):
		for i in range(len(self.nodes)):
			self.nodes[i].searched = False
			self.nodes[i].parents = None