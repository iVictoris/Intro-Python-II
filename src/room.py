# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description):
    self.__name = name
    self.__description = description
    self.__n = None
    self.__e = None
    self.__w = None
    self.__s = None

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
    setattr(self, f'__{direction}', room)
    setattr(room, f'__{opposite_direction[direction]}', self)
  
  def get_room(self, direction):
    return getattr(self, f'__{direction}')

