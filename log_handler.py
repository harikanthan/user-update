import logging
import sys


class LogHandler():

    def __init__(self, name, console_level, file_level, file_name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s %(message)s', "%Y-%m-%d %H:%M:%S")

        # File handler
        self.file_handler = logging.FileHandler(file_name, 'a')
        self.file_handler.setLevel(file_level)
        self.file_handler.setFormatter(formatter)
        self.logger.addHandler(self.file_handler)

        # # Console handler
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(console_level)
        self.console_handler.setFormatter(formatter)
        self.logger.addHandler(self.console_handler)

    def getLogger(self):
        return self.logger


def getLogger(console_level=None, file_level=None, file_name=None):
    if file_name == None: file_name = 'script.log'
    if file_level == None: file_level = logging.DEBUG
    if console_level == None: console_level = logging.DEBUG
    logHandler = LogHandler(__name__, console_level, file_level, file_name)
    return logHandler.getLogger()
