from sys import stderr

from loguru import logger

logger.remove()
frmt = "<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan>{line}</cyan> - <white>{message}</white>"
logger.add(stderr, format=frmt)


def get_logger():
    return logger
