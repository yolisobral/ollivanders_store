class Ollivanders():

    def __init__(self,items):
        self.items = items

    def updateQuality(self):
        for item in self.items:
            item.updateQuality()
    
class Interfaz():
    def updateQuality(self):
        pass

class Item:
     def __init__(self, name, quality, sellIn):
        self.name = name
        self.quality = quality
        self.sellIn = sellIn

class NormalItem(Interfaz,Item):
    pass
    
class Sulfuras(NormalItem):
    pass
class Conjured(NormalItem):
    pass
class Backstage(NormalItem):
    pass
class AgedBrie(NormalItem):
    pass