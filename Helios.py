from Phaethon import *

Romans=SuperFaction("Romans")
Hannibal=SuperFaction("Hannibal")
Carthaginians=SuperFaction("Carthaginians")

Romans.addEnemy(Hannibal)
Romans.addEnemy(Carthaginians)
Hannibal.addEnemy(Carthaginians)

Greeks=Faction("Greeks")

Greeks.addNeutral(Romans)
Greeks.addAlly(Hannibal)
Greeks.addEnemy(Carthaginians)

RomesProvince=Province("RomansProvince",Romans)
CarthagesProvince=Province("CarthaginiansProvince",Carthaginians)
AthenasProvince=Province("AthenasProvince",Greeks)

Rome=City("Rome",RomesProvince,Romans,manPower=1000,capital=True)
Carthage=City("Carthage",CarthagesProvince,Carthaginians,manPower=1000,capital=True)
Athens=City("Athens",AthenasProvince,Greeks,manPower=1000,capital=True)

RomeExpress=Route("RomeExpress",[],Rome,Carthage,[RomesProvince,CarthagesProvince])
VictoryRoad=Route("VictoryRoad",[],Rome,Athens,[RomesProvince,AthenasProvince])

FishMax=SeaRoute("FishMax",[],Carthage,Athens)

GA=GraphAnalyser()

Romans.addAlly(Carthaginians)
Romans.recruitArmy(Carthaginians,{'Foot Soldiers':100})
Romans.recruitArmy(Carthaginians,{'Elephants':100})
Romans.recruitNavy(Carthaginians,{'Brigs':5})
Carthaginians.recruitArmy(Romans,{'Cavalry':50})
triggerBattle(armies+navies)
Carthaginians.armies[0].laySiege(Athens)

Carthaginians.captureCity(Athens)
