class person:
# Character class. Everything related to the player, or player
# controlled characters, goes in here. The idea is that, eventually,
# you'll be able to control more than one character in battle
	def __init__(self, **plattr):
		self.name = plattr.get('name', "Unknown Ninja")
		self.prof = plattr.get('prof', "Warrior")
		self.hp = plattr.get('hp', 20)
		self.mp = plattr.get('mp', 10)
		self.sta = plattr.get('sta', 10)
		self.spd = plattr.get('spd', 5)
		# CND relates to CONDITION, I'm thinking 0 for no condition,
		# 1 for poisoned... and so on.
		self.cnd = plattr.get('cnd', 0)
		self.atkpwr = plattr.get('atkpwr', 1.0)
		self.defpwr = plattr.get('defpwr', 1.0)
		self.healpwr = plattr.get('healpwr', 1.0)
		self.wearing = []*6
		self.bag = []




class item:
# Item class. Everything a consumable item can do is defined here,
# so that different items with different sets of effects can be made.
# That is, an item that can restore mp, but in turn makes your healing
# spells less effective.
# This class is not used only to make potions, but instead it makes all
# consumable items. - I'm looking at you, cheese wheel.
	def __init__(self, **effects):
		self.name = effects.get('name', "Unknown Potion")
		self.desc = effects.get('desc', "This potion's effects are unknown")
		self.hpeff = effects.get('hpeff', 0)
		self.mpeff = effects.get('mpeff', 0)
		self.staeff = effects.get('staeff', 0)
		self.spdeff = effects.get('spdeff', 0)
		self.atkpwreff = effects.get('atkpwreff', 0)
		self.defpwreff = effects.get('defpwreff', 0)
		self.healpwreff = effects.get('healpwreff', 0)
		
	def itemUse(self):
		party[sel].hp += self.hpeff
		party[sel].mp += self.mpeff
		party[sel].sta += self.staeff
		party[sel].spd += self.spdeff
		party[sel].atkpwr += self.atkpwreff
		party[sel].defpwr += self.defpwreff
		party[sel].healpwr += self.healpwreff
		


class wearable:
# This class creates all wearable items and defines all the effects
# it has on its user.
	def __init__(self, **itattr):
		self.name = itattr.get('name', "Unknown Item")
		self.kind = itattr.get('kind', 0)
		# Kinds:
		# 0 = Weapon
		# 1 = Helmet
		# 2 = Chest Piece
		# 3 = Leg Piece
		# 4 = Boots
		# 5 = Amulet
		# These align with the list in the person class.
		self.hpdiff = itattr.get('hpdiff', 0)
		self.mpdiff = itattr.get("mpdiff", 0)
		self.stadiff = itattr.get('stadiff', 0)
		self.spddiff = itattr.get('spddiff', 0)
		self.atkpwrdiff = itattr.get('atkpwrdiff', 0)
		self.defpwrdiff = itattr.get('defpwrdiff', 0)
		self.healpwrdiff = itattr.get('healpwrdiff', 0)

