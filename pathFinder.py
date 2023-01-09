# importing modules to be uesed
import pygame
import math
from queue import PriorityQueue

# defining colours and creating pygame window
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

surface = pygame.display.set_mode((800,800))


#defining class for our grid locations
class Spot:
    # initializing with row, colmn, width, andd total number of rows
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

    # getting the position of a grid square
	def get_pos(self):
		return self.row, self.col

    # functions to return properties of grid square
	def is_closed(self):
		return self.color == RED

	def is_open(self):
		return self.color == GREEN

	def is_barrier(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == ORANGE

	def is_end(self):
		return self.color == TURQUOISE

    # functions to change values of the grid square
	def reset(self):
		self.color = WHITE

	def make_start(self):
		self.color = ORANGE

	def make_closed(self):
		self.color = RED

	def make_open(self):
		self.color = GREEN

	def make_barrier(self):
		self.color = BLACK

	def make_end(self):
		self.color = TURQUOISE

	def make_path(self):
		self.color = PURPLE

    # function to draw the square
	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		# checking all neighours of a node and if it is not a barrier then adding to a neighbour
		# also initially checking whether there is a node to check
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False


# returns Manhattan distance between two points
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# function to build grid
def build_grid(rows, width):
    grid = []
    # gives us the width of each square 
    gridWidth = width // rows

    # creating corresponding nodes with correct parameters
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Spot(i,j,gridWidth, rows)
            grid[i].append(node)

    return grid

def draw_grid(win, rows, width):
    # getting the width of each square
    gridWidth = width // rows
    for i in range(rows):
        # drawing the horizontal lines
        pygame.draw.line(win, GREY, (0, i * gridWidth), (width, i* gridWidth))

        #drawing the vertical lines
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gridWidth, 0), (j * gridWidth, width))

# function to draw the squarees
def draw(win, grid, rows, width):
	win.fill(WHITE)
    # drawing all the sqaures by traversing all squares in all rows of the grid
	for row in grid:
		for node in row:
			node.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gridWidth = width // rows
    y, x = pos

    # getting the row and col of the square that was clicked and then returning it
    row = y // gridWidth
    col = x // gridWidth

    return row, col

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()



def algorithm(draw, grid, start, end):
	# defining variables
	count = 0
	open_set = PriorityQueue()
	# inputting the first value of 0 into the priority queue
	open_set.put((0, count, start))
	came_from = {}
	
	g_score = {node: float("inf") for row in grid for node in row}
	#setting initial g score of our start node to 0
	g_score[start] = 0
	f_score = {node: float("inf") for row in grid for node in row}
	# setting initial f score of our start node to the distance
	f_score[start] = distance(start.get_pos(), end.get_pos())

	open_set_hash = {start}

	# algorithm runs until the priority queue is empty
	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		# popping the lowest f score node
		current = open_set.get()[2]
		open_set_hash.remove(current)

		# if we have reached the last node
		if current == end:
			# creating the path 
			reconstruct_path(came_from, end, draw)
			end.make_end()
			return True

		# looking at the neighbours of our node
		for neighbor in current.neighbors:
			# since we are going one more to get to the node, doing + 1
			temp_g_score = g_score[current] + 1

			# if we find a shorter path than before
			if temp_g_score < g_score[neighbor]:
				# changing g and f scorevalues as well as came from value to reflect change in priority queue
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + distance(neighbor.get_pos(), end.get_pos())
				# if the neighbour is not in our queue
				if neighbor not in open_set_hash:
					# adding neighbour into our priority queue
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

		# redrawing the grid
		draw()

		# if the node is not our start node, closing it off since we already looked at it
		if current != start:
			current.make_closed()

	# if we do not find a path
	return False



def main(win, width):
	# building grid
	ROWS = 50
	grid = build_grid(ROWS, width)

	start = None
	end = None
	run = True

	while run:
		# drawing grid which updates the display as well
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			# if left pressed
			if pygame.mouse.get_pressed()[0]: 
				# getting position 
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				node = grid[row][col]
				# if there is not start position and it is not also the end square
				if not start and node != end:
					# setting square to the start square
					start = node
					start.make_start()

				# if there is not end position and it is not also the start square
				elif not end and node != start:
					# setting square to the end square
					end = node
					end.make_end()

				# if it is neither the start or end position 
				elif node != end and node != start:
					# creating a barrier
					node.make_barrier()

			# if it was a right click
			elif pygame.mouse.get_pressed()[2]: # RIGHT
				# getting position and resetting that square and corresponding variables if necessary
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				node = grid[row][col]
				node.reset()
				if node == start:
					start = None
				elif node == end:
					end = None

			# if user presses a button and it is the spacebar and we have a start and end already
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					# going through each row
					for row in grid:
						# going through each node
						for node in row:
							# updating rhe neighbours of that node
							node.update_neighbors(grid)

					# calling the algorithm function
					algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

				# resetting the map and variablesif user presses c
				if event.key == pygame.K_c:
					start = None
					end = None
					grid = build_grid(ROWS, width)

	pygame.quit()

main(surface, 800)