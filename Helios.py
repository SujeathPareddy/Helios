from Phaethon import *

Romans=SuperFaction("Romans")
Hannibal=SuperFaction("Hannibal")
Carthaginians=SuperFaction("Carthaginians")

Romans.addEnemy(Hannibal)
Romans.addEnemy(Carthaginians)
Hannibal.addEnemy(Carthaginians)

Greeks=Faction("Greeks",Romans)

RomesProvince=Province("RomansProvince",Romans)
CarthagesProvince=Province("CarthaginiansProvince",Carthaginians)
AthenasProvince=Province("AthenasProvince",Greeks)

Rome=City("Rome",RomesProvince,Romans)
Carthage=City("Carthage",CarthagesProvince,Carthaginians)
Athens=City("Athens",AthenasProvince,Greeks)

Romans.capital=Rome
Carthaginians.capital=Carthage
Greeks.capital=Athens

RomeExpress=Route([],Rome,Carthage,[RomesProvince,CarthagesProvince])
VictoryRoad=Route([],Rome,Athens,[RomesProvince,AthenasProvince])

FishMax=SeaRoute([],Carthage,Athens)

GA=GraphAnalyser()

print(RomeExpress.passesThrough(RomesProvince))
print(RomeExpress.passesThrough(CarthagesProvince))
print(RomeExpress.passesThrough(AthenasProvince))
print(VictoryRoad.passesThrough(AthenasProvince))
print(VictoryRoad.passesThrough(CarthagesProvince))
print(FishMax.isBlockedFor(Romans))

print(GA.unblockedFrom(Romans,CarthagesProvince))