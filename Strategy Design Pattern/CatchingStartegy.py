from abc import abstractmethod, ABC


class CatchingStrategy(ABC):
    @abstractmethod
    def apply(self):
        pass


class KangarooCatchingStrategy(CatchingStrategy):

    def apply(self):
        print("Caught by Australian Kangaroo style")


class ReverseCupCatchingStrategy(CatchingStrategy):

    def apply(self):
        print("Caught by Reverse cup style")


class CupHandCatchingStrategy(CatchingStrategy):

    def apply(self):
        print("Caught by Cup Hand style")



