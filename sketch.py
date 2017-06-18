import json
from graph import *
from node import *

# The data
data = None
# Create the graph
graph = Graph()
# A seperate lookup table for actors
actors = {}

# Load bacon.json data
with open('bacon.json') as data_file:    
    data = json.load(data_file)

# For all movies
movies = data["movies"]
for i in range(len(movies)):
	# Title and castlist
	movie = movies[i]["title"]
	cast = movies[i]["cast"]
	# Add the movie to the graph
	movieNode = graph.addNode(movie)
	# Go through the entire castlist
	for j in range(len(cast)):
		name = cast[j]
		# Does the actor exist already?
		if name in actors:
			actorNode = actors[name]
		# If not add a new node
		else:
			actorNode = graph.addNode(name)
			actors[name] = actorNode
		# Connect movie and actor
		movieNode.connect(actorNode)

def bfs():
	# Create a queue and path
	queue = []
	path = []

	# Get started
	queue.append(graph.start)

	while len(queue) > 0:
		node = queue.pop(0)
		# Are we done?
		if node == graph.end:
			# Figure out the path
			path.append(node)
			mnext = node.parent
			while mnext != None:
				path.append(mnext)
				mnext = mnext.parent
				break
		else:
			# Check all neighbors
			mnext = node.edges
			for i in range(len(mnext)):
				neighbor = mnext[i]
				# Any neighbor not already searched add to the queue
				if not neighbor.searched:
					queue.append(neighbor)
					# Update the parent
					neighbor.parent = node
			# Mark node as searched
			node.searched = True
	print "-------finished-------"
	result = ""
	path = list(reversed(path))
	for i in path:
		result += i.label
		result += " -> "
	result = result[:-3]
	print result

def findbacon():
	# Clear everyone from having been searched
	graph.clear()
	# Start and end. Change start to an actor of your choice 
	start = actors["Gita Reddy"]
	end = actors["Kevin Bacon"]
	graph.setStart(start)
	graph.setEnd(end)
	# Run the search
	bfs()

# Run it
findbacon()