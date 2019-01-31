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
