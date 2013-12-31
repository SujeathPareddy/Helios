import networkx as nx

superFactions=[]
routes=[]
seaRoutes=[]#Variables

def triggerNavalBattle(navies):
		pass

def triggerArmyBattle(armies):
		pass
				
class Faction:  
		def __init__(self,capital,cities):
        		self.capital = capital 
                self.cities = [capital]+cities
				
		def getManPower(self):
				return sum(map(lambda city:city.manPower,self.cities))
				
		def recruit(self,number):
				mp=self.getManPower()
				fractions=map(lambda x:x.manPower/mp,self.cities)
				for i in range(len(self.cities)):
						self.cities[i].manPower-=fraction[i]*self.cities[i].manPower

		def getTribute(self):
				pass
				
		def destroy(self):
				pass
		
        def changeCapital(capital):
				self.capital = capital

class City:
		 def __init__(self,province,alleigance,geoX,geoY,manPower=0,money=0):
				self.manPower=manPower
				self.money=money            
				self.province=province
				self.geoX=geoX
				self.geoY=geoY
				self.alleigance=alleigance
				self.destroyed=False
				self.beseiged=False

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

class superFaction(Faction):
         def __init__(self,allies,enemies):
				self.allies=[]
				self.enemies=[]
				self.armies=[]
				self.navies=[]

class Province:
		def __init__(self):
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
					G.add_edges_from([(route.A,route.B) for route in self.routes if not route.isBlockedFor(recruitingSuperFaction)])
					return any(G.has_path(recruitingSuperFaction.capital,region) for region in recruitingRegion.cities)				