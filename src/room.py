# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description):
    self.__name = name
    self.__description = description
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

