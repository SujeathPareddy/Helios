from Phaethon import cities,routes,seaRoutes,armies,navies,factions,superFactions
import itertools
#A SONG is a JSON file (jSONg) that may/may not adhere to IEEE JSON specifications.

def generateSong():
		temp=[]	
		for city in cities:
				temp.append(genSongforCity(city))
		for route in routes:
				temp.append(genSongforRoute(route))
		for seaRoute in seaRoutes:
				temp.append(genSongforSeaRoute(seaRoute))
		for army in armies:
				temp.append(genSongforArmy(army))
		for navy in navies:
				temp.append(genSongforNavy(navy))
		for faction in factions:
				temp.append(genSongforFaction(faction))
		for superFaction in superFactions:
				temp.append(genSongforSuperFaction(superFaction))
		return "\n".join(temp)
				
def genSongforCity(x):
		return """City{
Name:%s
Coords:%d,%d
Allegiance:%s
ManPower:%f
Money:%f
Garrison:%f
isCapital:%d
isDestroyed:%d
isSieged:%d
isAssistedByNavy:%d
MoneyCoefficient:%f
ManPowerCoefficient:%f
}"""%(x.name,x.geoX,x.geoY,x.alleigance.name,x.manPower,x.money,x.garrison,x.capital,x.destroyed,x.besieged,x.navyAssist,x.moneyCoefficient,x.manPowerCoefficient)

def genSongforRoute(x):
		return """Route{
Name:%s
Coords:%s
Blocked:%d
}"""%(x.name,x.points,False)#Need to add trade route blocking mechanism
		
def genSongforSeaRoute(x):
		return """SeaRoute{
Name:%s
Coords:%s
BlockedFactions:%s
}"""%(x.name,x.points,{i.name:x.isBlockedFor(i) for i in itertools.chain(superFactions,factions)})
		
def genSongforArmy(x):
		return """Army{
Coords:%d,%d
Faction:%s
Ambushing:%d
Sieging=%d
Composition:%s
}"""%(x.geoX,x.geoY,x.faction,x.ambush,x.sieging,x.composition)
		
def genSongforNavy(x):
		return """Navy{
Coords:%d,%d
Faction:%s
Composition:%s
}"""%(x.geoX,x.geoY,x.faction,x.composition)
		
def genSongforFaction(x):
		return """Faction{
Name:%s
Allies:%s
Enemies:%s
Neutral:%s
HomeProvince:%s
Money:%f
ManPower:%f
capital:%s
}"""%(x.name,[i.name for i in x.allies],[i.name for i in x.enemies],[i.name for i in x.neutral],x.province,x.money,x.getManPower(),str(x.capital))
		
def genSongforSuperFaction(x):
		return """SuperFaction{
Name:%s
Allies:%s
Enemies:%s
Neutral:%s
HomeProvince:%s
Money:%f
ManPower:%f
Capital:%s
}"""%(x.name,[i.name for i in x.allies],[i.name for i in x.enemies],[i.name for i in x.neutral],x.province,x.money,x.getManPower(),str(x.capital))