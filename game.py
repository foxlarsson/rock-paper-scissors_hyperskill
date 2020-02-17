import random


class Game:
    def __init__(self):
        self.user_choice = ""
        self.choices = ["rock", "paper", "scissors"]
        self.computer_choice = ""
        self.play_game = True

    def get_choice(self):
        return self.user_choice

    def get_status(self):
        return self.play_game

    def set_choice(self, new_choice):
        self.user_choice = new_choice

    def set_status(self, state):
        self.play_game = state

    def random_choice(self):
        random.seed()
        index = random.randint(0, 2)
        self.computer_choice = self.choices[index]
        return self.computer_choice

    def game_result(self):
        self.random_choice()
        if self.get_choice() == self.computer_choice:
            print(f"There is a draw ({self.get_choice()})")
        elif self.get_choice() == "rock":
            if self.computer_choice == "paper":
                print(f"Sorry, but computer chose {self.computer_choice}")
            elif self.computer_choice == "scissors":
                print(f"Well done. Computer chose {self.computer_choice} and failed")
        elif self.get_choice() == "paper":
            if self.computer_choice == "scissors":
                print(f"Sorry, but computer chose {self.computer_choice}")
            elif self.computer_choice == "rock":
                print(f"Well done. Computer chose {self.computer_choice} and failed")
        elif self.get_choice() == "scissors":
            if self.computer_choice == "rock":
                print(f"Sorry, but computer chose {self.computer_choice}")
            elif self.computer_choice == "paper":
                print(f"Well done. Computer chose {self.computer_choice} and failed")

    def game_loop(self):
        while self.play_game is True:
            self.set_choice(input())
            if self.get_choice() == "!exit":
                self.set_status(False)
            else:
                self.game_result()


game = Game()
game.game_loop()
