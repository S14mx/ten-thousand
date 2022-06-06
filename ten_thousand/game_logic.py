import random
from collections import Counter


class GameLogic:

    @staticmethod
    def roll_dice(value):
        results = []
        for num in range(value):
            result = (random.randrange(1, 6))
            results.append(result)
        return tuple(results)

    @staticmethod
    def calculate_score(roll):
        roll_points = Counter(roll)
        score = 0

        # Handle 3 pairs and straight
        if (len(roll_points) == 3 and list(roll_points.values()) == [2, 2, 2]) or (len(roll_points) == 6):
            return 1500

        for dice in roll_points:
            number_of_occurrences = roll_points[dice]
            if number_of_occurrences < 3:
                value = 100 if dice == 1 else 50 if dice == 5 else 0
                score += value * number_of_occurrences
            else:
                value = 1000 if dice == 1 else dice * 100
                score += value * (number_of_occurrences - 2)

        return score
