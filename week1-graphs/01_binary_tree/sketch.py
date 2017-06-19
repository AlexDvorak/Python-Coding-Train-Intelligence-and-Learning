from tree import *
from math import floor
from random import randint

# New binary tree
tree = Tree()

# Add 10 random values to the tree
for i in range(10):
	tree.addValue(floor(randint(0,100)))

# Traverse the tree
tree.traverse()

# Search the tree for 10
result = tree.search(10)
if result == None:
	print "10 not found"
else:
	print result.value