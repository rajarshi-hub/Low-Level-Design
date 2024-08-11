
class Fielder:

    def __init__(self, catching_strategy):
        self.catching_strategy = catching_strategy

    def catch(self):
        self.catching_strategy.apply()
