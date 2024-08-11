import datetime
from abc import abstractmethod, ABC


class Formatter(ABC):

    @abstractmethod
    def format(self, *args, **kwargs):
        pass


class SimpleFormatter(Formatter):

    def format(self, module, message, level):
        return f"[{level}] -- [{module}] -- {message}"


class DateTimeFormatter(Formatter):

    def format(self, module, message, level):
        datetime_now = datetime.datetime.now()
        return f"[{datetime_now}] --  [{level}] -- [{module}] -- {message}"



