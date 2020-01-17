# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        #create empty list to hold items
        self.items = []
        # set initial connected rooms to None
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f'-----------------\n{self.name}\n'

    def get_next_room(self, direction):
        nav = {'n': self.n_to,
               'e': self.e_to,
               's': self.s_to,
               'w': self.w_to
               }
        return nav[direction]

    # add an item to the room
    def add_item(self, item):
        self.items.append(item)

    # return items currently in room
    def list_items(self):
        if len(self.items) == 0:
            return 'There are no items in this room.\n'

        item_str = f'{self.name} contains\n'
        for item in self.items:
            item_str += item.name + ', ' + item.description + ';\n'
        return item_str
