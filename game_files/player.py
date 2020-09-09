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

players = {
	"Mulitate4": "passw0rd"
}

with open ("other_files/player.json") as f:
	player_data = json.load(f)

class player():
	health = 100
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

	def __init__(self, player_name, exists: bool):
		if exists == True:
			print(f"Welcome back {player_name}")
			self.health = player_data[player_name]["health"]
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

			self.set_sword_damage()
			self.set_player_level()

		elif exists == False:
			print("New account created :3")

	'''These are initializing functions, will probably be required to run most of time
	so call these two - set_player_level(), and set_sword_damage().
	-- Gotta find a more efficient way :/'''
	#Player level function -sets player level after an encounter
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

	#Init function (?), can be used by shop
	def set_sword_damage(self):
		self.player_sword_damage = sword_damages[self.player_sword_level]

	#Player money methods
	def player_money_add(self, amount: int):
		self.player_money += amount
		return self.player_money

	def player_money_reduce(self, amount:int):
		self.player_money -= amount
		return self.player_money

	#Player Shop interaction, also calls set_sword_damage, which is required!
	def shop_set_sword_level(self, sword_level: int):
		self.player_sword_level = sword_level
		self.set_sword_damage()
		return f"Your sword is {self.get_player_sword_type()} which does {self.get_player_sword_damage_range()}"

	#Player backpack methods
	def backpack_add_item(self, item):
		self.player_backpack.append(item)

	#Player health methods
	def damage_health(self, damage_amount):
		self.health -= damage_amount
		return self.health

	def heal_health(self, heal_amount):
		self.health += heal_amount
		return self.health

	#Returns player's damage range
	def get_player_sword_damage_range(self):
		return f"{self.player_sword_damage[0]}-{self.player_sword_damage[1]}"

	#Return's player's sword type
	def get_player_sword_type(self):
		return sword_types[self.player_sword_level]

	#Returns random damage, will be used a lot!
	def get_player_sword_randomdmg(self):
		random_dmg = random.randint(self.player_sword_damage[0], self.player_sword_damage[1])
		return random_dmg

#this is enemy super class
class Enemy():
	health = 20
	damage = [1, 5]
	exp = [10, 20]
	gold = [5, 10]

	def __init__(self, rank: int):
		self.health *= rank
		for i, damage_possible in enumerate(self.damage):
			damage_possible *= rank
			self.damage[i] = damage_possible
		for i, exp_possible in enumerate(self.exp):
			exp_possible *= rank
			self.exp[i] = exp_possible
		for i, gold_possible in enumerate(self.gold):
			gold_possible *= rank
			self.gold[i] = gold_possible

	def get_random_damage(self):
		return random.randint(self.damage[0], self.damage[1])

	def get_random_gold_drop(self):
		return random.randint(self.gold[0], self.gold[1])

	def get_random_exp_drop(self):
		return random.randint(self.exp[0], self.exp[1])

	def enemy_damage_health(self, damage: int):
		self.health -= damage
		return self.health