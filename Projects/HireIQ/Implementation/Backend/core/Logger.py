
import logging
import os
from logging.handlers import RotatingFileHandler

IS_PROD = os.environ.get("DJANGO_SETTINGS_MODULE") == "core.settings.prod"

LOG_DIR = "logs"
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
        "%(asctime)s | %(levelname)-8s | %(funcName)-25s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    # 
    # Console handler (CloudWatch)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO if IS_PROD else logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    # 
    # File handler (LOCAL ONLY)
    if not IS_PROD:
        os.makedirs(LOG_DIR, exist_ok=True)
        # 
        file_handler = RotatingFileHandler(
            LOG_FILE,
            maxBytes=5 * 1024 * 1024,
            backupCount=5
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    # 
    return logger
