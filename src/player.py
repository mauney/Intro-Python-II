# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        # create empty set to keep track of rooms visited
        self.rooms_visited = set()

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
            # add romm to set of rooms visited
            self.rooms_visited.add(self.current_room)
