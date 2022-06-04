import random


class GameLogic:

  def __init__(self,data):
    self.data = data
    self.next = next
  
  @staticmethod
  def roll_dice(value):
    results =[]
    for num in range(value):
      result = (random.randrange(1,6))
      results.append(result)
    return results
    