from numpy import asarray, where

def homemade_where(arr, to_check_element):
	for y, row in enumerate(arr):
		for x, column in enumerate(row):
			if to_check_element != column:
				continue
			return (x, y)

class rpg_map():
	chunk_1 = asarray([
		[10, 10, 10, 10, 10],
		[10, 0, 0, 0, 10],
		[10, 0, 0, 0, 0],
		[10, 0, 0, 0, 10],
		[10, 0, 0, 10, 10],
	])
	chunk_2 = asarray([
		[10, 10, 0, 10, 10],
		[10, 0, 0, 5, 10],
		[10, 0, 0, 0, 0],
		[10, 0, 0, 0, 10],
		[10, 10, 0, 10, 10],
	])
	chunk_3 = asarray([
		[10, 10, 10, 10, 10],
		[10, 0, 0, 5, 10],
		[0, 0, 0, 0, 10],
		[10, 0, 0, 0, 10],
		[10, 10, 0, 10, 10],
	])
	chunk_4 = asarray([
		[10, 10, 0, 10, 10],
		[10, 0, 0, 5, 10],
		[0, 0, 0, 0, 10],
		[10, 0, 0, 0, 10],
		[10, 10, 0, 10, 10],
	])
	global_chunks = [
		[1, 3],
		[2, 4],
		[6, 5],
	]
	chunks = {1: chunk_1, 2: chunk_2, 3: chunk_3, 4: chunk_4}

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

	def draw_map(self, chunk):
		gui_grid = ""
		for x, row in enumerate(self.chunks[chunk]):
			for y, col in enumerate(row):
				#if col == 10:
				#	gui_grid += " ■ "
				
				if x == 0 and y == 0:
					gui_grid += " \u259B "

				elif x == 0 and y == len(self.chunks[chunk]) - 1:
					gui_grid += "\u259c "
				
				elif x == len(self.chunks[chunk]) - 1 and y == 0:
					gui_grid += " \u2599 "

				elif x == len(self.chunks[chunk]) - 1 and y == len(self.chunks[chunk]) - 1:
					gui_grid += "\u259F "

				#elif col == 10:
				#    gui_grid += " \u25a0 "
				elif y == 0 and col == 10:
					gui_grid += " \u258d "

				elif y == len(self.chunks[chunk])-1 and col==10:
					gui_grid += " \u258d "


				elif x == 0 and col == 10:
					gui_grid += "▀▀▀"
				elif x == len(self.chunks[chunk]) - 1 and col == 10:
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
		result = homemade_where(self.chunks[self.player_location["chunk"]], 2)

		print(result)

		player_old_location_x = result[0]
		player_old_location_y = result[1]
#		print(player_old_location)

		#replaces old location with empty space (0)
		self.chunks[self.player_location["chunk"]][player_old_location_y][player_old_location_x] = 0

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
		return self.draw_map(self.player_location['chunk'])

	#Checks player movement, before actually moving, and sending a signal
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

	#Moves the player to the next (specified) chunk
	def global_chunk_move(self, dir: str):
#		curr_chunk_xy = where(self.global_chunks == self.player_location["chunk"])
		curr_chunk_xy = homemade_where(self.global_chunks, self.player_location['chunk'])
				#Way of accessing y of result from n.where. curr_chunk has a list, in a tuple like so - ([y], [x])
		curr_chunk_x = curr_chunk_xy[0]
		#accessing x
		curr_chunk_y = curr_chunk_xy[1]

		#Resetting earlier chunk
		#TODO modify update player pos, to take an arg - (global_chunk and normal). Global chunk implements this below, amd takes
		#optional arg Chunk.
		old_chunk_index = self.global_chunks[curr_chunk_y][curr_chunk_x]
		print(old_chunk_index)

		curr_chunk = self.chunks[self.player_location["chunk"]]
		result = homemade_where(curr_chunk, 2)
		
		# player_old_loc = [result[0], result[1]]
		player_old_loc_x = result[0]
		player_old_loc_y = result[1]
		
		#TODO, make this dynamic, by taking array.size
		if dir == "up":
			self.player_location["chunk"] = int(self.global_chunks[curr_chunk_y-1][curr_chunk_x])
			self.player_location["y_pos"] = 5
			self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]-1][self.player_location["x_pos"]] = 2

		elif dir == "down":
			self.player_location["chunk"] = int(self.global_chunks[curr_chunk_y+1][curr_chunk_x])
			self.player_location["y_pos"] = -1
			print(self.player_location["chunk"])
			print(self.player_location["y_pos"])
			print(self.player_location["x_pos"])
			
			self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]+1][self.player_location["x_pos"]] = 2
		
		elif dir == "right":
			self.player_location["chunk"] = int(self.global_chunks[curr_chunk_y][curr_chunk_x+1])
			self.player_location["x_pos"] = -1
			self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]+1] = 2
		
		elif dir == "left":
			self.player_location["chunk"] = int(self.global_chunks[curr_chunk_y][curr_chunk_x-1])
			self.player_location["x_pos"] = 5
			self.chunks[self.player_location["chunk"]][self.player_location["y_pos"]][self.player_location["x_pos"]-1] = 2
		
		
		self.chunks[old_chunk_index][player_old_loc_y][player_old_loc_x] = 0
		self.player_move(dir)

	#Gives player location as a dict
	def ret_player_location(self):
		return self.player_location