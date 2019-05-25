import logging
import utils

logging.debug("top of loglog.py")
utils.log_paths()


def simple_function():
    logging.info("calling simple_function")
    utils.log_paths()
    print("print this instead of logging")
