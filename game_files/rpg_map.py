from numpy import asarray, where

class map():
	immovable_block = 10
	enemy = 2
	player = 1

	chunk_1 = asarray([
		[10, 10, 10, 10, 10],
		[10, 0, 0, 0, 10],
		[0, 0, 0, 0, 0],
		[10, 0, 0, 0, 10],
		[10, 0, 0, 10, 10],
	])
	chunk_2 = asarray([
		[10, 10, 0, 10, 10],
		[10, 0, 0, 5, 10],
		[0, 0, 0, 0, 0],
		[10, 0, 0, 0, 10],
		[10, 10, 0, 10, 10],
	])
	chunk_3 = asarray([
		[10, 10, 0, 10, 10],
		[10, 0, 0, 5, 10],
		[0, 0, 0, 0, 10],
		[10, 0, 0, 0, 10],
		[10, 10, 0, 10, 10],
	])

	global_chunks = asarray([
		[1, 3],
		[2, 4],
		[6, 5],
	])
	chunks = {1: chunk_1, 2: chunk_2, 3: chunk_3}

	player_location = {
		"chunk": 1,
		"x_pos": 1,
		"y_pos": 1,
	}

	def __init__(self, player: object):
		self.player_location["chunk"] = player.player_location["chunk"]
		self.player_location["x_pos"] = player.player_location["x_pos"]
		self.player_location["y_pos"] = player.player_location["y_pos"]

		#------PLACES THE PLAYER IN THE CORRECT POSITION------#
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
		result = where(self.chunks[self.player_location["chunk"]]==2)

		# if result[0].size > 0 and result[1] > 0:
		player_old_location = [result[0][0], result[1][0]]
		print(player_old_location)

		#replaces old location with empty space (0)
		self.chunks[self.player_location["chunk"]][player_old_location[0]][player_old_location[1]] = 0

		#replaces new location with player(2)
		self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]] = 2
	
		# else:
		# 	self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]] = 2
		# 	print("An unexpected error Occurred")

	#Moves the player in the specified direction
	def player_move(self, direction):
		if direction == "up":
			if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]-1][self.player_location["x_pos"]] == 10:
				return "Can't move, immovable block\n"

			self.player_location["y_pos"] -= 1

		elif direction == "down":
			if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]+1][self.player_location["x_pos"]] == 10:
				return "Can't move, immovable block\n"

			self.player_location["y_pos"] += 1
		
		elif direction == "right":
			if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]+1] == 10:
				return "Can't move, immovable block\n"

			self.player_location["x_pos"] += 1
		
		elif direction == "left":
			if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]-1] == 10:
				return "Can't move, immovable block\n"

			self.player_location["x_pos"] -= 1

		
		self.update_player_pos()
		return self.draw_map()

	def check_player_movement(self, direction: str):
		ret_str = ""
		if direction == "up":
			#TODO - Make it dynamic, by taking length of array, rather than hard-coding values
			#Checks if player's Y_position is 0
			if self.player_location["y_pos"] == 0:
				return "chunk_move"

			elif self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]-1][self.player_location["x_pos"]] == 5:
				ret_str = "enemy"
				return ret_str

		elif direction == "down":
			if self.player_location["y_pos"] == 4:
				return "chunk_move"
			
			elif self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]+1][self.player_location["x_pos"]] == 5:
				ret_str = "enemy"
				return ret_str
		
		elif direction == "left":
			if self.player_location["x_pos"] == 0:
				return "chunk_move"
			
			if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]-1] == 5:
				ret_str = "enemy"
				return ret_str

		elif direction == "right":
			if self.player_location["x_pos"] == 4:
				return "chunk_move"
			
			if self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]+1] == 5:
				ret_str = "enemy"
				return ret_str

	def global_chunk_move(self, dir: str):
		curr_chunk = where(self.global_chunks == self.player_location["chunk"])
		#Way of accessing y of result from n.where. curr_chunk has a list, in a tuple like so - ([y], [x])
		curr_chunk_y = curr_chunk[0][0]
		#accessing x
		curr_chunk_x = curr_chunk[1][0]

		if dir == "up":
			self.player_location["chunk"] = int(self.global_chunks[curr_chunk_y-1][curr_chunk_x])
			self.player_location["y_pos"] = 5
			self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]-1][self.player_location["x_pos"]] = 2

		elif dir == "down":
			self.player_location["chunk"] = int(self.global_chunks[curr_chunk_y+1][curr_chunk_x])
			self.player_location["y_pos"] = -1
			self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]+1][self.player_location["x_pos"]] = 2
		
		elif dir == "right":
			self.player_location["chunk"] = int(self.global_chunks[curr_chunk_y][curr_chunk_x+1])
			self.player_location["x_pos"] = -1
			self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]+1] = 2
		
		elif dir == "left":
			self.player_location["chunk"] = int(self.global_chunks[curr_chunk_y][curr_chunk_x-1])
			self.player_location["x_pos"] = 5
			self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]-1] = 2
		
		self.player_move(dir)

	def ret_player_location(self):
		return self.player_location