# Implement a class to hold room information. This should have name and
# description attributes.

from game import Game


class Room(Game):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description
        self.__items = []
        self.rooms = {
            'north': None,
            'south': None,
            'west': None,
            'east': None
        }

    def add_items(self, item):
        self.items.append(item)

    def _get_items(self):
        return self.items

    def clear_items(self):
        self.items = []

    def __str__(self):
        return f"Room: {self.name}"

    items = property(_get_items)
