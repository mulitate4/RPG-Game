
import random
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