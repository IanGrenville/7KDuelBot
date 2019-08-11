import random
import Injury
class Dueler:
	name = ""
	bonus = 0
	health = 100
	yieldthreshold = 0
	continuefighting = True
	def __init__(self,name,bonus,yieldthreshold):
		self.name = name
		self.bonus = bonus
		self.yieldthreshold = yieldthreshold
	def attack_roll(self):
		return random.randint(1,60) + self.bonus
	def take_damage(self,damage):
		message = "{} is hit for {} damage".format(self.name,damage)
		self.health -= damage
		if(self.health < -20):
			message += " and dies.\n \n"
			self.continuefighting = False
		elif(self.health > 0 and self.health < self.yieldthreshold):
			message += " and yields.\n \n"
			self.continuefighting = False
		elif(damage > 45 or self.health < 0):
			message += "  and is severely injured, maimed or killed. They are forced to surrender. \n \n"
			roll = random.randint(1,20)
			message += "Roll of {}: \n \n".format(roll)
			if(roll >= 8):
				message+= "They are severely injured, suffering (a) {} \n".format(Injury.severe_injury())
			elif(roll > 1):
				message+= "They are maimed, suffering (a) {} \n".format(Injury.maiming_injury())
			else:
				message+= "They die"
			self.continuefighting = False
		elif(damage > 20 and self.continuefighting):
			message += " suffering a minor injury of: {} \n".format(Injury.minor_injury())
		return message