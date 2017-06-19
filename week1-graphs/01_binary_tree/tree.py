from node import *

# Tree object
class Tree(object):
	def __init__(self):
		# Just store the root
		self.root = None

	# Start by searching the root
	def traverse(self):
		self.root.visit()

	# Start by searching the root
	def search(self,val):
		found = self.root.search(val)
		return found

	# Add a new value to the tree
	def addValue(self,val):
		n = Node(val)
		if self.root == None:
			self.root = n
		else:
			self.root.addNode(n)