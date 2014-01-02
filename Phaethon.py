import networkx as nx

superFactions=[]
factions=[]
routes=[]
provinces=[]
seaRoutes=[]
cities=[]

def triggerNavalBattle(navies):
		pass

def triggerArmyBattle(armies):
		pass
		
class Faction:
		def __init__(self,name,alleigance):
				self.name=name
				self.capital=None
				self.province=None
				self.cities=[]
				self.alleigance=alleigance
				factions.append(self)#@global

		def getManPower(self):
				return sum(map(lambda city:city.manPower,self.cities))

		def recruit(self,number):
				mp=self.getManPower()
				fractions=map(lambda x:x.manPower/mp,self.cities)
				for i in range(len(self.cities)):
						self.cities[i].manPower-=fraction[i]*number

		def getTribute(self):
				pass
				
		def destroy(self):
				pass

		def changeCapital(self,capital):
				self.capital = capital
				
		def __str__(self):
				return self.name

class SuperFaction(Faction):
		def __init__(self,name):
				self.name=name
				self.neutral=[]
				self.allies=[]
				self.enemies=[]
				self.alleigance=self
				self.capital=None
				self.cities=[]
				self.armies=[]
				self.navies=[]
				self.province=None
				superFactions.append(self)#@global

		def addEnemy(self,enemy):
				if enemy in self.enemies:
						return
				if enemy in self.allies:
						self.allies.remove(enemy)
				elif enemy in self.neutral:
						self.neutral.pop(enemy)
				self.enemies.append(enemy)
				enemy.addEnemy(self)

		def addAlly(self,ally):
				if ally in self.allies:
						return
				if ally in self.enemies:
						self.enemies.remove(ally)
				elif ally in self.neutral:
						self.neutral.remove(ally)
				self.allies.append(ally)
				ally.addAlly(self)
				
		def addNeutral(self,neutral):
				if neutral in self.neutral:
						return
				if neutral in self.enemies:
						self.enemies.remove(neutral)
				elif neutral in self.allies:
						self.allies.remove(neutral)
				self.neutral.append(neutral)
				neutral.addNeutral(self)

class Province:
		def __init__(self,name,occupying):
				self.name=name
				self.occupying=occupying
				self.cities=[]
				occupying.cities=self.cities
				occupying.province=self#@upper
				provinces.append(self)#@global

class City:
		def __init__(self,name,province,alleigance,geoX=0,geoY=0,manPower=0,money=0,capital=False):
				self.name=name
				self.province=province
				province.cities.append(self)#@upper
				self.alleigance=alleigance#Use self.alleigance.alleigance to get superFaction
				self.geoX=geoX
				self.geoY=geoY
				self.manPower=manPower
				self.money=money
				self.destroyed=False
				self.beseiged=False
				if capital:
						alleigance.capital=self
				cities.append(self)#@global

		def besiege(self):
				self.besieged=True
				self.money*=0.33
				self.manPower*=0.33
				self.supply*=0.33

		def desiege(self):
				self.besieged=False
				pass

		def destroy(self):
				self.destroyed=True
				self.money=0
				self.manPower=0

		def sack(self):
				pass

class Route:
		def __init__(self,points,A,B,provinces):#Provinces is a list of provinces that the route passes through
				self.A=A
				self.B=B
				self.provinces=provinces
				routes.append(self)
				
		def passesThrough(self,province):
				if province in self.provinces:
						return True
				else:
						return False
		
		def isBlockedFor(self,superFaction):
				for province in self.provinces:
						if province.occupying.alleigance in superFaction.enemies:
								return False
				return True

class SeaRoute:
		def __init__(self,points,A,B):
				self.A=A
				self.B=B
				self.navies={i:[] for i in superFactions}
				seaRoutes.append(self)

		def addNavy(navy):
				if navy not in self.navies[navy.faction]:
						self.navies[navy.faction].append(navy)
				navyPresence=0
				for side in self.navies:
						if len(self.navies[side])>0:
								armyPresence+=1
				if navyPresence>1:
						triggerNavalBattle(self.navies)
		
		def isBlockedFor(self,superFaction):
				if superFaction in self.A.alleigance.enemies or superFaction in self.B.alleigance.enemies:
						return True
				for side in superFaction.enemies:
						if len(self.navies[side])>0:
								return True
				return False

class GraphAnalyser:
		def __init__(self):
				self.routes=routes+seaRoutes
	
		def unblockedFrom(self,recruitingSuperFaction,recruitingRegion):
				G=nx.MultiGraph()
				G.add_edges_from([(route.A,route.B) for route in self.routes if not route.isBlockedFor(recruitingSuperFaction)])
				return any(nx.has_path(G,recruitingSuperFaction.capital,region) for region in recruitingRegion.cities)
				
class MetaArmy:
		def __init__(self,geoX,geoY,faction):	
				self.geoX=geoX
				self.geoY=geoY
				self.faction=faction

class Army(MetaArmy):
		def __init__(self,geoX,geoY,faction):
				self.geoX=geoX
				self.geoY=geoY
				self.faction=faction
				faction.armies.append(self)#@upper
				armies.append(self)#@global
				
class Navy(MetaArmy):
		def __init__(self,geoC,geoY,faction):
				self.geoX=geoX
				self.geoY=geoY
				navies.append(self)
				faction.navies.append(self)#@upper
				self.faction=faction#@global