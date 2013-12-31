class Faction:
                manPower = 0
                money= 0
                supply = 0
                
                def __init__(self,capital,cities):
                        self.capital = capital 
                        self.cities = cities
                        for i in capital+cities :
                            self.manPower += i.manPower
                            self.money += i.money
                            self.supply += supply
    
                def getManPower(self):
                        return self.manPower

                def getMoney (self):
                        return self.money

                

class City:

                manPower = 0
                money = 0
                supply = 0
                destroyed = False
                beseiged = False
                

                def __init__(self,province,alleigance,geoX,geoY):
                        self.province = province
                        self.geoX = geoX
                        self.geoY = geoY
                        self.alleigance = alleigance

                def besiege(self):
                        self.besieged = True
#                        self.money *= 0.33
#                        self.manPower *= 0.33
#                        self.supply *= 0.33

                def destroy(self):
                        self.destroyed = True               

class superFaction(Faction):

                armies = []
                navies = []
              

                def __init__(self,allies,enemies):
                        self.allies =[]
                        self.enemies = []

                def changeCapital(capital):
                        self.capital = capital


class Province:

            def 
                
                        
                        

                
