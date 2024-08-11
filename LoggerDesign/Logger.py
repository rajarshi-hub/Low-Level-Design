import enum


class LoggerLevel(enum.Enum):
    WARNING = "Warning"
    ERROR = "Error"
    INFO = "Info"
    CRITICAL = "Critical"


class Logger:
    logger_instance = None

    # Check for passing self and cls, args and kwargs

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls.logger_instance:
            cls.logger_instance = super().__new__(cls)
        return cls.logger_instance

    def __init__(self, initial_handlers, formatter):
        self.handlers = initial_handlers

    def log(self, module, message, level):
        """
        :param module: Module to which the log belongs
        :param message: String message for log
        :param level: Level of the Log
        :return: None
        """
        for handler in self.handlers:
            log_message = handler.formatter.format(module, message, level)
            handler.add_log(log_message)

    def add_handlers(self, handler):
        self.handlers.append(handler)
