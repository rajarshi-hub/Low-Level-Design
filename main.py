from Logger import Logger, LoggerLevel
from Formatter import SimpleFormatter, DateTimeFormatter
from Handler import ConsoleHandler, DBHandler, FileHandler

message = "User Data not found"
module = "User Segment"
level = LoggerLevel('Error')
handlers = [ConsoleHandler(SimpleFormatter()), DBHandler(DateTimeFormatter())]
formatter = SimpleFormatter()
logger = Logger(handlers, formatter)
logger.log(module, message, level)
message = "Multiple users found with name Parrot"
module = "FTP"
level = LoggerLevel.INFO.value
logger.add_handlers(FileHandler(DateTimeFormatter()))
logger.log(module, message, level)
