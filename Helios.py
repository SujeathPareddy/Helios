from Phaethon import *
from Song import *

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

Rome=City("Rome",RomesProvince,Romans,geoX=0,geoY=0,manPower=1000,money=500,capital=True)
Carthage=City("Carthage",CarthagesProvince,Carthaginians,geoX=50,geoY=0,manPower=1000,money=500,capital=True)
Athens=City("Athens",AthenasProvince,Greeks,geoX=50,geoY=50,manPower=1000,money=500,capital=True)

RomeExpress=Route("RomeExpress",[],Rome,Carthage,[RomesProvince,CarthagesProvince])
VictoryRoad=Route("VictoryRoad",[],Rome,Athens,[RomesProvince,AthenasProvince])

FishMax=SeaRoute("FishMax",[],Carthage,Athens)

GA=GraphAnalyser()

Romans.addAlly(Carthaginians)
Romans.recruitArmy(Carthaginians,{'Foot Soldiers':100})
Romans.recruitArmy(Carthaginians,{'Elephants':100})
Romans.recruitNavy(Carthaginians,{'Brigs':5})
Carthaginians.recruitArmy(Romans,{'Cavalry':50})
Carthaginians.armies[0].laySiege(Athens)

print(genSongforCity(Athens))
Athens.siegeIter()
print(genSongforCity(Athens))
Athens.siegeIter()
print(genSongforCity(Athens))
Carthaginians.captureCity(Athens)
print(genSongforCity(Athens))