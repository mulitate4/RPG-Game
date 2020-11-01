#----------------
# MODULE IMPORTS
#----------------
import random
import time
import json
from os import system
import sys


#-------------------
# GAME FILE IMPORTS
#-------------------
from game_files import player
from game_files import rpg_map
from game_files import enemies
from game_files import rpg_shop


#-----------
# VARIABLES
#-----------
enemy_encountered = False
directions = {
	'w': 'up',
	'a': 'left',
	's': 'down',
	'd': 'right',
}
yes_aliases = [
	"Yes",
	"yes",
	"y",
]
no_aliases = [
	"No",
	"no",
	"n",
]

#------------
# MAIN GAME FUNCTIONS
#------------
def player_login(player_name, player_data):
	#------------
	# LOGIN SYSTEM
	#------------

	#-----------CHECK IF PLAYER EXISTS-----------#
	#-----------PLAYER EXISTS - LOGIN-----------#
	if player_name in [player for player in player_data]:

		#while loop to keep asking password
		while True:
			password = input("Enter Password: ")

			#------------check password given-------------#
			#Password matches, continue with game
			if password == player_data[player_name]["password"]:
				game_player = player.player(player_name=player_name, exists=True)
				return game_player

			#Password doesn't match
			else:
				print(f"Player name and Password don't match!")
				enter_pass_again = input("Do you want to try again?\ny: Yes\nn: No\n")

				#Try again - Yes
				if enter_pass_again in yes_aliases:
					continue

				#Try again - No
				elif enter_pass_again in no_aliases:
					return "leave"

				#Try again - Not Valid
				else:
					print("Enter a valid choice")
					continue

	#-----PLAYER DOESNT EXISTS (CREATE NEW)------#
	elif player_name not in [player for player in player_data]:
		while True:
			create_new_acc = input(f"{player_name} does not exist, create a new player?\ny: Yes\nn: No\n")
			#-----------CREATE ACC - YES-----------#
			if create_new_acc in yes_aliases:
				#Creates a new player with the given password
				password = input("Enter a P4$$w0rd: ")
				game_player = player.player(player_name=player_name, exists=False, password=password)

				#Returns the newly created player
				print(f"Welcome {player_name}")
				player_data = get_player_data()
				return player_data

			#-----------CREATE ACC - NO------------#
			elif create_new_acc in no_aliases:
				return "leave"

			#-----------Create ACC - Enter Valid ---#
			else:
				print("Enter a valid option ples!")
				continue

def main_game_map():
	while True:
		print(game_map.draw_map(game_map.player_location['chunk']))
		direc = input("enter direction: ")
		if direc in directions.keys():

			#-----------Using Directions[dir] to convert into proper directions-----------#
			#---------------Checks if the direction entered has enemy on it---------------#
			signal = game_map.check_player_movement(directions[direc])

			if signal == "enemy":
				enemy_encounter()

			elif signal == "chunk_move":
				game_map.global_chunk_move(directions[direc])
				save_game_state()

			else:
				print(game_map.player_move(directions[direc]))
				save_game_state()
		
		#-----------Player types Q, so quit the game-----------#
		elif direc == "q":
			print("quit the game")
			save_game_state()
			exit()

		#---------------------------------
		# Basically CHEAT CODES/ DEV TOOLS
		#---------------------------------
		#TODO - Make this dict

		elif direc == "map":
			print(game_map.ret_player_location())
			continue

		elif "chunk" in direc:
			num = direc.split(" ")[1]
			print(game_map.draw_map(int(num)))
			continue

		elif direc == "map":
			print(game_map.ret_player_location())
			continue

		elif direc == "shop":
			shop()

		else:
			print ("Enter valid direction with W-up, A-left, S-down, D-right")
			continue
		system("cls")

def enemy_encounter():
	#------------
	# TO-DO:
	# Make the Enemy Encounter system
	# similiar to drug wars
	#------------
	system("cls")
	while True:
		print("Enemy Encountered")
		print("your stats: \n")
		player_stats()
		break

	main_game_map()

def shop():
	system("cls")
	max_chars = 0
	for item in game_shop.items:
		item_length = len(item)
		if item_length > max_chars:
			max_chars = item_length
		
	max_chars += 8
	h = "+" + "-"*max_chars + "+"

	print(h)
	for item in game_shop.items:
		print(f"|{item} iz for {game_shop.items[item]}|")
	print(h)
	print(game_shop.buy_item("apple"))
	print(game_shop.sell_item("apple"))
	print(game_shop.sell_item("apple"))
	exit()

#------------
# SIDE/EXTRA FUNCTIONS
#------------
def player_stats():
	print(f"health: {game_player.player_health}")
	print(f"money: {game_player.player_money}")

def enemy_stats(enemy):
	print(f"health: {enemy.health}")

def get_player_data():
	with open ("game_files/other_files/player.json") as p:
		return json.load(p)

def border_msg(sentences: list, indent = 1):
	space = " "*indent
	max_sentence = 0
	for sentence in sentences:
		item_length = len(sentence)
		if item_length > max_sentence:
			max_sentence = item_length

	box_top_left = u"\u2554"
	box_double_line = u"\u2550"
	box_top_right = u"\u2557"
	box_vert_double_line = u"\u2551"

	box = box_top_left + (2 * indent + max_sentence)*box_double_line + box_top_right +"\n"

	for sentence in sentences:
		box += f'{box_vert_double_line}{space}{sentence}{" "*(max_sentence - len(sentence))}{space}{box_vert_double_line}\n'

	box += f'╚{"═" * (max_sentence + indent * 2)}╝'  # lower_border
	return box

save_game_state = lambda : game_player.save_player_data_json(player_name=player_name, player_location=game_map.ret_player_location())


#----------------
# INITIALIZATION
#----------------
player_data = get_player_data()

#-----------------------
# MAIN GAME STARTS HERE
#-----------------------
print(border_msg(["⚔Welcome to Da RPG Gaem⚔", "select option:", "a: Play", "b: Quit Game"]))

while True:
	#-----------MAIN MENU-----------#
	choice = input()

	#------------
	# GAME STARTS
	#------------
	if choice == 'a' or choice == 'play' or choice == '2':
		player_name = input("Enter Player Name: ")

		#-------------
		# Checks login
		#-------------

		game_player = player_login(player_name=player_name, player_data=player_data)
		
		#-----------EXIT GAME - LOGIN FAILED-----------#
		if game_player == "leave":
			print("Cya bruh. Peace out.")
			exit()

		#------------------------
		# ACTUAL GAME STARTS HERE
		#------------------------
		game_shop = rpg_shop.shop(game_player)
		game_map = rpg_map.rpg_map(game_player)
		main_game_map()

		break

	#-----------QUIT GAME - CHOICE = B-----------#
	if choice == 'b' or choice == 'quit' or choice == 2:
		print("You quit the game, Cya!")
		break
