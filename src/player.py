# Write a class to hold player information, e.g. what room they are in
# currently.
from game import Game


class Player(Game):
    def __init__(self, name):
        super().__init__(name)
        self.__location = 'outside'
        self.__bag = []

    def loot_items(self, room):
        self.bag.append(room.items)
        room.clear_items()

    def _set_location(self, location):
        self.__location = location

    def _get_location(self):
        return self.__location

    location = property(_get_location, _set_location)
