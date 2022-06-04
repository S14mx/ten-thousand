import random

class GameLogic:

  def __init__(self,data):
    self.data = data
  
  @staticmethod
  def roll_dice():
    print(random.randrange(0,6))
    

# if __name__ == "__main__":
#   game1 = GameLogic(1)
#   game1.roll_dice()
