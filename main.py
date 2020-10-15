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

#------------
# FUNCTIONS
#------------
def main_game_map():
	while True:
		print(map.draw_map())
		dir = input("enter direction: ")
		if dir == "w" or dir == "a" or dir =='s' or dir == 'd':

			#-----------Using Directions[dir] to convert into proper directions-----------#
			#---------------Checks if the direction entered has enemy on it---------------#
			if map.check_player_movement(directions[dir]) == "enemy":
				system("cls")
				enemy_encounter()
				break
			
			elif map.check_player_movement(directions[dir]) == "chunk_move":
				map.global_chunk_move(directions[dir])

			else:
				print(map.player_move(directions[dir]))
				game_player.save_player_data_json(player_name=player_name, player_location=map.ret_player_location())
		
		#-----------Player types Q, so quit the game-----------#
		elif dir == "q":
			print("quit the game")
			game_player.save_player_data_json(player_name=player_name, player_location=map.ret_player_location())
			exit()

		elif dir == "map":
			print(map.ret_player_location())
			continue

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
	while True:
		print("Enemy Encountered")
		print("your stats: \n")
		player_stats()
		break

	main_game_map()

def player_stats():
	print(f"health: {game_player.player_health}")
	print(f"money: {game_player.player_money}")

def enemy_stats(enemy):
	print(f"health: {enemy.health}")

def get_player_data():
	with open ("game_files/other_files/player.json") as p:
		return json.load(p)

#----------------
# INITIALIZATION
#----------------
player_data = get_player_data()

#-----------------------
# MAIN GAME STARTS HERE
#-----------------------
print("⚔Welcome to Da RPG Gaem⚔")
print("select option:")
while True:
	#-----------MAIN MENU-----------#
	print("a: Play\nb: Quit Game")
	choice = input()

	#-----------CHOICE = A (PLAY)-----------#
	if choice == 'a' or choice == 'play' or choice == '2':
		player_name = input("Enter Player Name: ")
		login_failed = True

		#-----------CHECK IF PLAYER EXISTS-----------#
		#-----------PLAYER EXISTS - LOGIN-----------#
		if player_name in [player for player in player_data]:

			#while loop to keep asking password
			while login_failed == True:
				password = input("Enter Password: ")

				#------------check password given-------------#
				if password == player_data[player_name]["password"]:
					#Password matches, continue with game
					login_failed = False
					game_player = player.player(player_name=player_name, exists=True)
					break

				#Password doesn't match
				else:
					print(f"Player name and Password don't match!")
					enter_pass_again = input("Do you want to try again?\ny: Yes\nn: No\n")

					#Try again - Yes
					if enter_pass_again == 'Yes' or enter_pass_again == 'y' or enter_pass_again == 'yes':
						login_failed = True
						continue

					#Try again - No
					elif enter_pass_again == 'No' or enter_pass_again == 'n' or enter_pass_again == 'no':
						print("Okay, Bbye!")
						login_failed = True
						break

					#Try again - Not Valid
					else:
						print("Enter a valid choice")
						login_failed = True
						continue

		#-----PLAYER DOESNT EXISTS (CREATE NEW)------#
		elif player_name not in [player for player in player_data]:
			while True:
				create_new_acc = input(f"{player_name} does not exist, create a new player?\ny: Yes\nn: No\n")
				#-----------CREATE ACC - YES-----------#
				if create_new_acc == 'yes' or create_new_acc == 'y' or create_new_acc == 'Yes':
					password = input("Enter a P4$$w0rd: ")
					game_player = player.player(player_name=player_name, exists=False, password=password)
					print(f"Welcome {player_name}")
					player_data = get_player_data()
					login_failed = False
					break
				#-----------CREATE ACC - NO------------#
				elif create_new_acc == "no" or create_new_acc == "n" or create_new_acc == "No":
					print("BBye!")
					break

				#-----------Create ACC - Enter Valid ---#
				else:
					print("Enter a valid option ples!")
					continue
		
		#-----------EXIT GAME - LOGIN FAILED-----------#
		if login_failed == True:
			exit()

		#-----------------------
		# ACTUAL GAME STARTS HERE
		#-----------------------
		# print(game_player.player_location)

		map = rpg_map.map(game_player)

		main_game_map()

		break

	#-----------QUIT GAME - CHOICE = B-----------#
	if choice == 'b' or choice == 'quit' or choice == 2:
		print("You quit the game, Cya!")
		break
