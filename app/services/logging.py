import logging
from logging import Logger
from logging.handlers import RotatingFileHandler


def create_logger(module_name: str) -> Logger:
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(
        'main.log', maxBytes=50000000, backupCount=5, encoding='utf-8')
    formater = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formater)
    logger.addHandler(handler)
    return logger
