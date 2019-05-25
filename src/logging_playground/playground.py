import os
import sys
import logging
from logging.config import dictConfig
import config
import utils
from logging_module import loglog

logging.debug('A debug message')
logging.info('Some information')
logging.warning('A shot across the bows')


def main():
    logging.info("main")
    loglog.simple_function()


if __name__ == '__main__':
    os.makedirs(config.LOG_DIR, exist_ok=True)
    dictConfig(config.logging_config)
    utils.log_paths()
    for path_item in sys.path:
        logging.debug("{} is on path".format(path_item))

    main()
