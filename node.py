class Node(object):
	def __init__(self,label):
		self.label = label
		self.edges = []
		self.parent = None
		self.searched = False

	def connect(self,*neighbors):
		for i in range(len(neighbors)):
			self.edges.append(neighbors[i])
			neighbors[i].edges.append(self)