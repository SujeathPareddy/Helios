import networkx as nx

superFactions=[]
routes=[]
seaRoutes=[]

def triggerNavalBattle(navies):
		pass

def triggerArmyBattle(armies):
		pass
				
class Faction:#A faction represents a side in the war, due to asymmetries in the faction game mechanics,
			  #it would be better to inherit different sides in a hierarchy 
		def __init__(self,capital,cities):
				self.cities=cities
				self.capital=capital

class SuperFaction(Faction):#Roman, Hannibal or Carthage
		pass
				
class Route:
		def __init__(self,points,A,B,provinces):#Provinces is a list of provinces that the route passes through
				self.A=A
				self.B=B
				self.provinces
				
		def passesThrough(province):
				if province in self.provinces:
						return True
				else:
						return False
		
		def isBlockedFor(superFaction):
				for province in self.provinces:
						if province.occupying.alleigance in superFaction.enemies:
								return False
				return True
		
class SeaRoute:
		def __init__(self,points,A,B):
				self.A=A
				self.B=B
				self.navies={i:[] for i in superFactions}
			
		def addNavy(navy):
				if navy not in self.navies:
						self.navies[navy.faction].append(navy)
				navyPresence=0
				for side in self.navies:
						if len(self.navies[side])>0:
								armyPresence+=1
				if navyPresence>1:
						triggerNavalBattle(self.navies)
		
		def isBlockedFor(superFaction):
				for side in superFaction.enemies:
						if len(self.navies[side])>0:
								return False
				return True
				
class GraphAnalyser:
			def __init__(self,routes,seaRoutes):
					self.routes=routes+seaRoutes
			
			def unblockedFrom(recrutingSuperFaction,recruitingRegion):
					G=nx.MultiGraph()
					G.add_edges_from([(route.A,route.B) for route in self.routes if not route.isBlockedFor(recruitingSuperFraction)])
					return any(G.has_path(recruitingSuperFaction.capital,region) for region in recruitingRegion.cities)
					
			
					
					
					