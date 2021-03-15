import random

COLORS = ["blue", "green", "red"]
ANIMALS = ["cat", "dog", "tiger"]

class Character:

	curr_hp = 0

	def __init__(self, name, level):
		self.name = name
		self.max_hp = random.randint(5, 10)*level
		self.curr_hp = self.max_hp
		self.atk = random.randint(1, 5)*level
		self.res = random.randint(1, 5)*level

	def __str__(self):
		hp = str(self.curr_hp)+"/"+str(self.max_hp)
		return f"{self.name.ljust(12)}  HP:{hp.rjust(5)}  ATK:{str(self.atk).rjust(2)}  DEF:{str(self.res).rjust(2)}"

	def getStatus(self):

		print(self.name)
		print("-"*10)
		print("HP:   ", f"{self.curr_hp}/{self.max_hp}")
		print("Attack:\t", self.atk)
		print("Defense:", self.res)

	def getAttackDamage(self, other):
		return self.atk - other.res if self.atk - other.res > 0 else 0

	def attack(self, other, protocol):
		other.curr_hp -= self.getAttackDamage(other)

	def isAlive(self):
		return self.curr_hp > 0

class Weasel(Character):
	
	pass

class Enemy(Character):

	def __init__(self, level):
		self.color = random.choice(COLORS)
		self.species = random.choice(ANIMALS)
		name = self.color + " " + self.species 
		super().__init__(name, level)

def spawnEnemies(how_many, level=1):
	return [Enemy(level) for i in range(how_many)]

def removeDead(enemies):
	"""
	for enemy in enemies:
		if not enemy.isAlive():
			enemies.remove(enemy)
	return enemies
	"""
	return [enemy for enemy in enemies if enemy.isAlive()]
