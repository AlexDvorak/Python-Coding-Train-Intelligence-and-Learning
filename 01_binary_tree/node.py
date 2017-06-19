# Node in the tree
class Node(object):
	def __init__(self,val):
		self.value = val
		self.left = None
		self.right = None

# Search the tree for a value
	def search(self,val):
		if self.value == val:
			return self
		elif val < self.value and self.left != None:
			return self.left.search(val)
		elif val > self.value and self.right != None:
			return self.right.search(val)
		# otherwise if nothing found then return none
		return None

	def visit(self):
		# Recursively go to the left
		if self.left != None:
			self.left.visit()

		print self.value

		# Recursively go to the right
		if self.right != None:
			self.right.visit()

	def addNode(self,n):
		if n.value < self.value:
			if self.left == None:
				self.left = n
			else:
				self.left.addNode(n)

		elif n.value > self.value:
			if self.right == None:
				self.right = n
			else:
				self.right.addNode(n)