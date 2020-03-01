import random


class Game:
    def __init__(self):
        self.user_choice = ""
        self.default_options = ["rock", "paper", "scissors"]
        self.user_options = []
        self.winning_options = []
        self.losing_options = []
        self.computer_choice = ""
        self.play_game = True
        self.scoreboard = {}
        self.user_name = ""
        self.outcome = ""

    def get_choice(self):
        return self.user_choice

    def get_status(self):
        return self.play_game

    def get_score(self):
        return self.scoreboard

    def get_name(self):
        return self.user_name

    def get_options(self):
        if not self.user_options:
            return self.default_options
        else:
            return self.user_options

    def get_winning(self):
        return self.winning_options

    def set_choice(self, new_choice):
        self.user_choice = new_choice

    def set_status(self, state):
        self.play_game = state

    def set_name(self, new_name):
        self.user_name = new_name

    def set_options(self):
        options = input().replace(' ', '')
        if options != "":
            self.user_options = options.split(',')
            if len(self.user_options) % 2 == 0:
                del(self.user_options[0])
        print("Okay, let's start")

    def set_winning(self, winning):
        self.winning_options = winning

    def reset_winning(self):
        self.winning_options.clear()

    def greeting(self):
        self.set_name(input("Enter your name: ").strip())
        print(f"Hello, {self.get_name()}")
        if self.get_name() not in self.scoreboard:
            self.scoreboard[self.get_name()] = 0
            self.save_score()

    def save_score(self):
        save_file = open('rating.txt', 'w')
        for key, value in self.scoreboard.items():
            content = key + " " + str(value) + "\n"
            save_file.write(content)
            save_file.flush()
        save_file.close()

    def write_score_from_file(self):
        write_file = open('rating.txt')
        self.scoreboard.clear()
        for line in write_file:
            items = line.split()
            self.scoreboard[items[0]] = int(items[1])
        write_file.close()

    def update_score(self):
        if self.outcome == "win":
            self.scoreboard[self.get_name()] += 100
        elif self.outcome == "draw":
            self.scoreboard[self.get_name()] += 50
        self.save_score()

    def print_rating(self):
        print_file = open('rating.txt')
        for line in print_file:
            items = line.split()
            if items[0] == self.get_name():
                print(f"Your rating: {items[1]}")
        print_file.close()

    def random_choice(self):
        random.seed()
        options = self.get_options()
        index = random.randint(0, len(options) - 1)
        self.computer_choice = options[index]
        return self.computer_choice

    def loose(self):
        print(f"Sorry, but computer chose {self.computer_choice}")
        self.outcome = "loose"

    def win(self):
        print(f"Well done. Computer chose {self.computer_choice} and failed")
        self.outcome = "win"

    def game_result(self):
        self.random_choice()
        if self.get_choice() == self.computer_choice:
            print(f"There is a draw ({self.get_choice()})")
            self.outcome = "draw"
        elif self.computer_choice in self.get_winning():
            self.win()
        else:
            self.loose()
        game.update_score()

    def evaluate_options(self):
        user_word = self.get_options().index(self.get_choice())
        options = self.get_options()
        start = user_word - 1
        end = user_word - len(options) // 2
        winning = []
        for i in range(min(start, end), max(start, end) + 1):
            winning.append(options[i])
        self.set_winning(winning)

    def game_loop(self):
        while self.play_game is True:
            self.set_choice(input())
            if self.get_choice() == "!exit":
                self.set_status(False)
                print("Bye!")
            elif self.get_choice() == '!rating':
                self.print_rating()
            else:
                self.evaluate_options()
                self.game_result()
            self.reset_winning()


game = Game()
game.write_score_from_file()
game.greeting()
game.set_options()
game.game_loop()
game.update_score()
