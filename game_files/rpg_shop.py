import random

class shop():
    items = {
        "apple": 10,
        "potion": 20,
    }

    player_money = 0
    player_backpack = {}

    def __init__(self, player:object):
        self.player_money = player.player_money
        self.player_backpack = player.player_backpack

    def buy_item(self, buy_item: str, amt=1):
        #TODO add money system to reduce money
        
		# If the item given is not in shop's items.
		if buy_item not in self.items:
			return "Item doesn't exist"
		
		# Player doesn't have enuff money
		if not self.player_money >= self.items[buy_item]:
			return "Not enough money"
		
		# Take the player's money.	
		self.player_money -= self.items[buy_item]
		print(self.player_money)
		
		# If player doesn't already have item, create the item
		if buy_item not in self.player_backpack:
			self.player_backpack[buy_item] = amt
						
		# else just add the item to the the backpack
		else:
			self.player_backpack[buy_item] += amt
		return f"Item bought! You now have {self.player_backpack[buy_item]} of {buy_item}"

    def sell_item(self, sell_item: str, amt=1):
		if sell_item not in self.items:
			return "Item cannot be bought"
        
		if sell_item not in self.player_backpack:
			return "You don't have the item. WTF?"
		
		if not self.player_backpack[sell_item] >= amt:
			return "You don't have enough item. bRuh"
			
		self.player_backpack[sell_item] -= amt
		self.player_money += items[sell_item]
		return f"Item Sold. You now have {self.player_backack[sell_item]} of {sell_item}"
			
	#TODO Add save system, that exports - Player_backpack and player_money :D
	def ret_money_backpack(self):
	   return self.player_money, self.player_backpack