import sys
import logging


def utility_function(x):
    """
    do nothing but log
    :param x:
    :return:
    """
    logging.info("utility_function")
    logging.debug("x={}".format(x))
    return x


def log_paths():
    """
    log all of the things on path
    :return:
    """
    logging.info("log_paths")
    for path_item in sys.path:
        logging.debug("{} is on path".format(path_item))
