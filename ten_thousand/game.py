from unicodedata import name
from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    def __init__(self):
        pass

    def handle_roll(self, roller=GameLogic.roll_dice):
        roll = roller(6)
        roll_str = ""
        for dice in roll:
            roll_str += str(dice) + " "
        print(f"*** {roll_str}***")
        print("Enter dice to keep, or (q)uit:")

    def play(self, roller=GameLogic.roll_dice, calculate=GameLogic.calculate_score, banker=Banker()):
        round_counter = 1
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        answer = input("> ")
        if answer == 'n':
            print("OK. Maybe another time")
        else:
            print(f"Starting round {round_counter}")
            print("Rolling 6 dice...")
            roll = roller(6)
            roll_str = ""
            for dice in roll:
                roll_str += str(dice) + " "
            print(f"*** {roll_str}***")
            print("Enter dice to keep, or (q)uit:")
            answer = input("> ")

            if answer == "q":
                print("Thanks for playing. You earned 0 points")

            else:
                answer_to_int = tuple(int(dice) for dice in answer)
                calc_points = calculate(answer_to_int)
                banker.shelf(calc_points)
                print(f"You have {banker.shelved} unbanked points and {len(roll) - len(answer_to_int)} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")

                answer = input("> ")
                if answer == "b":
                    print(f"You banked {banker.shelved} points in round {round_counter}")
                    banker.bank()
                    round_counter += 1
                    print(f"Total score is {banker.balance} points")
                    print(f"Starting round {round_counter}")
                    print("Rolling 6 dice...")
                    roll = roller(6)
                    roll_str = ""
                    for dice in roll:
                        roll_str += str(dice) + " "
                    print(f"*** {roll_str}***")
                    print("Enter dice to keep, or (q)uit:")
                    answer = input("> ")
                    if answer == "q":
                        print(f"Thanks for playing. You earned {banker.balance} points")
                    else:
                        answer_to_int = tuple(int(dice) for dice in answer)
                        calc_points = calculate(answer_to_int)
                        banker.shelf(calc_points)
                        print(f"You have {banker.shelved} unbanked points and {len(roll) - len(answer_to_int)} dice remaining")
                        print("(r)oll again, (b)ank your points or (q)uit:")
                        answer = input("> ")
                        if answer == "b":
                            print(f"You banked {banker.shelved} points in round {round_counter}")
                            banker.bank()
                            round_counter += 1
                            print(f"Total score is {banker.balance} points")
                            print(f"Starting round {round_counter}")
                            print("Rolling 6 dice...")
                            roll = roller(6)
                            roll_str = ""
                            for dice in roll:
                                roll_str += str(dice) + " "
                            print(f"*** {roll_str}***")
                            print("Enter dice to keep, or (q)uit:")
                            answer = input("> ")


if __name__ == "__main__":
    game = Game()
    game.play()
