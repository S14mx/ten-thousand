import random
from collections import Counter


class GameLogic:

    @staticmethod
    def roll_dice(value=6):
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

    @staticmethod
    def get_scorers(roll):
        roll_points = Counter(roll)
        if (len(roll_points) == 3 and list(roll_points.values()) == [2, 2, 2]) or (len(roll_points) == 6):
            return roll

        output = []
        for dice in roll_points:
            number_of_occurrences = roll_points[dice]
            if (dice == 1 or dice == 5) or number_of_occurrences >= 3:
                output += [dice] * number_of_occurrences

        return tuple(output)

    @staticmethod
    def validate_keepers(roll, selection):
        if len(selection) != len(GameLogic.get_scorers(selection)) or len(GameLogic.get_scorers(selection)) == 0:
            return False

        roll_points = Counter(roll)
        selection_points = Counter(selection)
        for dice in selection_points:
            number_of_selected = selection_points[dice]
            number_in_roll = roll_points[dice]

            if number_of_selected > number_in_roll:
                return False
        return True
