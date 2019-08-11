import re
import Dueler
class Duel:
	def run_round(self,dueler1,dueler2,round):
		roundmessage = "\n \n ____ \n \n  **Round {}** \n \n \n ".format(round)
		roll1 = dueler1.attack_roll()
		roll2 = dueler2.attack_roll()
		roundmessage += "**{}** Roll: {} ({:+}) Health: {}\n \n".format(dueler1.name,roll1-dueler1.bonus,dueler1.bonus,dueler1.health)
		roundmessage += "**{}** Roll: {} ({:+}) Health: {}\n \n".format(dueler2.name,roll2-dueler2.bonus,dueler2.bonus,dueler2.health)
		if(roll1 > roll2):	
			roundmessage += dueler2.take_damage(roll1-roll2)
			if(roll1-roll2 > 20):
				dueler1.bonus += 5
		else:
			roundmessage += dueler1.take_damage(roll2-roll1)
			if(roll2-roll1 > 20):
				dueler2.bonus += 5
		return roundmessage
	def run(self,duelinfo):
		battlemessage = ""
		round = 1
		dueler1 = Dueler.Dueler(duelinfo.group(1),int(duelinfo.group(2)),int(duelinfo.group(3)))
		dueler2 = Dueler.Dueler(duelinfo.group(4),int(duelinfo.group(5)),int(duelinfo.group(6)))
		while(dueler1.continuefighting and dueler2.continuefighting):
			battlemessage += self.run_round(dueler1,dueler2,round)
			round += 1
		return battlemessage	
	
			
		