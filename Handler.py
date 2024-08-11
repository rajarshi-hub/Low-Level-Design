from abc import abstractmethod, ABC


class Handler(ABC):

    def __init__(self, formatter):
        self.formatter = formatter

    @abstractmethod
    def add_log(self, message):
        pass


class ConsoleHandler(Handler):

    def add_log(self, message):
        print("Added log to console", message)


class FileHandler(Handler):

    def add_log(self, message):
        print("Added log to File", message)


class DBHandler(Handler):

    def add_log(self, message):
        print("Added Log to DB", message)
