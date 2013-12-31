class Faction:  
		def __init__(self,capital,cities):
                                self.capital = capital
                                self.cities = [capital]+cities
				
		def getManPower(self):
				return sum(map(lambda city:city.manPower,self.cities))
				
		def recruit(self,number):
				mp=getManPower()
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
		 def __init__(self,province,alleigance,geoX,geoY):
				self.manPower=0
				self.money=0            
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
                
                        
                        

                
