import random
import time
import json

common_items = ["stick", "apple"]
uncommon_items = ["stone_sword", "money_bag"]

sword_types = {
	1:"stick",
	2:"stone sword",
	3:"iron sword",
	4:"greatsword",
}
sword_damages = {
	1:[5,10],
	2:[11, 15],
	3:[16, 20],
	4:[21, 25]
}
bow_levels = {
	0:"none",
	1:"wooden bow",
	2:"stone bow",
	3:"iron bow",
	4:"great bow",
}

def get_player_data():
	with open ("game_files/other_files/player.json") as p:
		return json.load(p)
		
player_data = get_player_data()

class player():
	#---------------
	# ALL VARIABLES
	#---------------
	player_health = 100
	player_sword_damage = []

	player_sword_level = 1

	player_bow_level = 0

	levels = 100
	
	player_level = 0
	player_exp = 0
	player_required_exp = 40

	player_money = 0
	player_backpack = []

	player_location = {
		"chunk": 1,
		"x_pos": 1,
		"y_pos": 1,
	}

	def __init__(self, player_name, exists: bool, password = None):
		if exists == True:
			print(f"Welcome back {player_name}")
			
			self.get_player_data(player_name=player_name)

			self.set_sword_damage()

		else:
			print("New account created :3")
			player_data[player_name] = {}
			player_data[player_name]["password"] = password

			self.save_player_data_json(player_name=player_name, player_location=self.player_location)
			
			self.set_sword_damage()

	#________________________#
	#-----------------
	# LEVELING METHOD
	#-----------------
	def set_player_level(self):
		local_required_exp = self.player_required_exp
		local_exp = self.player_exp

		#For loop to increase exp required and checks levels gained
		for level in range(self.player_level, self.levels):
			local_required_exp += 10
			if local_exp >= local_required_exp:
				local_exp -= local_required_exp
				level += 1
			else:
				break
		self.player_level = level
		self.player_exp = local_exp
		self.player_required_exp = local_required_exp
		return self.player_level, self.player_exp

	#------------------
	# SWORD INIT METHOD
	#------------------
	def set_sword_damage(self):
		self.player_sword_damage = sword_damages[self.player_sword_level]
	#_________________________#

	#----------------------
	# PLAYER MONEY METHODS
	#----------------------
	def player_money_add(self, amount: int):
		self.player_money += amount
		return self.player_money

	def player_money_reduce(self, amount:int):
		self.player_money -= amount
		return self.player_money

	#---------------------
	# PLAYER SHOP METHODS
	#---------------------
	def shop_set_sword_level(self, sword_level: int):
		self.player_sword_level = sword_level
		self.set_sword_damage()
		return f"Your sword is {self.get_player_sword_type()} which does {self.get_player_sword_damage_range()}"

	#-------------------------
	# PLAYER BACKPACK METHODS
	#-------------------------
	def backpack_add_item(self, item):
		self.player_backpack.append(item)

	#-----------------------
	# PLAYER HEALTH METHODS
	#-----------------------
	def damage_health(self, damage_amount):
		self.player_health -= damage_amount
		return self.player_health

	def heal_health(self, heal_amount):
		self.player_health += heal_amount
		return self.player_health

	#----------------------------
	# RETURNS TUPLE OF SWORD DMG
	#----------------------------
	def get_player_sword_damage_range(self):
		return (self.player_sword_damage[0], self.player_sword_damage[1])

	#---------------------------
	# RETURNS SWORD TYPE AS STR
	#---------------------------
	def get_player_sword_type(self):
		return sword_types[self.player_sword_level]

	#-----------------------------
	# RETURNS RANDOM DAMAGE AS INT
	#-----------------------------
	def get_player_sword_randomdmg(self):
		random_dmg = random.randint(self.player_sword_damage[0], self.player_sword_damage[1])
		return random_dmg

	#-------------------------------
	# SAVE AND RETRIEVE PLAYER DATA
	#-------------------------------
	def save_player_data_json(self, player_name: str, player_location):
		player_data[player_name]["health"] = self.player_health
		player_data[player_name]["player_sword_level"] = self.player_sword_level
		player_data[player_name]["player_sword_level"] = self.player_bow_level

		player_data[player_name]["player_level"] = self.player_exp
		player_data[player_name]["player_level"] = self.player_level
		player_data[player_name]["player_required_exp"] = self.player_required_exp 

		player_data[player_name]["player_money"] = self.player_money 
		player_data[player_name]["player_backpack"] = self.player_backpack

		player_data[player_name]["player_location"] = player_location
		with open('game_files/other_files/player.json','w') as outfile:
			json.dump(player_data, outfile)

	def get_player_data(self, player_name):
		self.player_health = player_data[player_name]["health"]
		self.player_sword_level = player_data[player_name]["player_sword_level"]
		self.player_bow_level = player_data[player_name]["player_sword_level"]

		self.player_exp = player_data[player_name]["player_level"]
		self.player_level = player_data[player_name]["player_level"]
		self.player_required_exp = player_data[player_name]["player_required_exp"]

		self.player_money = player_data[player_name]["player_money"]
		self.player_backpack = player_data[player_name]["player_backpack"]

		self.player_location["x_pos"] = player_data[player_name]["player_location"]["x_pos"]
		self.player_location["y_pos"] = player_data[player_name]["player_location"]["y_pos"]
		self.player_location["chunk"] = player_data[player_name]["player_location"]["chunk"]