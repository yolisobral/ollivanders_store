class Ollivander:

    def __init__(self):
        self.items = []

    def updateQuality(self):
        for item in self.items:
            item.updateQuality()

    def addItem(self, item):
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
    

class Interfaz:
    def updateQuality(self):
        pass


class Item:
    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        # use setter to enforce bounds
        self.quality = quality

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, quality):
        self._quality = max(0, min(50, quality))

    # convenience method to match test expectations
    def getQuality(self):
        return self.quality

class NormalItem(Interfaz, Item):
    def setSellIn(self):
        self.sellIn -= 1

    def setQuality(self, quantity):
        # decreasing quality means subtracting, so positive quantity reduces
        self.quality -= quantity
        
    def updateQuality(self):
        self.setSellIn()
        if self.sellIn > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)

    def get_quality(self):
        return self.quality

    def get_sell_in(self):
        return self.sellIn
        
    def toString(self):
        return f'name= {self.name}, sell_in= {self.sellIn}, quality= {self.quality}'


class Sulfuras(Interfaz):
    def __init__(self):
        self.name = "Sulfuras, Hand of Ragnaros"
        # Sulfuras quality is fixed at 80 and never changes
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
        self.setSellIn()
        if self.sellIn > 0:
            self.setQuality(2)
        else:
            self.setQuality(4)


class Backstage(NormalItem):
    def updateQuality(self):
        self.setSellIn()
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