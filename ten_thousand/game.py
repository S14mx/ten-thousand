
from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class EndOfGame(Exception):
    pass


class Game:
    def __init__(self, round_counter=1, roll_num=6):
        self.round_counter = round_counter
        self.roll_num = roll_num
        self.roller = None
        self.calculate = None
        self.banker = None
        self.show_round_message = True

    def __capture_input(self, text):
        user_response = input(text)
        if user_response == "q":
            raise EndOfGame
        return user_response

    def __answer_to_int(self, answer):
        return tuple(int(dice) for dice in answer if dice.isnumeric())

    def handle_shelf(self, answer):
        answer_to_int = self.__answer_to_int(answer)
        self.roll_num = self.roll_num - len(answer_to_int)
        calc_points = self.calculate(answer_to_int)
        self.banker.shelf(calc_points)
        print(f"You have {self.banker.shelved} unbanked points and {self.roll_num} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        if self.roll_num == 0:
            self.roll_num = 6

    def handle_roll(self, roller, num=6):
        roll = roller(num)
        roll_str = ""
        for dice in roll:
            roll_str += str(dice) + " "
        print(f"Rolling {num} dice...")
        print(f"*** {roll_str}***")
        print("Enter dice to keep, or (q)uit:")

    def handle_bank(self):
        print(f"You banked {self.banker.shelved} points in round {self.round_counter}")
        self.banker.bank()
        self.round_counter += 1
        self.show_round_message = True
        self.roll_num = 6
        print(f"Total score is {self.banker.balance} points")

    def handle_round(self, dice=6):
        if self.show_round_message:
            print(f"Starting round {self.round_counter}")
            self.show_round_message = False

        print(f"Rolling {dice} dice...")
        roll = self.roller(dice)
        roll_str = ""
        for dice in roll:
            roll_str += str(dice) + " "
        print(f"*** {roll_str}***")
        if len(GameLogic.get_scorers(roll)) == 0:
            print("****************************************")
            print("**        Zilch!!! Round over         **")
            print("****************************************")
            self.banker.clear_shelf()
            self.handle_bank()
            return

        print("Enter dice to keep, or (q)uit:")
        answer = self.__capture_input("> ")
        while not GameLogic.validate_keepers(roll, self.__answer_to_int(answer)):
            print("Cheater!!! Or possibly made a typo...")
            print(f"*** {roll_str}***")
            print("Enter dice to keep, or (q)uit:")
            answer = self.__capture_input("> ")

        self.handle_shelf(answer)
        answer = self.__capture_input("> ")
        if answer == "b":
            self.handle_bank()

    def play(self, roller=GameLogic.roll_dice, calculate=GameLogic.calculate_score, banker=Banker()):
        try:
            self.roller = roller
            self.calculate = calculate
            self.banker = banker

            self.banker.clear_shelf()
            self.banker.clear_balance()

            print("Welcome to Ten Thousand")
            print("(y)es to play or (n)o to decline")
            answer = self.__capture_input("> ")
            if answer == 'n':
                print("OK. Maybe another time")
            else:
                while self.round_counter <= 20:
                    self.handle_round(self.roll_num)
                raise EndOfGame

        except EndOfGame:
            print(f"Thanks for playing. You earned {self.banker.balance} points")


if __name__ == "__main__":
    game = Game()
    game.play()
