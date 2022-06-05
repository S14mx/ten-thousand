import random
from collections import Counter


class GameLogic:

    dice_value = {
        1: {"single": 100, "multiple": 1000},
        2: {"single": 0, "multiple": 200},
        3: {"single": 0, "multiple": 300},
        4: {"single": 0, "multiple": 400},
        5: {"single": 50, "multiple": 500},
        6: {"single": 0, "multiple": 600}
    }

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
                score += GameLogic.dice_value[dice]["single"] * number_of_occurrences
            else:
                score += GameLogic.dice_value[dice]["multiple"] * (number_of_occurrences - 2)

        return score
