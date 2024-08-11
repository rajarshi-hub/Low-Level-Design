import random


class Player:
    pos = 0
    user_name = None

    def __init__(self, user_name):
        self.user_name = user_name

    def roll_die(self):
        return random.randint(1,6)


