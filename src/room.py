from item import Item
# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description, items=[]):
    self.__name = name
    self.__description = description
    self.items = [Item(item) for item in items]
    self.n = None
    self.e = None
    self.w = None
    self.s = None

  def __str__(self):
    return f"{self.__name}"

  def __repr__(self):
    return f"Room({self.__name})"

  def assign_room(self, direction, room):
    opposite_direction = {
      's': 'n',
      'n': 's',
      'w': 'e',
      'e': 'w'
    }
    setattr(self, direction, room)
    setattr(room, opposite_direction[direction], self)
  
  def get_room(self, direction):
    return self[direction]

  def get_description(self):
    return self.__description

  def __contains__(self, item):
    for i in self.items:
      if str(i) == item:
        return True
        
  def remove_item(self, item):
    # slice up to index of item name 
    # concat the index after item
    item_location = 0
    for index in range(len(self.items)):
      if str(self.items[index]) == item:
        item_location = index
        break

    self.items = self.items[0:item_location] + self.items[item_location+1:]

  def add_item(self, item):
    item = Item(item)
    self.items.append(item)
