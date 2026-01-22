
import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "hireiq.log")

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # 
    if logger.handlers:
        return logger
    # 
    logger.propagate = False
    # 
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(funcName)-25s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    # 
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    # 
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    # 
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    # 
    return logger
