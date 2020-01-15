# Write a class to hold item information, e.g. if the player is carrying it or
# what room it is in currently.

class Item:
    
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room