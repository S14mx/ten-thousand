import random
from collections import Counter

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
    return tuple(results)

  @staticmethod
  def calculate_score(roll):
    roll_points = Counter(roll)
    if roll_points == Counter({1: 1}):
      return 100
    elif roll_points == Counter({1: 2}):
      return 200
    elif roll_points == Counter({1: 3}):
      return 1000
    elif roll_points == Counter({1: 4}):
      return 2000
    elif roll_points == Counter({1: 5}):
      return 4000
    elif roll_points == Counter({2: 3}):
      return 200
    elif roll_points == Counter({2: 4}):
      return 400
    elif roll_points == Counter({2: 5}):
      return 600
    elif roll_points == Counter({2: 6}):
      return 800
    elif roll_points == Counter({3: 3}):
      return 300
    elif roll_points == Counter({3: 4}):
      return 600
    elif roll_points == Counter({3: 5}):
      return 900
    elif roll_points == Counter({3: 6}):
      return 1200
    elif roll_points == Counter({4: 3}):
      return 400
    elif roll_points == Counter({4: 4}):
      return 800
    elif roll_points == Counter({4: 5}):
      return 1200
    elif roll_points == Counter({4: 6}):
      return 1600
    elif roll_points == Counter({5: 1}):
      return 50
    elif roll_points == Counter({5: 2}):
      return 100
    elif roll_points == Counter({5: 3}):
      return 500
    elif roll_points == Counter({5: 4}):
      return 1000
    elif roll_points == Counter({5: 5}):
      return 1500
    elif roll_points == Counter({5: 6}):
      return 2000
    elif roll_points == Counter({6: 3}):
      return 600
    elif roll_points == Counter({6: 4}):
      return 1200
    elif roll_points == Counter({6: 5}):
      return 1800
    elif roll_points == Counter({6: 6}):
      return 2400
    else:
      return 0






    