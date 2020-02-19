import random


class Game:
    def __init__(self):
        self.user_choice = ""
        self.choices = ["rock", "paper", "scissors"]
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

    def set_choice(self, new_choice):
        self.user_choice = new_choice

    def set_status(self, state):
        self.play_game = state

    def set_name(self, new_name):
        self.user_name = new_name

    def greeting(self):
        self.set_name(input("Enter your name: ").strip())
        print(f"Hello, {self.get_name()}")
        if self.get_name() not in self.scoreboard:
            self.scoreboard[self.get_name()] = 0
            self.save_score()

    def save_score(self):
        save_file = open('rating.txt', 'w')
        for key, value in self.scoreboard.items():
            print(save_file)
            print(key, value, file=save_file, flush=True)
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
        index = random.randint(0, 2)
        self.computer_choice = self.choices[index]
        return self.computer_choice

    def game_result(self):
        self.random_choice()
        if self.get_choice() == self.computer_choice:
            print(f"There is a draw ({self.get_choice()})")
            self.outcome = "draw"
        elif self.get_choice() == "rock":
            if self.computer_choice == "paper":
                print(f"Sorry, but computer chose {self.computer_choice}")
                self.outcome = "loose"
            elif self.computer_choice == "scissors":
                print(f"Well done. Computer chose {self.computer_choice} and failed")
                self.outcome = "win"
        elif self.get_choice() == "paper":
            if self.computer_choice == "scissors":
                print(f"Sorry, but computer chose {self.computer_choice}")
                self.outcome = "loose"
            elif self.computer_choice == "rock":
                print(f"Well done. Computer chose {self.computer_choice} and failed")
                self.outcome = "win"
        elif self.get_choice() == "scissors":
            if self.computer_choice == "rock":
                print(f"Sorry, but computer chose {self.computer_choice}")
                self.outcome = "loose"
            elif self.computer_choice == "paper":
                print(f"Well done. Computer chose {self.computer_choice} and failed")
                self.outcome = "win"
        game.update_score()

    def game_loop(self):
        while self.play_game is True:
            self.set_choice(input())
            if self.get_choice() == "!exit":
                self.set_status(False)
                print("Bye!")
            elif self.get_choice() == '!rating':
                self.print_rating()
            else:
                self.game_result()


game = Game()
game.greeting()
game.game_loop()
