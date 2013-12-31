from Phaethon import *

Romans=superFaction("Romans")
Hannibal=superFaction("Hannibal")
Carthaginians=superFaction("Carthaginians")

Romans.addEnemy(Hannibal)
Romans.addEnemy(Carthaginians)
Hannibal.addEnemy(Carthaginians)

superFactions=[Romans,Hannibal,Carthaginians]

RomesProvince=Province(Romans)
CarthagesProvince=Province(Carthaginians)
Athena=Province(Romans)

Rome=City("Rome",RomesProvince,Romans,0,0)
Carthage=City("Carthage",CarthagesProvince,Carthaginians,0,0)
Athens=City("Athens",Athena,Romans,0,0)

Romans.changeCapital(Rome)
Carthaginians.changeCapital(Carthage)

RomeExpress=Route([],Rome,Carthage,[RomesProvince,CarthagesProvince])
VictoryRoad=Route([],Rome,Athens,[RomesProvince,Athena])

FishMax=SeaRoute([],Carthage,Athena)

GA=GraphAnalyser()

print(RomeExpress.passesThrough(RomesProvince))
print(RomeExpress.passesThrough(CarthagesProvince))
print(RomeExpress.passesThrough(Athena))
print(VictoryRoad.passesThrough(Athena))
print(VictoryRoad.passesThrough(CarthagesProvince))
print(FishMax.isBlockedFor(Romans))

print(GA.unblockedFrom(Romans,CarthagesProvince))