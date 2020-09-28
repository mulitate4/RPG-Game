#----------------
# MODULE IMPORTS
#----------------
import random
import time
import json
from os import system

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

#------------
# FUNCTIONS
#------------
def main_game_map():
	enemy_encountered = False
	while True:
		print(map.draw_map())
		dir = input("enter direction: ")
		if dir == "w":
			if map.check_player_movement("up") == "enemy":
				system("cls")
				enemy_encountered = True
				break
			else:
				print(map.player_move("up"))

		elif dir == "a":
			if map.check_player_movement("left") == "enemy":
				system("cls")
				enemy_encountered = True
				break
			else:
				print(map.player_move("left"))

		elif dir == "d":
			if map.check_player_movement("right") == "enemy":
				system("cls")
				enemy_encountered = True
				break
			else:
				print(map.player_move("right"))

		elif dir == "s":
			if map.check_player_movement("down") == "enemy":
				system("cls")
				enemy_encountered = True
				break
			else:
				print(map.player_move("down"))
				
		elif dir == "q":
			print("quit the game")
			game_player.save_player_data_json(player_name=player_name)
			break

		else:
			print ("Enter valid direction with W-up, A-left, S-down, D-right")
		system("cls")

	if enemy_encountered == True:
		enemy_encounter()

def enemy_encounter():
	while True:
		print("Enemy Encountered")
		print("your stats:")
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

		#-----------CHECK FOR PLAYER EXISTS-----------#
		if player_name in [player for player in player_data]:

			#while loop to keep asking password
			while login_failed == True:
				password = input("Enter Password: ")

				#check password given
				if password == player_data[player_name]["password"]:
					#Password matches, continue with game
					login_failed = False
					game_player = player.player(player_name=player_name, exists=True)
					break
				else:
					#Password doesn't match
					print(f"Player name and Password don't match!")
					enter_pass_again = input("Do you want to try again?\ny: Yes\nn: No\n")
					if enter_pass_again == 'Yes' or enter_pass_again == 'y' or enter_pass_again == 'yes':
						login_failed = True
						continue
					elif enter_pass_again == 'No' or enter_pass_again == 'n' or enter_pass_again == 'no':
						print("Okay, Bbye!")
						login_failed = True
						break
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
				#-----------CREATE ACC - NO-----------#
				elif create_new_acc == "no" or create_new_acc == "n" or create_new_acc == "No":
					print("BBye!")
					break
				else:
					print("Enter a valid option ples!")
					continue
		
		#-----------EXIT GAME - LOGIN FAILED-----------#
		if login_failed == True:
			break

		#-----------ACTUAL GAME STARTS HERE-----------#
		ch = game_player.player_location["chunk"]
		x = game_player.player_location["x_pos"]
		y = game_player.player_location["y_pos"]
		map = rpg_map.map(ch, x, y)

		main_game_map()

		break

	#-----------QUIT GAME - CHOICE = B-----------#
	if choice == 'b' or choice == 'quit' or choice == 2:
		print("You quit the game, Cya!")
		break
