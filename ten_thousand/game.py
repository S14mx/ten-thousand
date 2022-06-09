class Game:

    def __init__(self):
        pass

    def play(self, roller):
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        answer = input("> ")
        if answer == 'n':
            print(f"OK. Maybe another time")
        # print(f"Step right up and guess {self.riddle}!")
