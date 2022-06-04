import random

class GameLogic:

  def __init__(self,data):
    self.data = data
  
  @staticmethod
  def roll_dice():
    return(random.randrange(0,6))
    