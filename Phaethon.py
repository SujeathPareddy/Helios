import networkx as nx
from math import sqrt
from random import gauss
import itertools

superFactions=[]
factions=[]
routes=[]
provinces=[]
seaRoutes=[]
cities=[]
armies=[]
navies=[]

def isOnLand(newX,newY):
		return True

def isOnWater(newX,newY):
		return True

def triggerBattle(List):
		k=0
		flag=False
		for k,i in enumerate(List):
				print("%d=%s:%s"%(k,i.faction,str(i)))
		while True:
				try:
						winner=[int(i) for i in input("Enter the winner(s)").split()]
						print(winner)
				except Exception as ex:
						print(ex)
						continue
				if not all(0<=i<=k for i in winner):
						continue 
				temp=[List[i] for i in range(k+1) if i not in winner]
				for i in temp:
						i.destroy()
				break
						
		
class Faction:
		def __init__(self,name,money=0):
				self.name=name
				self.capital=None
				self.province=None
				self.cities=[]
				self.neutral=[]
				self.allies=[]
				self.enemies=[]
				factions.append(self)#@global
				self.armies=[]
				self.navies=[]
				self.money=money

		def getManPower(self):
				return sum(map(lambda city:city.manPower,self.cities))

		def getTribute(self):
				pass
				
		def destroySelf(self):
				pass

		def changeCapital(self,capital):
				self.capital = capital
				
		def __str__(self):
				return self.name
				
		def addEnemy(self,enemy):
				if enemy in self.enemies:
						return
				if enemy in self.allies:
						self.allies.remove(enemy)
				elif enemy in self.neutral:
						self.neutral.remove(enemy)
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
				
		def recruitFrom(self,recruiter,troops,cue):#Troops is a dict, E.g. {"Iberian Foot Soldiers":100,"War Elephants":15,...}
				if recruiter in self.enemies:
						return False
				number=sum(troops.values())
				mp=self.getManPower()
				fractions=list(map(lambda x:x.manPower/mp,self.cities))
				for i in range(len(self.cities)):
						self.cities[i].manPower-=fractions[i]*number
						if self.cities[i].manPower<0:
								return False
				if cue:
						Army(self.capital.geoX,self.capital.geoY,recruiter,troops)
				else:
						Navy(self.capital.geoX,self.capital.geoY,recruiter,troops)
				return True
				
		def recruitArmy(self,target,troops):
				target.recruitFrom(self,troops,True)
		
		def recruitNavy(self,target,troops):
				target.recruitFrom(self,troops,False)
				
		def __str__(self):
				return self.name
				
		def sackCity(self,city):
				self.money+=city.sack()
				
		def destroyCity(self,city):
				self.money+=city.money
				city.destroy()
		
		def captureCity(self,city):
				city.money*=0.4
				city.manPower*=0.4
				city.defect(self)
				
		def evalStatus(self):
				print(self.name)
				if len(self.cities)==0:
						print("%s has lost"%self.name)
						self.destroySelf()

class SuperFaction(Faction):
		def __init__(self,name,money=0):
				self.name=name
				self.neutral=[]
				self.allies=[]
				self.enemies=[]
				self.capital=None
				self.cities=[]
				self.armies=[]
				self.navies=[]
				self.province=None
				self.money=money
				superFactions.append(self)#@global

class Province:
		def __init__(self,name,occupying):
				self.name=name
				self.occupying=occupying
				self.cities=[]
				occupying.cities=self.cities
				occupying.province=self#@upper
				provinces.append(self)#@global
				
		def __str__(self):
				return self.name

class City:
		def __init__(self,name,province,alleigance,geoX=0,geoY=0,manPower=0,money=0,capital=False,garrison=None,garrisonCost=0):
				self.name=name
				self.province=province
				province.cities.append(self)#@upper
				self.alleigance=alleigance
				self.geoX=geoX
				self.geoY=geoY
				self.manPower=manPower
				self.money=money
				self.destroyed=False
				self.besieged=False
				self.siegeFaction=None
				self.navyAssist=False
				self.moneyCoefficient=1.0
				self.manPowerCoefficient=1.0
				self.capital=capital
				if capital:
						alleigance.capital=self
				if garrison is None:
						self.garrison=int(gauss(self.manPower/10,self.manPower/100))
				else:
						self.garrison=garrison
				self.money-=garrisonCost
				cities.append(self)#@global

		def besiege(self,army):
				self.besieged=True
				self.siegeFaction=army.faction
				self.siegeArmy=army
				self.moneyCoefficient*=0.33
				self.manPowerCoefficient*=0.33

		def siegeIter(self):
				if self.navyAssist:
						self.moneyCoefficient-=0.105
						self.manPowerCoeffcient-=0.105
				else:
						self.moneyCoefficient-=0.166
						self.manPowerCoefficient-=0.166
				if self.moneyCoefficient<=0.0 or self.manPowerCoefficient<=0.0:
						print("%s is defeated"%self.name)

		def desiege(self):
				self.besieged=False
				self.moneyCoefficient=1.0
				self.manPowerCoefficient=1.0
				self.siegeFaction=None
				self.siegeArmy=None
				self.navyAssist=False

		def destroy(self):
				print("%s is Destroyed"%self.name)
				self.destroyed=True
				self.besieged=True
				self.money=0
				self.manPower=0
				self.siegeFaction=None
				self.siegeArmy=None
				self.navyAssist=False
				self.alleigance.evalStatus()

		def sack(self):
				print("%s is Sacked"%self.name)
				self.money*=0.4
				return self.money*0.6/0.4
				
		def defect(self,other):
				if self.capital:
						self.alleigance.capital=None
				self.capital=False
				self.alleigance.cities.remove(self)
				self.alleigance.evalStatus()
				self.alleigance=other
				other.cities.append(self)
				if self.besieged:
						self.desiege()
						
		def addToGarrison(number,cost):
				self.garrison+=number
				self.money-=cost
				
		def __str__(self):
				return self.name

class Route:
		def __init__(self,name,points,A,B,provinces):#Provinces is a list of provinces that the route passes through
				self.name=name
				self.points=points
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
				if self.A.seigeFaction in superFaction.enemies or self.B.seigeFaction in superFaction.enemies:
						return True
				if any(province.occupying in superFaction.enemies for province in self.provinces):
						return True
				return False
				
		def __str__(self):
				return self.name

class SeaRoute:
		def __init__(self,name,points,A,B):
				self.name=name
				self.points=points
				self.A=A
				self.B=B
				self.navies={i:[] for i in itertools.chain(superFactions,factions)}
				seaRoutes.append(self)

		def addNavy(self,navy):
				if navy not in self.navies[navy.faction]:
						self.navies[navy.faction].append(navy)
				navyPresence=0
				for side in self.navies:
						if len(self.navies[side])>0:
								armyPresence+=1
				if navyPresence>1:
						triggerBattle(self.navies)
		
		def isBlockedFor(self,superFaction):
				if superFaction in self.A.alleigance.enemies or superFaction in self.B.alleigance.enemies:
						return True
				if any(len(self.navies[side])>0 for side in superFaction.enemies):
						return True
				return False
				
		def __str__(self):
				return self.name

class GraphAnalyser:
		def __init__(self):
				self.routes=routes+seaRoutes
	
		def unblockedFrom(self,recruitingSuperFaction,recruitingRegion):
				G=nx.MultiGraph()
				G.add_edges_from([(route.A,route.B) for route in self.routes if not route.isBlockedFor(recruitingSuperFaction)])
				return any(nx.has_path(G,recruitingSuperFaction.capital,region) for region in recruitingRegion.cities)
				
class MetaArmy:
		def __init__(self,geoX,geoY,faction,composition):	
				self.geoX=geoX
				self.geoY=geoY
				self.faction=faction
				self.composition
				
		def checkValidMove(self,newX,newY):
				return True
				
		def Battle(self,other):
				triggerBattle([self,other])
				
		def __str__(self):
				return "%s@%f,%f"%(str(self.composition),self.geoX,self.geoY)

class Army(MetaArmy):
		def __init__(self,geoX,geoY,faction,composition):
				self.geoX=geoX
				self.geoY=geoY
				self.faction=faction
				self.ambush=False
				self.sieging=False
				self.composition=composition
				faction.armies.append(self)#@upper
				armies.append(self)#@global
				
		def destroy(self):
				armies.remove(self)
				self.faction.armies.remove(self)
				
		def move(self,newX,newY):
				if sqrt((newX-self.geoX)**2 + (newY-self.geoY)**2)<100 and isOnLand(newX,newY):
						self.geoX=newX
						self.geoY=newY
				else:
						print("Error, move not valid")
						
		def laySiege(self,city):
				city.besiege(self)
				self.siegeing=True
		
		def removeSiege(self,city):
				city.desiege()
				self.sieging=False
				
		def layAmbush(self):
				self.ambush=True
				
		def removeAmbush(self):
				self.ambush=False
							
class Navy(MetaArmy):
		def __init__(self,geoX,geoY,faction,composition):
				self.geoX=geoX
				self.geoY=geoY
				self.composition=composition
				navies.append(self)
				faction.navies.append(self)#@upper
				self.faction=faction#@global
				
		def destroy(self):
				self.faction.navies.remove(self)
				navies.remove(self)
				
		def move(self,newX,newY):
				if sqrt((newX-self.geoX)**2 + (newY-self.geoY)**2)<100 and isOnWater(newX,newY):
						self.geoX=newX
						self.geoY=newY
				else:
						print("Error, move not valid")