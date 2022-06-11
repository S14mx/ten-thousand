
from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class EndOfGame(Exception):
    pass


class Game:
    def __init__(self, round_counter=1):
        self.round_counter = round_counter

    def __capture_input(self, text):
        user_response = input(text)
        if user_response == "q":
            raise EndOfGame
        return user_response

    def handle_shelf(self, answer, banker, calculate, roll):
        answer_to_int = tuple(int(dice) for dice in answer)
        calc_points = calculate(answer_to_int)
        banker.shelf(calc_points)
        print(f"You have {banker.shelved} unbanked points and {len(roll) - len(answer_to_int)} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")

    def handle_roll(self, roller, num=6):
        roll = roller(num)
        roll_str = ""
        for dice in roll:
            roll_str += str(dice) + " "
        print(f"*** {roll_str}***")
        print("Enter dice to keep, or (q)uit:")

    def handle_bank(self, banker):
        print(f"You banked {banker.shelved} points in round {self.round_counter}")
        banker.bank()
        self.round_counter += 1
        print(f"Total score is {banker.balance} points")

    def play(self, roller=GameLogic.roll_dice, calculate=GameLogic.calculate_score, banker=Banker()):
        try:
            print("Welcome to Ten Thousand")
            print("(y)es to play or (n)o to decline")
            answer = self.__capture_input("> ")
            if answer == 'n':
                print("OK. Maybe another time")
            else:
                print(f"Starting round {self.round_counter}")
                print("Rolling 6 dice...")
                roll = roller(6)
                roll_str = ""
                for dice in roll:
                    roll_str += str(dice) + " "
                print(f"*** {roll_str}***")
                print("Enter dice to keep, or (q)uit:")
                # self.handle_roll(roller)
                answer = self.__capture_input("> ")
                self.handle_shelf(answer, banker, calculate, roll)
                answer = self.__capture_input("> ")
                if answer == "b":
                    self.handle_bank(banker)
                    print(f"Starting round {self.round_counter}")
                    print("Rolling 6 dice...")
                    self.handle_roll(roller)
                    answer = self.__capture_input("> ")
                    self.handle_shelf(answer, banker, calculate, roll)
                    answer = self.__capture_input("> ")
                    if answer == "b":
                        self.handle_bank(banker)
                        print(f"Starting round {self.round_counter}")
                        print("Rolling 6 dice...")
                        self.handle_roll(roller)
                        answer = self.__capture_input("> ")

        except EndOfGame:
            print(f"Thanks for playing. You earned {banker.balance} points")
            banker.clear_balance()


if __name__ == "__main__":
    game = Game()
    game.play()
