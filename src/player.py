# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
  def __init__(self, name, room):
    self.__name = name
    self.__current_room = room

  def __str__(self):
    return f'Player: {self.__name}, currently in room: {self.__current_room}'
  
  def get_room(self):
    return self.__current_room