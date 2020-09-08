import random
import time
import json
import player
import rpg_map
import enemies
from os import system

enemy_encountered = False

def main_game():
	while True:
		print(map.draw_map())
		dir = input("enter direction: ")
		if dir == "w":
			if map.check_player_movement("up") == "enemy":
				system("cls")
				print("enemy encountered")
				enemy_encountered = True
				print(enemy_encountered)
				break
			else:
				print(map.player_move("up"))

		elif dir == "a":
			if map.check_player_movement("left") == "enemy":
				system("cls")
				print("enemy encountered")
				enemy_encountered = True
				break
			else:
				print(map.player_move("left"))

		elif dir == "d":
			if map.check_player_movement("right") == "enemy":
				system("cls")
				print("enemy encountered")
				enemy_encountered = True
				break
			else:
				print(map.player_move("right"))

		elif dir == "s":
			if map.check_player_movement("down") == "enemy":
				system("cls")
				print("enemy encountered")
				enemy_encountered = True
				break
			else:
				print(map.player_move("down"))
		elif dir == "q":
			print("quit the game")
			break
		else:
			print ("Enter valid direction with W-up, A-left, S-down, D-right")
		system("cls")

	if enemy_encountered == True:
		enemy_encounter()


def enemy_encounter():
	print("ok")

def stats():
	print(f"health = {game_player.health}")
	print(f"money = {game_player.player_money}")

players = {
	"Mulitate4": "passw0rd"
}

with open ("player.json") as f:
	player_data = json.load(f)

print("⚔Welcome to Da RPG Gaem⚔")
print("select option:")
while True:
	#Main Menu
	print("a: Play\nb: Quit Game")
	choice = input()

	#choice = play/a/2
	if choice == 'a' or choice == 'play' or choice == '2':
		player_name = input("Enter Player Name: ")
		login_failed = True

		#checks if player name exists
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

		#If player name doesnt exist, creates new
		elif player_name not in [player for player in players.keys()]:
			#while loop to break out of - 2
			while True:
				create_new_acc = input(f"{player_name} does not exist, create a new player?\ny: Yes\nn: No\n")
				if create_new_acc == 'yes' or create_new_acc == 'y' or create_new_acc == 'Yes':
					password = input("Enter a P4$$w0rd: ")
					players[player_name] = password
					game_player = player.player(player_name=player_name, exists=False)
					print(f"Welcome {player_name}")
					login_failed = False
					break
				elif create_new_acc == "no" or create_new_acc == "n" or create_new_acc == "No":
					print("BBye!")
					break
				else:
					print("Enter a valid option ples!")
					continue
		
		#exit game if login failed
		if login_failed == True:
			break

		#Game starts here, while loop count - 1
		ch = game_player.player_location["chunk"]
		x = game_player.player_location["x_pos"]
		y = game_player.player_location["y_pos"]
		map = rpg_map.map(ch, x, y)

		'''while True:
			print(map.draw_map())
			dir = input("enter direction: ")
			if dir == "w":
				if map.check_player_movement("up") == "enemy":
					system("cls")
					print("enemy encountered")
					enemy_encountered = True
					print(enemy_encountered)
					break
				else:
					print(map.player_move("up"))

			elif dir == "a":
				if map.check_player_movement("left") == "enemy":
					system("cls")
					print("enemy encountered")
					enemy_encountered = True
					break
				else:
					print(map.player_move("left"))

			elif dir == "d":
				if map.check_player_movement("right") == "enemy":
					system("cls")
					print("enemy encountered")
					enemy_encountered = True
					break
				else:
					print(map.player_move("right"))

			elif dir == "s":
				if map.check_player_movement("down") == "enemy":
					system("cls")
					print("enemy encountered")
					enemy_encountered = True
					break
				else:
					print(map.player_move("down"))
			elif dir == "q":
				print("quit the game")
				break
			else:
				print ("Enter valid direction with W-up, A-left, S-down, D-right")
			system("cls")
		'''
		main_game()

		break

	#Quit the game
	if choice == 'b' or choice == 'quit' or choice == 2:
		print("You quit the game, Cya!")
		break
