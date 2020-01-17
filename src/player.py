# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        # create empty set to keep track of rooms visited
        self.rooms_visited = set()
        # create an empty starting inventory
        self.inventory = []

    def move(self, direction):
        new_room = self.current_room.get_next_room(direction)
        if new_room is not None:
            self.current_room = new_room
            print(self.current_room)
            self.first_visit_check()
        else:
            print('Travel in that direction is not possible.\n')

    def first_visit_check(self):
        if self.current_room not in self.rooms_visited:
            # descripe room on first visit
            print(self.current_room.description)
            # list the possible travel directions
            # TODO
            # add romm to set of rooms visited
            self.rooms_visited.add(self.current_room)

    # return items currently on player
    def list_inventory(self):
        if len(self.inventory) == 0:
            return 'You have no items.\n'

        item_str = f'{self.name} has\n'
        for item in self.inventory:
            item_str += item.name + ', ' + item.description + ';\n'
        return item_str

    def pickup_item(self, item_name):
        new_item = next((x for x in self.current_room.items if x.name == item_name), None)
        if new_item is not None:
            self.inventory.append(new_item)
            self.current_room.items.remove(new_item)
            new_item.on_take()
        else:
            print(f"{item_name.capitalize()} is not available.")

    def drop_item(self, item_name):
        old_item = next((x for x in self.inventory if x.name == item_name), None)
        if old_item is not None:
            self.current_room.items.append(old_item)
            self.inventory.remove(old_item)
            old_item.on_drop()
        else:
            print(f"You do not have a {item_name}.")
