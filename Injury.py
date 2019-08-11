import random
def minor_injury():
	with open("minorinj.txt") as file:
		minorinjuries = file.readlines()
		return minorinjuries[random.randint(0,19)]
def severe_injury():
	with open("severeinj.txt") as file:
		severeinjuries = file.readlines()
		return severeinjuries[random.randint(0,19)]
def maiming_injury():
	with open("maiminj.txt") as file:
		maiminginjuries = file.readlines()
		return maiminginjuries[random.randint(0,19)]