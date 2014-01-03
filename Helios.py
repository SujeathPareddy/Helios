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

Rome=City("Rome",RomesProvince,Romans,manPower=1000,capital=True)
Carthage=City("Carthage",CarthagesProvince,Carthaginians,manPower=1000,capital=True)
Athens=City("Athens",AthenasProvince,Greeks,manPower=1000,capital=True)

RomeExpress=Route([],Rome,Carthage,[RomesProvince,CarthagesProvince])
VictoryRoad=Route([],Rome,Athens,[RomesProvince,AthenasProvince])

FishMax=SeaRoute([],Carthage,Athens)

GA=GraphAnalyser()

Romans.addAlly(Carthaginians)
Romans.recruitArmy(Carthaginians,{'Foot Soldiers':100})
Romans.recruitArmy(Carthaginians,{'Elephants':100})
Romans.recruitNavy(Carthaginians,{'Brigs':5})
triggerBattle(armies+navies)
import pdb
pdb.set_trace()