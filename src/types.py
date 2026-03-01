class Ollivanders():

    def __init__(self):
        self.items = []

    def updateQuality(self):
        for item in self.items:
            item.updateQuality()

    def addItem(self,item):
        self.items.append(item)

    def toString(self):
        representation = ""
        for item in self.items:
            representation += item.toString()
        return representation
    
    def inventory(self):
        return self.items
    
    def nextDay(self):
        for item in self.items:
            item.updateQuality()
            print(item.toString())
    
class Interfaz():
    def updateQuality(self):
        pass

class Item:
    def __init__(self, name, quality, sellIn):
        self.name = name
        self.quality = quality
        self.sellIn = sellIn

    @property
    def getQuality(self):
        return self._quality

    @getQuality.setter
    def qualitySetter(self, quality):
        self._quality = max(0, min(50, quality))

class NormalItem(Interfaz,Item):
    def setSellIn(self,quantity):
        self.sellIn -= quantity
    
    def setQuality(self,quantity):
        self.quality -= quantity

    def updateQuality(self):
        self.setSellIn(1)
        if self.sellIn < 0:
            self.setQuality(2)
        else:
            self.setQuality(1)

class Sulfuras(NormalItem):
    def __init__(self):
        self.name = "Sulfuras, Hand of Ragnaros"
        self.quality = 80
        self.sellIn = 0

    def get_quality(self):
        return self.quality

    def get_sell_in(self):
        return self.sellIn
    
    def toString(self):
        return f'name= {self.name}, sell_in= {self.sellIn}, quality= {self.quality}'

class Conjured(NormalItem):
    def updateQuality(self):
        self.setSellIn(1)
        if self.sellIn > 0:
            self.setQuality(2)
        else:
            self.setQuality(4)

class Backstage(NormalItem):
    def updateQuality(self):
        self.setSellIn(1)
        if self.sellIn <= 0:
            self.quality = 0
        elif self.sellIn < 5:
            self.setQuality(-3)
        elif self.sellIn <= 10:
            self.setQuality(-2)
        else:
            self.setQuality(-1)
            
class AgedBrie(NormalItem):
    def updateQuality(self):
        self.setSellIn()
        if self.sellIn > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)