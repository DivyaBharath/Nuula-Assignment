import logging
import sys
from logging import Logger

FORMAT = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
LOGFILE = "dataparser.log"
LOGNAME = "dataparser"

DEFAULT_LEVEL = "INFO"

log_levels = {
    'DEBUG': logging.DEBUG,
    'ERROR': logging.ERROR,
    'FATAL': logging.FATAL,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING
}


def get_console_handler():
    """

    :return:
    """
    console_h = logging.StreamHandler(sys.stdout)
    console_h.setFormatter(FORMAT)
    return console_h


def set_level(log_level="INFO"):
    """

    :param log_level:
    :return:
    """
    logger_object = logging.root.manager.loggerDict[LOGNAME]

    level = log_levels.get(log_level.upper())
    if level:
        logger_object.setLevel(level)
    else:
        logger_object.error(f"Specified log level {log_level} not supported.")

def get_logger(**kwargs):
    """

    :param kwargs:
    :return:
    """
    logger: Logger = logging.getLogger(LOGNAME)

    if "log_level" in kwargs:
        user_log_level = kwargs["log_level"]
        log_level = log_levels.get(user_log_level.upper())

        if log_level:
            logger.setLevel(log_level)
    else:
        logger.setLevel(DEFAULT_LEVEL)

    logger.addHandler(get_console_handler())
    return logger
