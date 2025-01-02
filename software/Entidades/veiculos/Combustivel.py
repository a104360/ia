class Combustivel:
    def __init__(self,level,limit,consumption = 10):
        """
            level - indica o nivel de combustivel (litros)

            consumption - indica os litros consumidos a cada 100Km
        """
        self.level = level
        self.limit = limit
        self.consumption = consumption

    def to_dict(self):
        return {
            "level" : self.level,
            "limit" : self.limit,
            "consumption" : self.consumption
        }

    def from_dict(self,dict):
        return Combustivel(
            dict["level"], 
            dict["limit"], 
            dict["consumption"]
        )
        


    def __str__(self):
        return f"Nivel (litros) : {self.level}L\nLimite (litros) : {self.limit}L\nConsumo: {self.consumption}L/100Km\n"

    def spend(self,km : int):
        """Decreases the amount of fuel in the tank, according to the consumption by 100Km"""
        decrease = round((km * self.consumption)/100) 
        if decrease > self.level:
            self.level = 0
            return
        self.level -= decrease
    
    def fill(self,liters = 10000):
        """
            Increases the amount of fuel, regarding the limit
            
            If no amount is passed, it either goes up to the limit or 10000L, if the limit is greater than 10000L
        """
        increase = self.level + liters
        if increase > self.limit:
            self.level = self.limit
            return 
        self.level = increase
    
    def getLevel(self):
        """Returns the amount of fuel remaining in the tank"""
        return self.level
    
    def getAutonomy(self):
        """Returns the amount of Kilometers that the tank supports"""
        remaining = round((self.level * 100) / self.consumption)
        return remaining
    
    def getConsumption(self):
        """Returns the consumption in L/100Km"""
        return self.consumption