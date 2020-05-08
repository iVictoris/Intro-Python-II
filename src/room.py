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
