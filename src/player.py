from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
  def __init__(self, name, room, inventory=[]):
    self.__name = name
    self.__current_room = room
    self.inventory = inventory

  def __str__(self):
    room = self.__current_room
    return f'''Player: {self.__name}, currently in room: {self.__current_room}

    \t\t\t Map Overview:

    \t\t\t\t{room.n}
    \t{room.w}\t\t{room}\t\t\t{room.e}
    \t\t\t\t{room.s}
    
    Other info:
    Items: {', '.join([str(item) for item in room.items])}'''
  
  def get_room(self):
    return self.__current_room

  def enter_room(self, direction):
    next_room = getattr(self.__current_room, direction)
    if not next_room:
      raise ValueError()
    self.__current_room = next_room

  def add_item(self, item):
    item = Item(item)
    self.inventory.append(item)
    item.on_take()
    

