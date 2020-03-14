# Write a class to hold player information, e.g. what room they are in
# currently.
from game import Game


class Player(Game):
    def __init__(self, name):
        super().__init__(name)
        self.location = 'Outside'
        self.bag = []
