import numpy as n

'''chunk_2 = n.ndarray(shape=(50,50), dtype = int)

chunk_1 = n.asarray(chunk_1)
print(chunk_1)

for x, row in enumerate(chunk_2):
<<<<<<< HEAD
	for y, col in enumerate(row):
		chunk_2[x][y] = 101
=======
    for y, col in enumerate(row):
        chunk_2[x][y] = 101
>>>>>>> d8a65ed1085a36a0fbc9d4eae6fb726d00f21e30


chunk_2[1][1] = 43742
print(chunk_2)'''

class map():
<<<<<<< HEAD
	immovable_block = 10
	enemy = 2
	player = 1

	chunk_1 = n.asarray([
		[10, 0, 0, 10, 10],
		[10, 0, 0, 0, 10],
		[0, 0, 0, 0, 0],
		[10, 0, 0, 0, 10],
		[10, 0, 0, 10, 10],
	])
	chunk_2 = n.asarray([
		[10, 10, 0, 10, 10],
		[10, 0, 0, 5, 10],
		[0, 0, 0, 0, 0],
		[10, 0, 0, 0, 10],
		[10, 10, 0, 10, 10],
	])

	chunks = {1: chunk_1, 2: chunk_2}

	player_location = {
		"chunk": 1,
		"x_pos": 1,
		"y_pos": 1,
	}

	def __init__(self, chunk: int, x: int, y: int):
		self.player_location["chunk"] = chunk
		self.player_location["x_pos"] = x
		self.player_location["y_pos"] = y

		self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]] = 2

	def draw_map(self):
		gui_grid = ""
		for x, row in enumerate(self.chunks[self.player_location["chunk"]]):
			for y, col in enumerate(row):
				#if col == 10:
				#	gui_grid += " ■ "
				
				if x == 0 and y == 0:
					gui_grid += " \u259B "

				elif x == 0 and y == len(self.chunks[self.player_location["chunk"]]) - 1:
					gui_grid += "\u259c "
				
				elif x == len(self.chunks[self.player_location["chunk"]]) - 1 and y == 0:
					gui_grid += " \u2599 "

				elif x == len(self.chunks[self.player_location["chunk"]]) - 1 and y == len(self.chunks[self.player_location["chunk"]]) - 1:
					gui_grid += "\u259F "

				#elif col == 10:
				#    gui_grid += " \u25a0 "
				elif y == 0 and col == 10:
					gui_grid += " \u258d "

				elif y == len(self.chunks[self.player_location["chunk"]])-1 and col==10:
					gui_grid += " \u258d "


				elif x == 0 and col == 10:
					gui_grid += "▀▀▀"
				elif x == len(self.chunks[self.player_location["chunk"]]) - 1 and col == 10:
					gui_grid += "▄▄▄"

				elif col == 0:
					gui_grid += " . "
				elif col == 2:
					gui_grid += " ▼ "
				elif col == 5:
					gui_grid += " ◉ "
			gui_grid += "\n"

		return(gui_grid)

	#updates player position by removing old location
	def update_player_pos(self):
		result = n.where(self.chunks[self.player_location["chunk"]]==2)
		player_old_location = [result[0][0], result[1][0]]

		self.chunks[self.player_location["chunk"]][player_old_location[0]][player_old_location[1]] = 0

		self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]] = 2

	#Moves the player in the specified direction
	def player_move(self, direction):
		if direction == "up":
			if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]-1][self.player_location["x_pos"]] == 10:
				return "Can't move, immovable block\n"

			self.player_location["y_pos"] -= 1
			self.update_player_pos()
			return self.draw_map()

		elif direction == "down":
			if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]+1][self.player_location["x_pos"]] == 10:
				return "Can't move, immovable block\n"

			self.player_location["y_pos"] += 1
			self.update_player_pos()
			return self.draw_map()
		
		elif direction == "right":
			if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]+1] == 10:
				return "Can't move, immovable block\n"

			self.player_location["x_pos"] += 1
			self.update_player_pos()
			return self.draw_map()
		
		elif direction == "left":
			if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]-1] == 10:
				return "Can't move, immovable block\n"

			self.player_location["x_pos"] -= 1
			self.update_player_pos()
			return self.draw_map()

	def check_player_movement(self, direction: str):
		ret_str = ""
		if direction == "up":
			if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]-1][self.player_location["x_pos"]] == 5:
				ret_str = "enemy"
				return ret_str

		elif direction == "down":
			if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]+1][self.player_location["x_pos"]] == 5:
				ret_str = "enemy"
				return ret_str
		
		elif direction == "left":
			if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]-1] == 5:
				ret_str = "enemy"
				return ret_str

		elif direction == "right":
			if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]+1] == 5:
				ret_str = "enemy"
				return ret_str

	'''def player_move_right(self):
		if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]+1] == 10:
			return "Can't move, immovable block\n"

		self.player_location["x_pos"] += 1
		self.update_player_pos()
		return self.draw_map()

	def player_move_left(self):
		if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]-1] == 10:
			return "Can't move, immovable block\n"

		self.player_location["x_pos"] -= 1
		self.update_player_pos()
		return self.draw_map()
		
	def player_move_up(self):
		if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]-1][self.player_location["x_pos"]] == 10:
			return "Can't move, immovable block\n"

		self.player_location["y_pos"] -= 1
		self.update_player_pos()
		return self.draw_map()

	def player_move_down(self):
		if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]+1][self.player_location["x_pos"]] == 10:
			return "Can't move, immovable block\n"

		self.player_location["y_pos"] += 1
		self.update_player_pos()
		return self.draw_map()'''
=======
    immovable_block = 10
    enemy = 2
    player = 1

    chunk_1 = n.asarray([
        [10, 0, 0, 10, 10],
        [10, 0, 0, 0, 10],
        [0, 0, 0, 0, 0],
        [10, 0, 0, 0, 10],
        [10, 0, 0, 10, 10],
    ])
    chunk_2 = n.asarray([
        [10, 8, 0, 8, 10],
        [9, 0, 0, 5, 9],
        [0, 0, 0, 0, 0],
        [9, 0, 0, 0, 9],
        [10, 8, 0, 8, 10],
    ])

    chunks = {1: chunk_1, 2: chunk_2}

    player_location = {
        "chunk": 1,
        "x_pos": 1,
        "y_pos": 1,
    }

    def __init__(self, chunk: int, x: int, y: int):
        self.player_location["chunk"] = chunk
        self.player_location["x_pos"] = x
        self.player_location["y_pos"] = y

        self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]] = 2

    def draw_map(self):
        gui_grid = ""
        for x, row in enumerate(self.chunks[self.player_location["chunk"]]):
            for y, col in enumerate(row):
                if x == 0 and y == 0:
                    gui_grid += " \u259B "

                elif x == 0 and y == len(self.chunks[self.player_location["chunk"]]) - 1:
                    gui_grid += "\u259c "
                
                elif x == len(self.chunks[self.player_location["chunk"]]) - 1 and y == 0:
                    gui_grid += " \u2599 "

                elif x == len(self.chunks[self.player_location["chunk"]]) - 1 and y == len(self.chunks[self.player_location["chunk"]]) - 1:
                    gui_grid += "\u259F "

                elif col == 10:
                    gui_grid += " \u25a0 "
                elif col == 9:
                    gui_grid += " \u258d "


                elif x == 0 and col == 8:
                    gui_grid += "▀▀▀"
                elif x == len(self.chunks[self.player_location["chunk"]]) - 1 and col == 8:
                    gui_grid += "▄▄▄"

                elif col == 0:
                    gui_grid += "   "
                elif col == 2:
                    gui_grid += " ▼ "
                elif col == 5:
                    gui_grid += " ◉ "
            gui_grid += "\n"

        return(gui_grid)

    #updates player position by removing old location
    def update_player_pos(self):
        result = n.where(self.chunks[self.player_location["chunk"]]==2)
        player_old_location = [result[0][0], result[1][0]]

        self.chunks[self.player_location["chunk"]][player_old_location[0]][player_old_location[1]] = 0

        self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]] = 2

    #Moves player to the right
    def player_move_right(self):
        if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]+1] == 10:
            return "Can't move, immovable block\n"

        self.player_location["x_pos"] += 1
        self.update_player_pos()
        return self.draw_map()

    def player_move_left(self):
        if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]-1] == 10:
            return "Can't move, immovable block\n"

        self.player_location["x_pos"] -= 1
        self.update_player_pos()
        return self.draw_map()
        
    def player_move_up(self):
        if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]-1][self.player_location["x_pos"]] == 10:
            return "Can't move, immovable block\n"

        self.player_location["y_pos"] -= 1
        self.update_player_pos()
        return self.draw_map()

    def player_move_down(self):
        if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]+1][self.player_location["x_pos"]] == 10:
            return "Can't move, immovable block\n"

        self.player_location["y_pos"] += 1
        self.update_player_pos()
        return self.draw_map()


map = map(2, 2, 2)
print(map.draw_map())
print(map.player_move_right())
print(map.player_move_up())
>>>>>>> d8a65ed1085a36a0fbc9d4eae6fb726d00f21e30
