# Write a class to hold item information, e.g. if the player is carrying it or
# what room it is in currently.

class Item:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description