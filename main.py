import random
import characters
import fight

enemies = characters.spawnEnemies(3)
player = characters.Weasel("Harry", 1)
protocol = fight.Protocol()

move = None
while move not in ["A", "F"]:

	fight.cls()
	enemies = characters.removeDead(enemies)

	print("Your enemies:")
	for i, enemy in enumerate(enemies): print(str(i+1)+".", enemy)

	print()

	print("Your status:")
	player.getStatus()

	if protocol:
		print()
		print("Fight protocol:")
		for i in protocol:
			print(i)

	for enemy in enemies:
		if enemy.isAlive():
			break
	else:
		print("You won!")
		break


	print()
	print("What do you want to do?")
	print("\t (A)ttack!")
	print("\t (F)lee!")

	move = input("Your choice: ")

	if move == "A":
		print("Who do you want to attack? Enter number.")
		
		target = None
		while True:
			target = input("Your target: ")
			if not target.isnumeric() or int(target)-1 not in range(len(enemies)):
				print("this is not a valid target! try again.")
				continue
			target = int(target)-1

			protocol.append(f"\tAttacking {enemies[target].name}!")
			protocol.append(f"\tDealt {player.getAttackDamage(enemies[target])} damage!")

			enemies[target].curr_hp -= player.getAttackDamage(enemies[target])
			if not enemies[target].isAlive():
				protocol.append(f"\tEnemy ({enemies[target].name}) dies!")
			move = None
			target = None
			break


	elif move == "F":
		if random.random() >= 0.5:
			print("You fleed succesfully!")
			break
		else:
			protocol.append("Fleeing failed!")
			move = None
			continue

	else:
		pass
		#protocol.append("I dont understand.")
