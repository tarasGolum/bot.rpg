from functions import *
from bot import Bot
from colors import bcolors
import winsound

import random

class Melee(Bot):
	ATTACKS_LIMIT_BEFORE_TURN = 3

	def loop(self, stop_event):
		attacks = 0

		while not stop_event.is_set():

			player_hp = self.get_player_hp()
			targeted_hp = self.get_targeted_hp()

			if player_hp < 80:
				self.regenerateHp()

			if player_hp < 40:
				winsound.Beep(404, 1000)

			if targeted_hp > 0:
				print(bcolors.OKBLUE, 'target hp', targeted_hp, '%', bcolors.ENDC)
				self.useless_steps = 0

				if self.isStacked() and self.get_targeted_hp() > 98:
					print(bcolors.BOLD, 'go somewhere', bcolors.ENDC)
					self.go_somewhere()
					time.sleep(1)
					print(bcolors.BOLD, 'turn', bcolors.ENDC)
					self.turn()
					attacks = 0

				if attacks > 10 and targeted_hp > 98:  # bad
					self.autohot_py.F5.press()
					time.sleep(0.3)
					self.autohot_py.F1.press()
					attacks = 0

				print(bcolors.OKGREEN, "attack the target", bcolors.ENDC)
				self.autohot_py.F1.press()
				attacks += 1
				continue
			elif targeted_hp == 0:
				# self.get_player_hp_difference()
				print( "target is dead, find another")
				self.pickUpDrop()
				self.autohot_py.F5.press()
				time.sleep(0.3)
				self.autohot_py.F1.press()

				if self.get_targeted_hp():
					continue
				self.set_target()

				continue
			else:
				print("no target yet")
				# Find and click on the victim
				self.useless_steps = 0
				print("define target")
				self.set_target()

		print("loop finished!")

	#
	def set_target(self):
		self.autohot_py.F6.press()
		# random_target = int(random.randrange(0, 2))
		random_target = bool(random.getrandbits(1))

		if random_target:
			self.autohot_py.F6.press()
		elif random_target == 2:
			self.autohot_py.F8.press()
		else:
			self.autohot_py.F7.press()

		# if self.get_targeted_hp() <= 0:
		# 	self.set_target()
		# self.pickUpDrop()
		# self.autohot_py.F2.press() # dash



	def regenerateHp(self):
		self.autohot_py.F3.press() # potion

		# hp1	= self.get_player_hp()
		# time.sleep(1)
		# hp2	= self.get_player_hp()
		#
		# if  hp2 < hp1:
		# 	print(bcolors.FAIL, 'cant regen hp, under attack!', bcolors.ENDC)
		#
		# 	while True:
		# 		self.autohot_py.F5.press()
		#
		# 		if self.get_targeted_hp():
		# 			while self.get_targeted_hp():
		# 				self.autohot_py.F1.press()
		# 				time.sleep(0.75)
		# 		else:
		# 			break
		#
		# self.pickUpDrop() # in case if it was a fight

		# print(bcolors.OKGREEN, 'regenerating hp', bcolors.ENDC)
		# self.autohot_py.F11.press()
		#
		# hp = self.get_player_hp()
		# while hp < 90:
		# 	hp = self.get_player_hp()
		# 	print(bcolors.OKBLUE, 'hero hp -', bcolors.BOLD, int(hp), bcolors.ENDC)
		# 	time.sleep(3)
		# self.autohot_py.F11.press()


	def pickUpDrop(self):
		print(bcolors.OKGREEN, "picking up drop", bcolors.ENDC)
		for i in range(5):
			self.autohot_py.F4.press()
			time.sleep(0.5)

	def get_player_hp_difference(self):
		player_hp1 = self.get_player_hp()
		self.pickUpDrop()
		player_hp2 = self.get_player_hp()

		if player_hp1 < player_hp2:
			self.autohot_py.F5.press()
			time.sleep(0.3)
			self.autohot_py.F1.press()

